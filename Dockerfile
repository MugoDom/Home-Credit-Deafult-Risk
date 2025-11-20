# lightweight python base
FROM python:3.11-slim

# Creates app directory
WORKDIR /app

# Installs system deps
RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY api/ api/
COPY src/ src/
COPY model/ model/
COPY data/clean/ data/clean/

# Expose port for Uvicorn
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
