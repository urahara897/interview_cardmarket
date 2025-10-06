"""
Flask Web Application for Kubernetes DevOps Interview Project

This microservice provides a simple HTTP endpoint that returns a configurable
message, demonstrating containerized application deployment patterns.
"""

from flask import Flask
import os

# Initialize Flask application instance
app = Flask(__name__)

# Configuration from environment variables with sensible defaults
APP_MESSAGE = os.getenv("APP_MESSAGE", "Hello, DevopsCardmarket Interview!")
APP_PORT = int(os.getenv("APP_PORT", 8080))

@app.route("/")
def health_endpoint():
    """
    Primary application endpoint returning the configured message.
    
    This endpoint serves as both a health check and the main application
    functionality, demonstrating a simple microservice pattern.
    """
    return APP_MESSAGE

@app.route("/health")
def health_check():
    """
    Dedicated health check endpoint for Kubernetes liveness and readiness probes.
    
    Returns a simple status message indicating the application is running.
    """
    return "Application is healthy", 200

if __name__ == "__main__":
    # Start the Flask development server
    # Binding to 0.0.0.0 allows external connections in containerized environments
    app.run(host="0.0.0.0", port=APP_PORT, debug=False)
