from pprint import pprint

from langchain.chains import ConversationalRetrievalChain
from langchain.memory.buffer import ConversationBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WikipediaLoader
from langchain_community.vectorstores import Chroma
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings


def get_wiki_docs(query: str, lang: str = "ja"):
    loader = WikipediaLoader(query, lang=lang, load_max_docs=1, doc_content_chars_max=1000000)
    return loader.load()


def main():
    documents = []
    documents.extend(get_wiki_docs("徳川家光"))
    documents.extend(get_wiki_docs("徳川家宣"))
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(texts, embeddings)

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key='answer'
    )

    qa = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(model="gpt-4-1106-preview"),
        vectordb.as_retriever(search_kwargs={"k": 5}),
        memory=memory,
        return_source_documents=True
    )

    def custom_qa_loop():
        while True:  # 無限ループでユーザーからの入力を待ち受けます
            user_input = input("質問を入力してください（終了するには'exit()'と入力）: ")
            if user_input.lower() == 'exit()':  # ユーザーが終了を望んだ場合
                break  # ループを抜けます
            else:
                response = qa.invoke({"question": user_input})  # qa.invokeメソッドを使って質問に回答します
                pprint(response)  # 回答を出力します

    custom_qa_loop()

