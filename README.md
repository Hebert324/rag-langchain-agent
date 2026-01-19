# Projeto RAG (Retrieval-Augmented Generation) com LangChain

Este projeto é um Agente de IA capaz de ler documentos PDF, criar um banco de dados vetorial e responder perguntas com base exclusivamente no conteúdo desses documentos. Ele utiliza Python, LangChain, ChromaDB e a API da OpenAI.

## 📋 Pré-requisitos

* Python 3.11+
* Chave de API da OpenAI

## 🚀 Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Hebert324/rag-langchain-agent.git](https://github.com/Hebert324/rag-langchain-agent.git)
    cd rag-langchain-agent
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv .venv
    .\.venv\Scripts\Activate

    # Linux/Mac
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install langchain langchain-openai langchain-community langchain-chroma chromadb openai python-dotenv pypdfium2
    ```

## ⚙️ Configuração

1.  Crie um arquivo chamado `.env` na raiz do projeto.
2.  Adicione sua chave da OpenAI neste arquivo:
    ```env
    OPENAI_API_KEY=sua-chave-aqui
    ```

## 📂 Estrutura do Projeto

* `base/`: Pasta onde você deve colocar os arquivos PDF que a IA deve ler.
* `db/`: Pasta gerada automaticamente onde o banco de dados vetorial (Chroma) será salvo.
* `criar_db.py`: Script que lê os PDFs da pasta `base` e cria o banco de dados.
* `main.py`: Script principal que carrega o banco e permite fazer perguntas.

## ▶️ Como Usar

1.  **Adicione seus documentos:**
    Coloque os arquivos `.pdf` que você quer que a IA aprenda dentro da pasta `base`.

2.  **Crie o Banco de Dados:**
    Execute o script para processar os arquivos e gerar os vetores:
    ```bash
    python criar_db.py
    ```
    *Você verá a mensagem: "Banco de Dados criado".*

3.  **Faça Perguntas:**
    Execute o agente para iniciar a interação:
    ```bash
    python main.py
    ```
    Digite sua pergunta no terminal e aguarde a resposta baseada nos seus PDFs.

## 🛠 Tecnologias Utilizadas

* [LangChain](https://www.langchain.com/) - Framework para LLMs
* [ChromaDB](https://www.trychroma.com/) - Banco de dados vetorial
* [OpenAI](https://openai.com/) - Modelos de Embedding e Chat (GPT)
* [PyPDFium2](https://pypi.org/project/pypdfium2/) - Leitor de PDF otimizado

---
Desenvolvido por Hebert Almeida.