# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install PostgreSQL development tools
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /Backend

# Copy the requirements file into the container
COPY api.py .
COPY requirements.txt .
COPY models.py ./Backend/
COPY database.py ./Backend/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0"]
