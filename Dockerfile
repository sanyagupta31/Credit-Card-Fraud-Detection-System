FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Streamlit default port 8501 use karta hai
EXPOSE 8501

# Streamlit ko chalane ki command
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]