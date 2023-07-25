FROM python:3.9-slim

RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "app.py"]
