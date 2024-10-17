FROM python:3.11-slim

RUN apt-get update && apt-get install -y sqlite3

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["bash"]
