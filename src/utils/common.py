"""Some utility functions for the application."""

from src.utils.constants import SUPPORTED_FILE_TYPES

def get_file_extension(filename):
  """Get the file extension from the filename."""
  return '.' + filename.rsplit('.', 1)[1].lower()

def allowed_file(filename):
  """Check if the file extension is allowed."""
  return '.' in filename and get_file_extension(filename) in SUPPORTED_FILE_TYPES
