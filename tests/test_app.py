"""Tests for the application."""

from io import BytesIO

import pytest
from src.app import app
from src.utils.common import allowed_file

@pytest.fixture
def client():
  """Fixture to create a test client."""
  app.config['TESTING'] = True
  with app.test_client() as client:
    yield client


@pytest.mark.parametrize("filename, expected", [
    ("file.pdf", True),
    ("file.png", True),
    ("file.jpg", True),
    ("file.txt", False),
    ("file", False),
])

def test_allowed_file(filename, expected):
  """Test the allowed file."""
  assert allowed_file(filename) == expected

def test_no_file_in_request(client):
  """Test the no file in request."""
  response = client.post('/api/v1/files/classify-file')
  assert response.status_code == 400

def test_no_selected_file(client):
  """Test the no selected file."""
  data = {'file': (BytesIO(b""), '')}
  response = client.post('/api/v1/files/classify-file', data=data, content_type='multipart/form-data')
  assert response.status_code == 400

def test_success(client, mocker):
  """Test the success case."""
  mocker.patch('src.routes.files.ocr_extract_text', return_value='dummy content')
  mocker.patch('src.routes.files.classify_document', return_value='test_class')
  data = {'file': (BytesIO(b"dummy content"), 'file.pdf')}
  response = client.post('/api/v1/files/classify-file', data=data, content_type='multipart/form-data')
  assert response.status_code == 200
  assert response.get_json() == {"file_type": "test_class"}
