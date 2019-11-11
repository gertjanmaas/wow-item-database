FROM python:3.7

WORKDIR /app

COPY api/requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache

COPY . .

EXPOSE 5000

CMD ["python", "/app/api/service.py"]
