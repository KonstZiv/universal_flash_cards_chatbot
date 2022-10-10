FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
#COPY /app/src/ ./src/

