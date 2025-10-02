from flask import Flask
import os

app = Flask(__name__)

APP_MESSAGE = os.getenv("APP_MESSAGE", "Hello, DevopsCardmarket Interview!")
APP_PORT = int(os.getenv("APP_PORT", 8080))

@app.route("/")
def hello():
    return APP_MESSAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)
