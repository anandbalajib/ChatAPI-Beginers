anandbalajib: generate a Readme for this repo

Workspace: Collecting workspace informationFiltering to most relevant information# AB First ChatBot

A simple Streamlit-based chatbot that allows you to upload a PDF document and ask questions about its content using OpenAI's GPT models and vector search.

## Features

- Upload a PDF file via the web interface
- Extracts and chunks text from the PDF
- Generates embeddings using OpenAI Embeddings
- Stores document chunks in a FAISS vector store for efficient similarity search
- Uses OpenAI's GPT-3.5-turbo (via LangChain) to answer user questions based on the PDF content

## Requirements

- Python 3.9+
- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypdf2.readthedocs.io/)
- [langchain](https://python.langchain.com/)
- [openai](https://pypi.org/project/openai/)
- [faiss-cpu](https://github.com/facebookresearch/faiss) (or faiss-gpu)

## Setup

1. **Clone the repository:**
    ```sh
    git clone <repo-url>
    cd <repo-directory>
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set your OpenAI API key:**
    - The API key is currently hardcoded in chatBot.py. For production, use environment variables or Streamlit secrets.

## Usage

1. **Run the Streamlit app:**
    ```sh
    streamlit run code/chatBot.py
    ```

2. **In your browser:**
    - Upload a PDF file using the sidebar.
    - Type your question in the input box.
    - The chatbot will answer based on the PDF content.

## File Structure

- chatBot.py — Main Streamlit application.
- `requirements.txt` — Python dependencies (create this if missing).

## Notes

- This project uses OpenAI's GPT-3.5-turbo via LangChain's `ChatOpenAI`.
- The PDF is processed using PyPDF2.
- Text is chunked and embedded for semantic search using FAISS.

## License

MIT License

---

**Disclaimer:** This project is for educational/demo purposes. Do not expose your OpenAI API key in production code.

---

**Main file:** chatBot.py
