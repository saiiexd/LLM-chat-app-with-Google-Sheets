import os
import gspread
from datetime import datetime
from typing import List
from dotenv import load_dotenv

load_dotenv()

# Google Sheets Config
CREDENTIALS_FILE = "llm-chat-app-485016-5a0ee183737c.json"
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
CHAT_HISTORY_SHEET = "ChatHistory"
HEADERS = ["Timestamp", "First Name", "Last Name", "Email", "User Query", "LLM Response"]

class SheetsService:
    def __init__(self):
        self.client = None
        self.spreadsheet = None
        self.worksheet = None
        self._initialized = False

    def _initialize(self):
        """Lazy initialization of Google Sheets client"""
        if self._initialized:
            return True
        
        try:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"Warning: {CREDENTIALS_FILE} not found. Sheets integration disabled.")
                return False
            
            if not SPREADSHEET_ID:
                print("Warning: SPREADSHEET_ID not set. Sheets integration disabled.")
                return False

            self.client = gspread.service_account(filename=CREDENTIALS_FILE)
            self.spreadsheet = self.client.open_by_key(SPREADSHEET_ID)
            
            # Use the first worksheet (Sheet1) for better visibility
            self.worksheet = self.spreadsheet.get_worksheet(0)
            
            # Ensure headers
            try:
                first_row = self.worksheet.row_values(1)
                if not first_row or first_row != HEADERS:
                    self.worksheet.insert_row(HEADERS, 1)
            except:
                self.worksheet.append_row(HEADERS)
            
            self._initialized = True
            return True
        except Exception as e:
            print(f"Error initializing SheetsService: {e}")
            return False

    def log_chat(self, first_name: str, last_name: str, email: str, query: str, response: str):
        """Asynchronously log chat history including user details"""
        if not self._initialize():
            return False
        
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.worksheet.append_row([timestamp, first_name, last_name, email, query, response])
            return True
        except Exception as e:
            print(f"Error logging chat to sheets: {e}")
            return False

sheets_service = SheetsService()
