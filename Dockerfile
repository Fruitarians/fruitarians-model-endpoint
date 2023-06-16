FROM python:3.11.2-slim-buster

RUN  mkdir -p  /fruitarians-model
WORKDIR  /fruitarians-model

RUN pip install --no-cache-dir -U pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY  . .

CMD ["python", "main.py"]