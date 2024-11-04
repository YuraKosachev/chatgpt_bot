FROM python:latest

RUN mkdir /ai_telegram_bot

WORKDIR /ai_telegram_bot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python main.py