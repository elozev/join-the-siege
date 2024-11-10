"""Functions for parsing images and PDFs using Tesseract OCR."""

from io import BytesIO
from pdf2image import convert_from_bytes, convert_from_path
import pytesseract
from PIL import Image
from src.utils.constants import SUPPORTED_FILE_TYPES

def stream_to_bytes(file):
  """Convert a file stream to bytes."""
  bytes_data = BytesIO(file.read()).getvalue()
  return bytes_data

def ocr_extract_text_from_path(image_path: str) -> str:
  """Extract text from an image using Tesseract OCR. 
  If the file is a PDF, it will be converted to images and then processed.
  """
  if not image_path.endswith(tuple(SUPPORTED_FILE_TYPES)):
    raise ValueError(f"Unsupported file type: {image_path}")

  if image_path.lower().endswith(".pdf"):
    images = convert_from_path(image_path)
    text = ""
    for image in images:
      text += pytesseract.image_to_string(image)
    return text

  image = Image.open(image_path)
  text = pytesseract.image_to_string(image)
  return text


def ocr_extract_text(file, file_type: str) -> str:
  """Extract text from an image using Tesseract OCR. 
  If the file is a PDF, it will be converted to images and then processed.
  """

  if file_type.lower() == "pdf":
    image_bytes = stream_to_bytes(file)
    images = convert_from_bytes(image_bytes)
    text = ""
    for image in images:
      text += pytesseract.image_to_string(image)
    return text

  image = Image.open(file.stream)
  text = pytesseract.image_to_string(image)
  return text
