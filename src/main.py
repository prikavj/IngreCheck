from fastapi import FastAPI, HTTPException
from src.api import ocr_router, analyzer_router
from src.ocr import OCRService
from src.dietary_analyzer import DietaryAnalyzer
import os

app = FastAPI()

# Include OCR API and Analyzer API routes
app.include_router(ocr_router)
app.include_router(analyzer_router)

# Initialize OCR service and dietary analyzer
ocr_service = OCRService(google_credentials_path="config/credentials.json")
dietary_analyzer = DietaryAnalyzer(restrictions_folder="data/dietary_restrictions/pdfs")

# Helper function to read image file as bytes
def read_image_file_as_bytes(file_path):
    with open(file_path, "rb") as image_file:
        return image_file.read()

# Main route to prompt the user for confirmation and process images
@app.get("/process_images")
async def process_images(confirm: str):
    """
    Route to ask the user to confirm image processing and dietary compliance check.
    :param confirm: User confirmation ('yes' to proceed)
    :return: Dietary compliance results
    """
    if confirm.lower() != "yes":
        return {"message": "Image processing canceled."}

    # Read all images from the data/images/ folder
    image_folder = "data/images/test"
    images = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    if not images:
        raise HTTPException(status_code=404, detail="No images found in the data/images/ folder.")
    
    result_summary = []

    for image_file in images:
        image_path = os.path.join(image_folder, image_file)
        image_bytes = read_image_file_as_bytes(image_path)

        # Perform OCR (you can toggle between Google and Tesseract as needed)
        detected_text = ocr_service.perform_google_ocr(image_bytes)
        # For Tesseract, uncomment the line below:
        # detected_text = ocr_service.perform_tesseract_ocr(image_bytes)

        # Analyze dietary compliance
        compliance_result = dietary_analyzer.analyze_ingredients(detected_text)

        # Append the result to the summary
        result_summary.append({
            "image": image_file,
            "detected_text": detected_text,
            "compliance_result": compliance_result
        })

    return {"message": "Image processing completed.", "results": result_summary}

# Add root route
@app.get("/")
def read_root():
    return {"message": "Welcome to IngreCheck OCR and Dietary Analyzer API"}
