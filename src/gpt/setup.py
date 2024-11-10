__package__ = "gpt"
import os
from ocr.extract import ocr_extract_text
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY")
)


few_shot_prompts = """
Classify a document based on its content. 
Here are examples of different types of documents:

"""

LABEL_BANK_STATEMENT="bank-statement"
LABEL_INVOICE="invoice"
LABEL_DRIVER_LICENSE="driver-license"

allowed_labels = {'bank-statement', 'invoice', 'driver-license', 'other'}

training_files = {
  "bank_statement_1.pdf": list(allowed_labels)[0],
  "bank_statement_2.pdf": list(allowed_labels)[0],
  "bank_statement_3.pdf": list(allowed_labels)[0],
  "drivers_license_1.jpg": list(allowed_labels)[1],
  "drivers_license_2.jpg": list(allowed_labels)[1],
  "drivers_license_3.jpg": list(allowed_labels)[1],
  "invoice_1.pdf": list(allowed_labels)[2],
  "invoice_2.pdf": list(allowed_labels)[2],
  "invoice_3.pdf": list(allowed_labels)[2],
}

def get_prompt(base_files: dict):
  """
  Get the prompt for the document classifier.
  """
  prompt = few_shot_prompts
  example_count = 1
  for file, label in base_files.items():
    fileText = ocr_extract_text(f"./files/{file}")

    prompt += f"Example {example_count}:\nText:\"{fileText}\"\nLabel:\"{label}\"\n\n"
    example_count += 1

  prompt += "Classify the following document:\n\n\"{text}\""
  return prompt

base_prompt = get_prompt(training_files)

def classify_document(text: str):
  """
  Classify a document based on its text.
  """
  prompt = base_prompt.format(text=text)

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system", 
        "content": f"""
        You are a document classifier. You will be given text extracts from a document and 
        you need to classify it into one of the following categories: {allowed_labels}. 
        Return only the label, not the text, without any other text or formatting.
        """
      },
      {"role": "user", "content": prompt}
    ]
  )

  document_type = response.choices[0].message.content
  return document_type
