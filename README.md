# 🤖 Premium AI Chat Assistant (FastAPI + Groq + Google Sheets)

A professional full-stack AI chat application featuring a mandatory registration portal, high-speed LLM inference via **Groq**, and automated conversation logging to **Google Sheets**.

---

## 🌟 Key Features
- **Mandatory Login**: Cinematic entrance portal capturing Name and Email before chat begins.
- **Blazing Fast AI**: Integrated with **Groq (Llama 3.3)** for near-instant responses.
- **Persistent Logging**: Every interaction is logged to a Google Spreadsheet with user metadata.
- **Premium Dark UI**: Modern, responsive interface with smooth animations and typing indicators.
- **Resilient Backend**: FastAPI-powered architecture with structured service layers.

---

## 🏗️ Project Structure
```text
├── backend/
│   └── main.py          # FastAPI server & endpoints
├── frontend/
│   ├── index.html       # UI Structure & Login Modal
│   ├── style.css        # Premium Styling
│   └── script.js        # Frontend Logic & API calls
├── services/
│   ├── llm_service.py   # Groq API Integration (Llama 3.3)
│   └── sheets_service.py# Google Sheets API Logic
├── .env                 # API Keys & Configuration
├── run.py               # Main entry point to start the app
└── requirements.txt      # Python dependencies
```

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8+
- A Google Cloud Service Account JSON file.
- A Groq API Key.

### 2. Environment Setup
Configure your `.env` file with the following:
```env
GROQ_API_KEY=your_groq_key_here
SPREADSHEET_ID=your_google_sheet_id_here
```

### 3. Google Sheets Configuration
1. Create a Google Sheet.
2. Shared the sheet with the `client_email` found in your `credentials.json` (as an **Editor**).
3. Ensure the filename of your credentials matches the `CREDENTIALS_FILE` variable in `services/sheets_service.py`.

### 4. Installation & Launch
```bash
# Install dependencies
pip install -r requirements.txt

# Start the application
python run.py
```
Open your browser to: **`http://localhost:8000`**

---

## 🛠️ Developer Guide (How to Customize)

### How to add new columns to Google Sheets?
If you want to capture more info (e.g., "Company Name"), follow these steps:

1. **Update `services/sheets_service.py`**:
   - Locate the `HEADERS` list and add your new column name.
   - Update `log_chat(...)` to accept the new parameter and add it to the `append_row` list.

2. **Update `backend/main.py`**:
   - Update the `ChatRequest` class (Pydantic model) to include the new field.
   - Update the `chat()` function to pass the new field from the request to `sheets_service.log_chat()`.

3. **Update `frontend/index.html`**:
   - Add a new `<input>` field inside the `#login-form`.

4. **Update `frontend/script.js`**:
   - Capture the new input value in the `loginForm` submit listener.
   - Include the new value in the `body` of the `fetch` request inside `sendMessage()`.

### How to change the AI Model?
Edit `services/llm_service.py` and change the `GROQ_MODEL` variable. 
*Example: `llama-3.1-8b-instant` or `llama3-70b-8192`.*

---

## 🔒 Security Note
Never commit your `.env` file or `credentials.json` to version control (like GitHub). They contain sensitive API keys.
