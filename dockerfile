FROM python:3.11-slim

WORKDIR /app

# System dependencies voor MySQL client
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose poort 5000
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
