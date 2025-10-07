# Start with a lightweight Python image
FROM python:3.10-slim

# Set up our working directory
WORKDIR /app

# Install the Python packages we need
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy our app code into the container
COPY app.py .

# Create a regular user (not root) for security
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

# Tell Docker which port our app uses
EXPOSE 8080

# Start the app when the container runs
CMD ["python", "app.py"]
