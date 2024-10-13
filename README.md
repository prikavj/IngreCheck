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

## Sample output

```bash
➜  IngreCheck source venv/bin/activate     
(venv) ➜  IngreCheck uvicorn src.main:app --reload
INFO:     Will watch for changes in these directories: ['/Users/priyankavijeet/Desktop/Projects/IngreCheck']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [63906] using StatReload
INFO:     Started server process [63908]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
/Users/priyankavijeet/Desktop/Projects/IngreCheck/src/dietary_analyzer/dietary_analyzer.py:77: LangChainDeprecationWarning: The method `Chain.__call__` was deprecated in langchain 0.1.0 and will be removed in 1.0. Use :meth:`~invoke` instead.
  result = qa_chain({"question": question, "chat_history": chat_history})
INFO:     127.0.0.1:57338 - "GET /process_images?confirm=yes HTTP/1.1" 200 OK
```
```bash
➜  IngreCheck source /Users/priyankavijeet/Desktop/Projects/IngreCheck/venv/bin/activate
(venv) ➜  IngreCheck curl -X GET "http://127.0.0.1:8000/process_images?confirm=yes"
{"message":"Image processing completed.","results":[{"image":"image_1.jpg","detected_text":"VOTRE PEAU LES SOINS ATTENTIFS QU'ELLE MERITE!\nINGREDIENTS/INGRÉDIENTS : AQUA, GLYCERIN, STEARIC ACID, GLYCOL STEARATE, ISOPROPYL\nPALMITATE, GLYCINE SOJA (SOYBEAN) OIL, GLYCERYL STEARATE, TRIETHANOLAMINE, COCOS NUCIFERA\n(COCONUT) OIL, CETYL ALCOHOL, CAPRYLYL GLYCOL, PHENOXYETHANOL, CARBOMER, HYDROXYETHYLCELLULOSE,\nPARFUM, STEARAMIDE AMP, DISODIUM EDTA, BHT, HYDROLYZED ELÁSTIN, HYDROLYZED COLLAGEN, BENZYL\nALCOHOL, BENZYL SALICYLATE, COUMARIN, HEXYL CINNAMAL,\nLIMONENE AND LINALOOL\n8","compliance_result":{"question":"\n        You are an expert in dietary compliance. Given the following list of ingredients, \n        check whether these ingredients comply with the dietary restrictions mentioned in the provided documents.\n\n        Ingredients:\n        VOTRE PEAU LES SOINS ATTENTIFS QU'ELLE MERITE!\nINGREDIENTS/INGRÉDIENTS : AQUA, GLYCERIN, STEARIC ACID, GLYCOL STEARATE, ISOPROPYL\nPALMITATE, GLYCINE SOJA (SOYBEAN) OIL, GLYCERYL STEARATE, TRIETHANOLAMINE, COCOS NUCIFERA\n(COCONUT) OIL, CETYL ALCOHOL, CAPRYLYL GLYCOL, PHENOXYETHANOL, CARBOMER, HYDROXYETHYLCELLULOSE,\nPARFUM, STEARAMIDE AMP, DISODIUM EDTA, BHT, HYDROLYZED ELÁSTIN, HYDROLYZED COLLAGEN, BENZYL\nALCOHOL, BENZYL SALICYLATE, COUMARIN, HEXYL CINNAMAL,\nLIMONENE AND LINALOOL\n8\n\n        Based on the dietary restriction documents retrieved, check if the ingredients are safe to consume. \n        If not, explain why and specify which ingredients are problematic.\n        ","chat_history":[],"answer":"Based on the provided dietary restrictions, the following ingredients in the list are not compliant:\n\n1. Glycine Soja (Soybean) Oil - Individuals with a soy allergy should avoid this ingredient.\n2. Cocos Nucifera (Coconut) Oil - Individuals allergic to coconut should avoid this ingredient.\n3. Parfum - Individuals sensitive to perfumes or fragrances should avoid this ingredient.\n4. Benzyl Salicylate - A fragrance compound to be avoided by those sensitive to fragrances.\n5. Coumarin - Another fragrance compound to be avoided by fragrance-sensitive individuals.\n6. Limonene - A fragrance compound that should be avoided by those with perfume sensitivity.\n7. Linalool - A fragrance compound to steer clear of for individuals sensitive to fragrances.\n\nTherefore, the product contains ingredients that are not suitable for individuals with soy allergies, coconut allergies, or perfume sensitivity."}}]}%                                                                                                                                                    
(venv) ➜  IngreCheck
```

