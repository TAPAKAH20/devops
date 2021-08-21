"""
An app displaying current time in MSK timezone
"""
import datetime

from flask import Flask


app = Flask(__name__)

# Timezone offset for MSK, which is GMT+3
MSK_TZ = datetime.timezone(+datetime.timedelta(hours=3))


@app.route("/")
def hello_world():
    """
        Index page of the app
        Takes current time and displays it on the "/" page
    """
    time_now = datetime.datetime.now(tz=MSK_TZ)
    return f"<p> {time_now.strftime('%X')} </p>"
