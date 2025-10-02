# I am adding comments here for better understanding
# I am using a lightweight Python image here
FROM python:3.10-slim

# I am setting the working directory here
WORKDIR /app

# I am installing dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# I am copying app code from app.py
COPY app.py .

# I am running the app here
EXPOSE 8080
CMD ["python", "app.py"]
