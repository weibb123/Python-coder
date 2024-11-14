from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
from models import QueryInput, QueryResponse
from services import PythonCodeService

# configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIHandler:
    def __init__(self):
        self.service = PythonCodeService()

    
    # we specify these datatypes for the inputs
    async def query_handler(self, input_data: QueryInput) -> QueryResponse:
        """Handle AI query requests."""
        try:
            result = await self.service.process_query(
                query=input_data.query,
                temperature=input_data.temperature
            )
            return QueryResponse(**result)
        except Exception as e:
            logger.error(f"Error in query handler: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))
    
# Initialize FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"testing": "World"}

@app.get("/ok")
async def ok_endpoint():
    return {"message": "ok"}

# Initialize AI service
ai_service = PythonCodeService()

@app.post("/query", response_model=QueryResponse)
async def query_handler(input_data: QueryInput):
    """Handle AI query requests."""
    try:
        result = await ai_service.process_query(
            query=input_data.query
        )
        return QueryResponse(**result)
    except Exception as e:
        logger.error(f"Error in query handler: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
        """Handle health check requests."""
        return {"status": 200, "service": "AI Python Coder"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8080,
                reload=True)






