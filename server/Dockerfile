FROM python:latest

RUN mkdir /code

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=3000"]