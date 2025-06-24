from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from pathlib import Path

# these three lines swap the stdlib sqlite3 lib with the pysqlite3 package
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# need to import Chroma AFTER sqlite swap
from langchain_community.vectorstores import Chroma

embeddings_model = OpenAIEmbeddings()
llm = ChatOpenAI(model_name= "gpt-3.5-turbo", max_tokens= 500)
pdf_link = "os-sertoes.pdf"

def getDataRetriever():
    loader = PyPDFLoader(Path(__file__).parent / pdf_link, extract_images=False)
    pages = loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 4000, # each chunk will have 4000 characters
        chunk_overlap = 20, # they will have an overlap of 20 characters so we do not lose much content at the end of a given chunk
        length_function = len,
        add_start_index = True
    )
    chunks = text_splitter.split_documents(pages)
    vectordb = Chroma.from_documents(chunks, embedding=embeddings_model, persist_directory="vectordb_simple")

    # Load Retriever - search for relevant chunks (k:3 => top 3 relevant chunks)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    return retriever

def getRelevantDocs(question):
    retriever = getDataRetriever()
    relevantDocs = retriever.invoke(question)
    return relevantDocs

def sendSimpleRagPrompt(question):
    TEMPLATE = """
        Utilize o contexto abaixo para responder a pergunta:
        Contexto: {context}
        Pergunta: {question}
    """
    prompt = PromptTemplate(input_variables = ['context', 'question'], template=TEMPLATE)
    sequence = RunnableSequence(prompt | llm)
    context = getRelevantDocs(question)
    response = sequence.invoke({ 'context': context, 'question': question })
    return response
