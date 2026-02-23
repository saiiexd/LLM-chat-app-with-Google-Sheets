import os
import requests
import json
from typing import Tuple, List, Dict
from dotenv import load_dotenv

# Load keys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(base_dir, '.env'))

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# Using Llama 3.3 for high performance and current availability
GROQ_MODEL = "llama-3.3-70b-versatile"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

class LLMService:
    """
    Groq LLM Service.
    Uses the provided Groq API key for high-speed inference.
    """

    def __init__(self):
        if not GROQ_API_KEY:
            print("Warning: GROQ_API_KEY not found in .env")

    def generate_response(self, user_input: str, history: List[Dict[str, str]] = None) -> Tuple[bool, str]:
        """
        Generates a response using Groq API.
        """
        if not GROQ_API_KEY:
            return False, "Error: Groq API key is missing. Please check your .env file."

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        # Prepare content for Groq (OpenAI Compatible)
        payload = {
            "model": GROQ_MODEL,
            "messages": [
                {"role": "system", "content": "You are a helpful and clear AI assistant."},
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.7,
            "max_tokens": 1024
        }

        try:
            response = requests.post(
                GROQ_API_URL,
                headers=headers,
                json=payload,
                timeout=20
            )
            
            if response.status_code == 200:
                data = response.json()
                try:
                    text = data["choices"][0]["message"]["content"]
                    return True, text.strip()
                except (KeyError, IndexError):
                    return False, "Error: Unexpected response format from Groq."
            
            elif response.status_code == 429:
                return False, "Error: Groq rate limit exceeded. Please wait a moment."
            else:
                return False, f"Error: Groq API returned status {response.status_code}. {response.text}"
                
        except Exception as e:
            return False, f"Error connecting to Groq: {str(e)}"

llm_service = LLMService()
