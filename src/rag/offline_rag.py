import re
from langchain import hub
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class Str_StrOutputParser(StrOutputParser):
    def __init__(self) -> None:
        super().__init__()

    def parse(self, text:str)-> str:
        return self.extract_answer(text)
    
    def extract_answer(self, text_response:str, pattern: str=r"Answer:\s*(.*)") -> str:
        match = re.search(pattern, text_response, re.DOTALL)
        if match:
            anwser_text = match.group(1).strip()
            return anwser_text
        else:
            return text_response
    
class Offline_RAG:
    def __init__(self, llm) -> None:
        self.llm = llm
        self.prompt = hub.pull("rlm/rag-prompt")
        self.str_parser = Str_StrOutputParser()
    def get_chain(self, retriever):
        input_data = {
            "context" : retriever | self.__format__docs,
            "question" : RunnablePassthrough()
        }
        rag_chain = (
            input_data
            | self.prompt
            | self.llm
            | self.str_parser
        )
        return rag_chain
    
    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)