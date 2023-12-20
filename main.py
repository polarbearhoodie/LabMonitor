import os
import threading
from render import render
from flask import Flask, render_template, send_file
app = Flask("firewood")

# begin the image service
image_service = threading.Thread(target=render)
image_service.start()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/image")
def image():
    generate_image("index.html")
    return send_file('tmp/output.png', mimetype='image/gif')


def generate_image(page):
    # we use conversion to drop from three channels to a single 8-bit channel
    os.system("gm convert tmp/source.png tmp/lossy.jpg")
    os.system("gm convert tmp/lossy.jpg -colorspace Gray -resize 600x800 tmp/output.png")
