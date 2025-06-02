import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI

OPENAI_API_KEY = ""

#upload PDF
st.header("AB First ChatBot")
with st.sidebar:
    st.title("Your Docucments")
    file = st.file_uploader("Upload a PDF file and start asking questions", type ="pdf")

# Extract the text from file
if file is not None:
    pdf_Reader = PdfReader(file)
    text = ""
    for page in pdf_Reader.pages:
        text+=page.extract_text()
    #st.write(text)
# Break into chuncks
    text_splitter = RecursiveCharacterTextSplitter(
        separators = "\n",
        chunk_size = 1000,
        chunk_overlap = 150,
        length_function = len
    )
    chuncks=text_splitter.split_text(text)
    #st.write(chuncks)
#Generate Embedding
    embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

#Create Vecor store
    vector_store = FAISS.from_texts(chuncks,embedding)

#Get User Quwstions
    user_question = st.text_input("Type your question")

#Perfrom Simalrity Search
    if user_question:
        match = vector_store.similarity_search(user_question)
        #st.write(match)
# Define llm
        llm=ChatOpenAI(
           openai_api_key = OPENAI_API_KEY,
           temperature = 0,
           max_tokens=1000,
           model_name = "gpt-3.5-turbo"
        )
#Output results
        chain = load_qa_chain(llm, "stuff")
        response = chain.run(input_documents = match,  question = user_question)
        st.write(response)