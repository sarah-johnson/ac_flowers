FROM python:3.8

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENV FLASK_APP=ac_flowers

CMD ["flask", "run", "--host", "0.0.0.0"]
