FROM python:3.7-slim

COPY requirements_service.txt requirements.txt
COPY datasets/model.joblib /
COPY service/main.py /

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]