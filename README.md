# AIssistant-Agents

This project is a local assistant application built with **Streamlit** that integrates multiple AI-driven agents to manage meetings, notes, and emails. The system is fully open-source, stores data locally, and does not rely on any cloud services.

## Features

1. **Meeting Agent**
   - Create and manage meetings stored in `.ics` files.
   - View all scheduled meetings.

2. **Notes Agent**
   - Create and store notes in a SQLite database.
   - Export notes to a `.csv` file.

3. **Email Agent**
   - Send emails using `yagmail`.

4. **Integrated AI Chat**
   - Utilizes the Ollama model locally for AI-powered interactions.
## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create a Python Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
Install the required packages from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Download the Ollama Model
Pull the required Ollama model to ensure local availability:
```bash
ollama pull phi4
```

### 5. Set Environment Variables
Create a `.env` file in the root directory and define your email credentials:
```
EMAIL=your_email@example.com
EMAIL_PASSWORD=your_password
```
Alternatively, export the variables directly in your terminal:
```bash
export EMAIL=your_email@example.com
export EMAIL_PASSWORD=your_password
```
On Windows:
```powershell
set EMAIL=your_email@example.com
set EMAIL_PASSWORD=your_password
```

### 6. Run the Application
Start the Streamlit application:
```bash
streamlit run app.py
```

## Usage

### Main Interface
1. Navigate to the Streamlit interface in your browser (typically at `http://localhost:8501`).
2. Use the sidebar to select different features:
   - **Meetings**: Create or view scheduled meetings.
   - **Notes**: Create, view, or export notes.
   - **Emails**: Send an email to a recipient.

### Notes Export
Exported notes are saved as `notes.csv` in the current working directory.

### AI Chat
Use the integrated chat feature powered by the Ollama model for intelligent interactions.
