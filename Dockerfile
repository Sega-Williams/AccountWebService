FROM ubuntu

RUN apt update
RUN apt install python3 python3-pip -y

RUN pip3 install flask

COPY . /web-service

CMD python3 /web-service/server.py

# FROM python:3.9
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# CMD ["python", "server.py"]
