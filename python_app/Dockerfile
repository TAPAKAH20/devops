FROM python:3.9-alpine
LABEL version="0.13"

WORKDIR /


COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt 

RUN adduser -D user

COPY main.py ./app/main.py

RUN chmod 777 /app

USER user

WORKDIR /app/

EXPOSE 5000

ENV FLASK_APP=main

CMD [ "flask", "run", "--host=0.0.0.0"]
