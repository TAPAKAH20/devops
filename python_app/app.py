import datetime

from flask import Flask

app = Flask(__name__)

# Timezone offset to Moscow time / GMT+3
MSK_TZ = datetime.timezone(+datetime.timedelta(hours=3))


@app.route("/")
def hello_world():
    t = datetime.datetime.now(tz=MSK_TZ)
    return f"<p> {t.strftime('%X')} </p>"
