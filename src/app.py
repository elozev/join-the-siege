from flask import Flask, request, jsonify
from src.classifier import classify_file
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
  """Check if the file extension is allowed."""
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/classify-file', methods=['POST'])
def classify_file_route():
  """Classify the file and return the file class."""
  if 'file' not in request.files:
    return jsonify({"error": "No file part in the request"}), 400

  file = request.files['file']
  if file.filename == '':
    return jsonify({"error": "No selected file"}), 400

  if not allowed_file(file.filename):
    return jsonify({"error": f"File type {file.filename.split('.')[1].lower()} not allowed"}), 400

  file_class = classify_file(file)
  return jsonify({"file_class": file_class}), 200


if __name__ == '__main__':
  app.run(debug=True)
