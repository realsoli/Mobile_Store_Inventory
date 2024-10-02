FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
