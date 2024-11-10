from pdf2image import convert_from_path
from PIL import Image
import pytesseract

SUPPORTED_FILE_TYPES = [".pdf", ".jpg", ".jpeg", ".png"]

# TODO: refactor to use images from request/memory instead of file path
def ocr_extract_text(image_path: str) -> str:
  """Extract text from an image using Tesseract OCR. 
  If the file is a PDF, it will be converted to images and then processed.
  """

  if not image_path.endswith(SUPPORTED_FILE_TYPES):
    raise ValueError(f"Unsupported file type: {image_path}")

  if image_path.endswith(".pdf"):
    images = convert_from_path(image_path)
    text = ""
    for image in images:
      text += pytesseract.image_to_string(image)
    return text

  image = Image.open(image_path)
  text = pytesseract.image_to_string(image)
  return text
