FROM python:3.8

WORKDIR /TelegramBot

COPY requirements.txt /TelegramBot
RUN pip install -r requirements.txt

COPY . /TelegramBot

CMD ["python", "main.py"]