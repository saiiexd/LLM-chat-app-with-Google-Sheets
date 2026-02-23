import sys
import os

# Add root directory to sys.path to allow importing services
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Dict, Optional
from services.llm_service import llm_service
from services.sheets_service import sheets_service

app = FastAPI(title="AI Chat App")

# Enable CORS for frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Minimal session-based memory (In-memory for simplicity as per requirements)
# In production, this would be Redis or a database
sessions: Dict[str, List[Dict[str, str]]] = {}

class ChatRequest(BaseModel):
    message: str
    first_name: Optional[str] = "Anonymous"
    last_name: Optional[str] = ""
    email: Optional[str] = "N/A"

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    user_input = request.message

    # Generate response from LLM
    success, llm_response = llm_service.generate_response(user_input, [])

    if not success:
        raise HTTPException(status_code=500, detail=llm_response)

    # Log to Google Sheets with user info
    try:
        sheets_service.log_chat(
            request.first_name, 
            request.last_name, 
            request.email, 
            user_input, 
            llm_response
        )
    except Exception as e:
        print(f"Failed to log to sheets: {e}")

    return ChatResponse(response=llm_response)

@app.get("/health")
async def health():
    return {"status": "healthy"}

# Mount the frontend directory to serve static files
# Note: This is useful if running everything under one process
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
