FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
EXPOSE 3478
