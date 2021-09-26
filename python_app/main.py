"""
An app displaying current time in MSK timezone
"""
import datetime

from flask import Flask


APP = Flask(__name__)

# Timezone offset for MSK, which is GMT+3
MSK_TZ = datetime.timezone(+datetime.timedelta(hours=3))


@APP.route("/")
def index():
    """
        Index page of the APP
        Takes current time and displays it on the "/" page
    """
    time_now = datetime.datetime.now(tz=MSK_TZ)
    with open("visitors.txt", "a") as f:
        f.write(time_now.strftime('%X') + '\n')
    return f"<p> {time_now.strftime('%X')} </p>"

@APP.route("/healthcheck")
def health_check():
    """
        Stub for future healthcheck function
    """
    return ''

@APP.route("/visitors")
def visitors():
    resp = ''
    with open("visitors.txt") as f:
        for line in f.readlines():
            resp += f"<p> {line} </p>"
    return resp