FROM python:3.6.6-slim-stretch

WORKDIR /app

ENV PYTHONPATH=/app

ADD . /app

RUN apt-get update \
  && pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]
