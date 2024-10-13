import os
import yaml
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

class DietaryAnalyzer:
    def __init__(self, restrictions_folder):
        self.restrictions_folder = restrictions_folder
        self.retriever = None
        self._setup()

    def _load_config(self):
        """Loads the configuration file."""
        with open("config/config.yaml", "r") as f:
            config = yaml.safe_load(f)
        return config

    def _setup(self):
        """Loads PDFs, creates document embeddings, and sets up retriever."""
        # Load config
        config = self._load_config()
        openai_api_key = config['openai']['api_key']

        # Load all PDFs
        pdf_files = [f for f in os.listdir(self.restrictions_folder) if f.endswith('.pdf')]
        documents = []
        for pdf in pdf_files:
            pdf_path = os.path.join(self.restrictions_folder, pdf)
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())

        # Use OpenAI embeddings with the API key from the config file
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

        # Create FAISS vector store with document embeddings
        vector_store = FAISS.from_documents(documents, embeddings)
        self.retriever = vector_store.as_retriever()

    def analyze_ingredients(self, ingredients_text):
        """
        Given a string of ingredients (from OCR), check compliance against the dietary restrictions.
        :param ingredients_text: Extracted text of ingredients from the OCR service
        :return: Resulting dietary compliance information
        """
        if not self.retriever:
            raise RuntimeError("The retriever is not set up. Ensure the PDFs are loaded properly.")

        # Load config to get the OpenAI API key
        config = self._load_config()
        openai_api_key = config['openai']['api_key']

        # Set up a chat-based LLM with the API key (use ChatOpenAI for gpt-3.5-turbo)
        llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)

        # Create a ConversationalRetrievalChain with the retriever and LLM
        qa_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=self.retriever)

        # Build a prompt that considers both the dietary restrictions and ingredients
        question = f"""
        You are an expert in dietary compliance. Given the following list of ingredients, 
        check whether these ingredients comply with the dietary restrictions mentioned in the provided documents.

        Ingredients:
        {ingredients_text}

        Based on the dietary restriction documents retrieved, check if the ingredients are safe to consume. 
        If not, explain why and specify which ingredients are problematic.
        """

        # Provide an empty chat history if none exists
        chat_history = []

        # Query the retriever using the OCR-extracted ingredients text with the question
        result = qa_chain({"question": question, "chat_history": chat_history})
        return result
