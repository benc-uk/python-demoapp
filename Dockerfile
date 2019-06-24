FROM python:3.6-stretch
LABEL Name="Python Flask Demo App" Version=1.3.0 

WORKDIR /demoapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY run.py .
COPY app ./app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]