import pytest
from src.dietary_analyzer import DietaryAnalyzer
from unittest.mock import patch

# Test the setup and loading of PDFs
@patch("src.dietary_analyzer.dietary_analyzer.PyPDFLoader")
@patch("src.dietary_analyzer.dietary_analyzer.OpenAIEmbeddings")
@patch("src.dietary_analyzer.dietary_analyzer.FAISS")
def test_dietary_analyzer_setup(mock_faiss, mock_embeddings, mock_pdf_loader):
    mock_pdf_loader.return_value.load.return_value = ["Sample document text"]  # Mocked PDF content
    mock_faiss.from_documents.return_value.as_retriever.return_value = "Mocked Retriever"
    
    analyzer = DietaryAnalyzer(restrictions_folder="data/dietary_restrictions/pdfs")
    assert analyzer.retriever == "Mocked Retriever"

# Test dietary analysis with mocked retrieval and LLM
@patch("src.dietary_analyzer.dietary_analyzer.OpenAI")
@patch("src.dietary_analyzer.dietary_analyzer.RetrievalQA")
def test_analyze_ingredients(mock_qa_chain, mock_llm):
    # Mock the QA chain response
    mock_qa_chain.return_value.run.return_value = "Mocked compliance result"
    
    analyzer = DietaryAnalyzer(restrictions_folder="data/dietary_restrictions/pdfs")
    result = analyzer.analyze_ingredients("Wheat flour, Peanut oil")
    
    assert result == "Mocked compliance result"
