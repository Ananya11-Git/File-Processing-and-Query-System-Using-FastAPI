"""
This is the __init__.py file for the app package.
It initializes the FastAPI application.
"""
!git clone https://github.com/Ananya11-Git/File-Processing-and-Query-System-Using-FastAPI.git
%cd File-Processing-and-Query-System-Using-FastAPI

# Install dependencies
!pip install -r requirements.txt

# Run FastAPI server
import threading
from pyngrok import ngrok

# Start Uvicorn in a separate thread
def run():
    !uvicorn app.main:app --host 0.0.0.0 --port 8080

threading.Thread(target=run).start()

# Expose port using ngrok
from pyngrok import ngrok
!ngrok http 8000
ngrok.set_auth_token("2qDWkqJBOIEP8sTMS86qPcKqTcG_3rfH2kSVs9MXqKFQ2jxc4")
public_url = ngrok.connect(8080)
print("Public URL:", public_url.public_url)
