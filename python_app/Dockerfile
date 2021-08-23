FROM python:3.9-alpine
LABEL version="0.13"

WORKDIR /


COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt 

RUN adduser -D user

COPY app.py ./app/app.py

USER user

WORKDIR /app/

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0"]