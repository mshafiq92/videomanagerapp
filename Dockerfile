# Use lightweight Python 3.12 base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for better Docker layer caching)
COPY requirements.txt .
# Install Python dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY app/ ./app/
# Copy environment variables file
COPY .env .

# Document that app uses port 8000
EXPOSE 8000

# Start FastAPI app with uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]