from fastapi import APIRouter, HTTPException
from src.dietary_analyzer.dietary_analyzer import DietaryAnalyzer

# Initialize the dietary analyzer
dietary_analyzer = DietaryAnalyzer(restrictions_folder="data/dietary_restrictions/pdfs")

# Define the API router
router = APIRouter()

@router.post("/analyze")
async def analyze_ingredients(ingredients_text: str):
    """
    Endpoint to analyze the ingredients and check dietary compliance.
    :param ingredients_text: The extracted ingredients list as a string
    :return: Dietary compliance results
    """
    try:
        # Perform dietary analysis using the ingredients list
        result = dietary_analyzer.analyze_ingredients(ingredients_text)
        return {"compliance_result": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
