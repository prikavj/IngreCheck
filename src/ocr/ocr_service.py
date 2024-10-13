import os
from google.cloud import vision
import pytesseract
from PIL import Image
import io

class OCRService:
    def __init__(self, google_credentials_path=None):
        if google_credentials_path:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = google_credentials_path
            self.google_client = vision.ImageAnnotatorClient()
        else:
            self.google_client = None

    def perform_google_ocr(self, image_bytes):
        """
        Perform OCR using Google Vision API.
        :param image_bytes: Image file in bytes
        :return: Detected text
        """
        if not self.google_client:
            raise RuntimeError("Google Vision credentials not set up.")

        image = vision.Image(content=image_bytes)
        response = self.google_client.text_detection(image=image)
        texts = response.text_annotations

        if len(texts) > 0:
            return texts[0].description
        else:
            return "No text detected by Google Vision."

    def perform_tesseract_ocr(self, image_bytes):
        """
        Perform OCR using Tesseract (Open Source).
        :param image_bytes: Image file in bytes
        :return: Detected text
        """
        image = Image.open(io.BytesIO(image_bytes))
        detected_text = pytesseract.image_to_string(image)
        return detected_text
