"""Constants for the application."""

SUPPORTED_FILE_TYPES = [".pdf", ".jpg", ".jpeg", ".png"]

LABEL_BANK_STATEMENT="bank-statement"
LABEL_INVOICE="invoice"
LABEL_DRIVER_LICENSE="drivers-license"
LABEL_OTHER="other"

ALLOWED_LABELS = {
  "bank-statement": LABEL_BANK_STATEMENT,
  "invoice": LABEL_INVOICE,
  "drivers-license": LABEL_DRIVER_LICENSE,
  "other": LABEL_OTHER
}

TRAINING_FILES = {
  "bank_statement_1.pdf": LABEL_BANK_STATEMENT,
  "bank_statement_2.pdf": LABEL_BANK_STATEMENT,
  "bank_statement_3.pdf": LABEL_BANK_STATEMENT,
  "drivers_license_1.jpg": LABEL_DRIVER_LICENSE,
  "drivers_license_2.jpg": LABEL_DRIVER_LICENSE,
  "drivers_license_3.jpg": LABEL_DRIVER_LICENSE,
  "invoice_1.pdf": LABEL_INVOICE,
  "invoice_2.pdf": LABEL_INVOICE,
  "invoice_3.pdf": LABEL_INVOICE,
}
