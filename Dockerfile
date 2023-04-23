FROM python:alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
ENTRYPOINT ["python3"]
CMD ["manage.py", "makemigrations"]
CMD ["manage.py", "migrate"]
CMD ["manage.py", "runserver", "0.0.0.0:4321"]