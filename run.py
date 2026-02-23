import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print("--- Starting AI Chat Application ---")
    print("Backend: http://localhost:8000")
    print("Frontend: http://localhost:8000")
    print("-------------------------------------")
    
    # Run uvicorn from the root directory so imports work correctly
    # Point to backend.main:app
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
