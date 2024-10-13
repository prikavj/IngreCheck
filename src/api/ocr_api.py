from fastapi import APIRouter, UploadFile, File, HTTPException
from src.ocr import OCRService

import os

# Initialize OCR service
config_path = "config/config.yaml"

ocr_service = OCRService(google_credentials_path="config/credentials.json")

# Define the API router
router = APIRouter()

@router.post("/ocr/google")
async def google_ocr(file: UploadFile = File(...)):
    """
    Endpoint to perform OCR using Google Vision.
    """
    try:
        # Read image file
        image_data = await file.read()
        
        # Perform OCR using Google Vision
        detected_text = ocr_service.perform_google_ocr(image_data)
        return {"ocr_engine": "Google Vision", "text": detected_text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ocr/tesseract")
async def tesseract_ocr(file: UploadFile = File(...)):
    """
    Endpoint to perform OCR using Tesseract.
    """
    try:
        # Read image file
        image_data = await file.read()

        # Perform OCR using Tesseract
        detected_text = ocr_service.perform_tesseract_ocr(image_data)
        return {"ocr_engine": "Tesseract", "text": detected_text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
