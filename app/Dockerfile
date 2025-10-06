# Multi-stage Dockerfile for Flask application
# Base image: Official Python 3.10 slim variant for minimal attack surface
FROM python:3.10-slim

# Set application working directory
WORKDIR /app

# Install Python dependencies from requirements file
# Using --no-cache-dir to reduce image size and improve security
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code into container
COPY app.py .

# Create non-root user for enhanced security
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

# Expose application port for external access
EXPOSE 8080

# Define application startup command
CMD ["python", "app.py"]
