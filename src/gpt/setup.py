"""Setup for the GPT-3.5-turbo document classifier."""

import os
from openai import OpenAI
from dotenv import load_dotenv
from src.ocr.parsers import ocr_extract_text_from_path
from src.utils.constants import ALLOWED_LABELS, TRAINING_FILES

load_dotenv()

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY")
)

FEW_SHOT_PROMPTS = """
Classify a document based on its content. 
Here are examples of different types of documents:

"""

def get_prompt(base_files: dict):
  """
  Get the prompt for the document classifier.
  """
  prompt = FEW_SHOT_PROMPTS
  example_count = 1
  for file, label in base_files.items():
    text = ocr_extract_text_from_path(f"./files/{file}")

    prompt += f"Example {example_count}:\nText:\"{text}\"\nLabel:\"{label}\"\n\n"
    example_count += 1

  prompt += "Classify the following document:\n\n\"{text}\""
  return prompt

def classify_document(text: str):
  """
  Classify a document based on its text.
  """
  base_prompt = get_prompt(TRAINING_FILES)

  prompt = base_prompt.format(text=text)

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system", 
        "content": f"""
        You are a document classifier. You will be given text extracts from a document and 
        you need to classify it into one of the following categories: {ALLOWED_LABELS.values()}.
        Return only the label, not the text, without any other text or formatting.
        """
      },
      {"role": "user", "content": prompt}
    ]
  )

  document_type = response.choices[0].message.content or "other"
  return document_type
