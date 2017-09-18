FROM python:3
LABEL Name="Python Flask Demo App" Version=1.0.0 
ARG port=5000
ENV PORT=$port

WORKDIR /demoapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY run.py .
COPY app ./app

EXPOSE $port

CMD ["python", "run.py"]