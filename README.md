# AI Chat Application with Google Sheets Integration

A full-stack Python application that integrates a Large Language Model (LLM) with a FastAPI backend and uses Google Sheets for logging interactions. This project demonstrates a production-ready architecture for building AI-powered tools with persistent storage.

## Project Overview

This application provides a chat interface where users can interact with an AI model (powered by Groq). Every conversation, along with user metadata, is automatically logged into a specified Google Spreadsheet for record-keeping and analysis.

## Core Features

- **FastAPI Backend**: Robust and high-performance API handling.
- **LLM Integration**: High-speed inference using Groq's Llama-3 API.
- **Google Sheets Storage**: Automated data logging using Google Sheets as a database.
- **Responsive Frontend**: Clean and modern user interface built with vanilla JavaScript and CSS.
- **Environment Management**: Secure handling of API keys and credentials.

## Technology Stack

- **Backend**: Python, FastAPI
- **Frontend**: HTML5, CSS3, JavaScript
- **API Services**: Groq (LLM), Google Sheets API v4
- **Libraries**: `uvicorn`, `gspread`, `google-auth`, `pydantic`, `python-dotenv`

## Prerequisites

Before setting up the project, ensure you have the following:

- Python 3.8 or higher installed on your system.
- A GitHub account to clone the repository.
- A Groq API Key (obtainable from [Groq Console](https://console.groq.com/)).
- A Google Cloud Project with the Google Sheets API enabled.

## Installation Guide

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

Open your terminal or command prompt and run the following commands:

```bash
git clone https://github.com/saiiexd/LLM-chat-app-with-Google-Sheets.git
cd LLM-chat-app-with-Google-Sheets
```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies:

```bash
# Create venv
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Activate venv (Linux/macOS)
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Configuration and API Keys

This application requires specific API keys and credentials to function. **Without these, the application will fail to start or interact with AI and storage services.**

### 1. Environment Variables

Create a file named `.env` in the root directory and add the following configurations:

```env
GROQ_API_KEY=your_groq_api_key_here
SPREADSHEET_ID=your_google_spreadsheet_id_here
```

- **GROQ_API_KEY**: Replace with your actual key from the Groq console.
- **SPREADSHEET_ID**: Found in the URL of your Google Sheet: `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit`.

### 2. Google Cloud Service Account

To enable Google Sheets integration:

1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Enable the **Google Sheets API**.
3.  Create a **Service Account** and download the JSON key file.
4.  Rename the downloaded file to `credentials.json` and place it in the root directory.
5.  **Critical Step**: Open the `credentials.json` file, find the `client_email`, and share your Google Spreadsheet with this email address (Editor access).

## Running the Application

Once the configuration is complete, you can start the application using the provided entry point:

```bash
python run.py
```

The application will be available at:
- **Frontend**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Project Structure

- `backend/`: Contains the FastAPI application and route definitions.
- `frontend/`: Static files (HTML, CSS, JS) for the user interface.
- `services/`: Specialized services for LLM communication and Google Sheets interaction.
- `run.py`: The main entry point to launch both backend and frontend.
- `requirements.txt`: List of required Python libraries.
- `.env`: (User-created) Configuration for API keys.
- `credentials.json`: (User-provided) Google Service Account credentials.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
