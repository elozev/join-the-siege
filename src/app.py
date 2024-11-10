"""Main application file."""

from flask import Flask
from src.routes.files import files_bp

app = Flask(__name__)

API_V1 = '/api/v1'

app.register_blueprint(files_bp, url_prefix=f"{API_V1}/files")

if __name__ == '__main__':
  app.run(debug=True)
