"""
A simple web app for the DevOps interview project.
Just says hello and shows it's working.
"""

from flask import Flask
import os

# Create our web app
app = Flask(__name__)

# What message to show (can be changed with environment variables)
APP_MESSAGE = os.getenv("APP_MESSAGE", "Hello, DevopsCardmarket Interview!")
APP_PORT = int(os.getenv("APP_PORT", 8080))

@app.route("/")
def main_page():
    """The main page that shows our message."""
    return APP_MESSAGE

@app.route("/health")
def health_check():
    """A simple health check for Kubernetes to know the app is running."""
    return "Application is healthy", 200

if __name__ == "__main__":
    # Run the app on all network interfaces so Kubernetes can reach it
    app.run(host="0.0.0.0", port=APP_PORT, debug=False)  # nosec B104, semgrep:ignore python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
