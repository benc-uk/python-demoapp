FROM python:3

WORKDIR /demoapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY run.py .
COPY app ./app

EXPOSE 8080

CMD ["python", "run.py"]