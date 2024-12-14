

# Initialize FastAPI app
app = FastAPI()

# Define data models
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    response: Union[Dict[str, Union[str, Dict[str, str]]], str]

# OpenAI API Key (replace with your actual key)
openai.api_key = "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"

# Helper functions
def extract_text_from_pdf(file_path: str) -> str:
    """Extracts text from a PDF file."""
    try:
        with pdfplumber.open(file_path) as pdf:
            text = "".join([page.extract_text() for page in pdf.pages])
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting text: {str(e)}")

def extract_tables_from_pdf(file_path: str) -> List[List]:
    """Extracts tables from a PDF file."""
    tables = []
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                tables.extend(page.extract_tables())
        return tables
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting tables: {str(e)}")

def query_llm(prompt: str) -> str:
    """Queries the OpenAI GPT model with the given prompt."""
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error querying LLM: {str(e)}")

# API Endpoints
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """Handles file upload and content extraction."""
    if file.content_type not in ["application/pdf"]:
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name

    # Extract content
    text = extract_text_from_pdf(temp_file_path)
    tables = extract_tables_from_pdf(temp_file_path)

    # Cleanup temporary file
    os.remove(temp_file_path)

    return {
        "filename": file.filename,
        "text": text,
        "tables": tables
    }

@app.post("/query/", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """Handles querying extracted content using the LLM."""
    # Example prompt for querying
    prompt = f"Answer the following query based on the extracted content:\n\n{request.query}"

    response_text = query_llm(prompt)

    return {
        "query": request.query,
        "response": response_text
    }

# Add instructions for running the API in the README.md
# Additional endpoints can be added here if needed for visualization or other features.
