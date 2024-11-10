"""Routes for the files API."""

from flask import Blueprint, request, jsonify
from src.ocr.parsers import ocr_extract_text
from src.gpt.setup import classify_document
from src.utils.common import get_file_extension, allowed_file
files_bp = Blueprint('files', __name__)

@files_bp.route('/', methods=['GET'])
def index():
  """Endpoint used to wake up Google Cloud Run."""
  return jsonify({"message": "Welcome to the files API!"}), 200


@files_bp.route('/classify-file', methods=['POST'])
def classify_file_route():
  """Classify the file and return the file class."""
  if 'file' not in request.files:
    return jsonify({"error": "No file part in the request"}), 400

  file = request.files['file']
  if file.filename == '':
    return jsonify({"error": "No selected file"}), 400

  file_type = get_file_extension(file.filename)

  if not allowed_file(file.filename):
    return jsonify({"error": f"File type {file_type} not allowed"}), 400

  text = ocr_extract_text(file, file_type)

  file_type = classify_document(text)

  return jsonify({"file_type": file_type}), 200
