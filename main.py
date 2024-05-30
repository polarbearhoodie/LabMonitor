import os
import datetime
import calendar

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return get_current_time()


@app.route("/image")
def image():
    return send_file('tmp/output.png', mimetype='image/gif')


def generate_image(page):
    # we use conversion to drop from three channels to a single 8-bit channel
    os.system("gm convert tmp/source.png tmp/lossy.jpg")
    os.system("gm convert tmp/lossy.jpg -colorspace Gray -resize 600x800 tmp/output.png")

# returns the current time as a formatted string
# the string is HR:MIN AM/PM - DAY, MONTH #, 20xx
def get_current_time():
    today = datetime.datetime.today()

    hour = today.hour
    minute = today.minute

    if hour > 12:
        state = "AM"
        hour -= 12
    else:
        state = "PM"

    day_name = calendar.day_name[today.weekday()]
    month_name = calendar.month_name[today.month]
    
    day_number = today.day
    year_number = today.year

    return "{0}:{1} {2} - {3}, {4} {5}, {6}".format(hour, minute, state, day_name, month_name, day_number, year_number)

print(get_current_time())
