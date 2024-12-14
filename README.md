# File-Processing-and-Query-System-Using-FastAPI
A system that enables users to upload files, extracts relevant content such as text and tables, and interacts with the OpenAI Large Language Model to answer user queries.  The system returns responses in a structured JSON format.
# File Processing and Query System Using FastAPI

## **Overview**
This project is an end-to-end file processing and query system built using FastAPI. The system enables users to upload files (PDF or text format), extract relevant content such as text and tables, and interact with a Large Language Model (LLM) to answer user queries. Responses are returned in a consistent and structured JSON format.

---

## **Features**

1. **File Upload Interface**
   - Allows users to upload PDF or text files via an API endpoint.
   - 
2. **LLM Query Integration**
   - Processes user queries using LLM APIs such as ChatGPT or Gemini.
   - Supports requests for summaries, insights, and specific data extractions.

3. **Structured Output**
   - Returns query responses in a well-structured JSON format.

## **Technologies Used**

- **Programming Language**: Python
- **Framework**: FastAPI
- **Libraries**:
  - PDF Parsing: `PyPDF2`, `pdfplumber`
  - OCR (optional): `Tesseract`, `pytesseract`
  - JSON Handling: `json`
  - API Interaction: `httpx` or `requests`
- **Large Language Model (LLM)**: ChatGPT or Gemini APIs
- **Server**: Uvicorn (ASGI Server)

---

## **Project Structure**
```
project-directory/
├── app/
│   ├── __init__.py
│   ├── main.py           # Main application logic
│   ├── routes.py         # API endpoints
│   ├── utils.py          # Helper functions for content extraction and querying
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
```

---

## **Setup Instructions**

### Prerequisites

- Python 3.8+
- Pip package manager

### Steps to Set Up Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access the Application**:
   - Open your browser and navigate to: `http://127.0.0.1:8000`
   - API documentation is available at: `http://127.0.0.1:8000/docs`

---

## **API Endpoints**

1. **File Upload**
   - Endpoint: `/upload`
   - Method: `POST`
   - Description: Accepts PDF or text files for processing.

2. **Process Content**
   - Endpoint: `/process`
   - Method: `POST`
   - Description: Extracts text and tables from uploaded files.

3. **Query LLM**
   - Endpoint: `/query`
   - Method: `POST`
   - Description: Sends queries to the LLM and retrieves structured responses.

---

## **Sample Usage**

### File Upload
Example cURL command to upload a file:
```bash
curl -X POST "http://127.0.0.1:8000/upload" \
     -F "file=@example.pdf"
```

### Query LLM
Example cURL command to query the LLM:
```bash
curl -X POST "http://127.0.0.1:8000/query" \
     -H "Content-Type: application/json" \
     -d '{"query": "Summarize the financial section"}'


