"""Tests for the utils module."""

from src.utils.common import allowed_file, get_file_extension

def test_allowed_file():
  """Test the allowed file function."""
  assert allowed_file('test.pdf') is True
  assert allowed_file('test.png') is True
  assert allowed_file('test.jpg') is True
  assert allowed_file('test.jpeg') is True
  assert allowed_file('test.bmp') is False
  assert allowed_file('test.gif') is False
  assert allowed_file('test.tiff') is False


def test_get_file_extension():
  """Test the get file extension function."""
  assert get_file_extension('test.pdf') == '.pdf'
  assert get_file_extension('test.jpg') == '.jpg'
  assert get_file_extension('test.jpeg') == '.jpeg'
  assert get_file_extension('test.png') == '.png'
