from langchain_community.document_loaders import DirectoryLoader, PyPDFium2Loader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

PASTA_BASE = "base"

def criar_db():
    documentos = carregar_documentos()
    if documentos:
        chunks = dividir_chunks(documentos)
        vetorizar_chunks(chunks)
    else:
        print("Nenhum documento carregado.")

def carregar_documentos():
    carregador = DirectoryLoader(
        PASTA_BASE, 
        glob="*.pdf", 
        loader_cls=PyPDFium2Loader
    )
    documentos = carregador.load()
    return documentos

def dividir_chunks(documentos):
    separador_documentos = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True
    )
    chunks = separador_documentos.split_documents(documentos)
    print(f"Chunks gerados: {len(chunks)}")
    return chunks

def vetorizar_chunks(chunks):
    db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory="db")
    print("Banco de Dados criado")

if __name__ == "__main__":
    criar_db()