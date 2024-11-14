# services.py
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class PythonCodeService:
    def __init__(self, model_name: str="hf.co/weibb/model:Q4_K_M"):
        self.model_name = model_name
        self._llm = None
        self._prompt = None
        self._chain = None
        self.setup_chain()
    
    def setup_chain(self) -> None:
        """Initialize the language model and prompt template
        using Langchain"""
        try:
            self._llm = ChatOllama(
                model=self.model_name,
                temperature=0
            )

            self._prompt = ChatPromptTemplate.from_messages([
                (
                    "system",
                    "You are a senior Python developer. Maintain a clear code and good explanation"

                ),
                ("human", "{input}")
            ])

            self._chain = self._prompt | self._llm
        except Exception as e:
            logger.error(f"Error setting up AI chain: {str(e)}")
            raise
    
    async def process_query(self, query: str) -> Dict[str, Any]:
        """Process a query and return the response."""
        try:
            response = self._chain.invoke({"input": query})
            return {
                "response": response.content,
                "model_used": self.model_name
            }
        
        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            raise