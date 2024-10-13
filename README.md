# IngreCheck: OCR and AI-Powered Dietary Analyzer

**IngreCheck** is a Python project that uses OCR (Optical Character Recognition) and AI to analyze product ingredient lists for dietary compliance. The project exposes two APIs: one for open-source OCR using Tesseract, and another for Google Vision. It also includes a dietary analyzer using LangChain to process dietary restrictions.


## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/IngreCheck.git
   cd IngreCheck
   ```
2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up API Keys**:
    - Add your OpenAI API key and Google Vision API credentials in `config/config.yaml` and `config/credentials.json`.

5. **Run the FastAPI application**:
    ```bash
    uvicorn src.main:app --reload
    ```


## Testing the Process Images API

To test the **Process Images** endpoint, which processes an image for OCR and checks dietary compliance, you can use the following `curl` command:

```bash
curl -X GET "http://127.0.0.1:8000/process_images?confirm=yes"
```
