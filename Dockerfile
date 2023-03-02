FROM python:3.8.10-slim-buster
WORKDIR /src
COPY . .
RUN pip3 install -r requirements.txt
RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
