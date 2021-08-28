"""
An app displaying current time in MSK timezone
"""
import datetime

from flask import Flask


app = Flask(__name__)

# Timezone offset for MSK, which is GMT+3
MSK_TZ = datetime.timezone(+datetime.timedelta(hours=3))


@app.route("/")
def index():
    """
        Index page of the app
        Takes current time and displays it on the "/" page
    """
    time_now = datetime.datetime.now(tz=MSK_TZ)
    return f"<p> {time_now.strftime('%X')} </p>"

@app.route("/healthcheck")
def health_check():
    """
        Stub for future healthcheck function
    """
    return ''
