import pytest
from src.ocr import OCRService
from unittest.mock import patch

# Helper function to read image file as bytes
def read_image_file_as_bytes(file_path):
    with open(file_path, "rb") as image_file:
        return image_file.read()

# Test OCRService with Tesseract using a real image file
def test_tesseract_ocr():
    ocr_service = OCRService()  # No Google credentials needed for Tesseract

    # Path to a sample image
    image_path = "data/images/test/image_1.jpg"
    
    # Read the image as bytes
    image_bytes = read_image_file_as_bytes(image_path)

    # Mock the Tesseract OCR result
    with patch("pytesseract.image_to_string") as mock_tesseract:
        mock_tesseract.return_value = "Sample OCR text"
        
        # Perform Tesseract OCR and verify the result
        result = ocr_service.perform_tesseract_ocr(image_bytes)
        assert result == "Sample OCR text"

# Test OCRService with Google Vision (mocked), using a real image file
@patch("src.ocr.ocr_service.vision.ImageAnnotatorClient")
def test_google_ocr(mock_vision_client):
    ocr_service = OCRService(google_credentials_path="config/credentials.json")
    
    # Path to a sample image
    image_path = "data/images/test/image_1.jpg"

    # Read the image as bytes
    image_bytes = read_image_file_as_bytes(image_path)

    # Mock the Google Vision API response
    mock_client_instance = mock_vision_client.return_value
    mock_client_instance.text_detection.return_value.text_annotations = [{"description": "Sample Google OCR text"}]
    
    # Perform Google OCR and verify the result
    result = ocr_service.perform_google_ocr(image_bytes)
    assert result == "Sample Google OCR text"
