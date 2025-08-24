# Use Python 3.11 slim base image for smaller size while keeping essential packages
FROM python:3.11-slim

# Set working directory - all commands will run from /app
WORKDIR /app

# Copy requirements first for Docker layer caching optimization
# If requirements.txt doesn't change, this layer gets reused on rebuild
COPY requirements.txt .

# Install Python dependencies without cache to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy FastAPI application code to /app/app/
COPY app/ app/

# Copy startup script to /app/run.py
COPY run.py .

# Document that the app uses port 8000 (doesn't actually expose it)
EXPOSE 8000

# Start the FastAPI server when container runs
CMD ["python", "run.py"]

# File mapping:
# Local: ./requirements.txt → Container: /app/requirements.txt
# Local: ./run.py → Container: /app/run.py
# Local: ./app/ → Container: /app/app/
# Local: ./app/main.py → Container: /app/app/main.py
# Local: ./app/api/ → Container: /app/app/api/
# Local: ./app/models/ → Container: /app/app/models/
# Local: ./app/operations/ → Container: /app/app/operations/