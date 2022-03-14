"""
Links:
- google fonts: https://fonts.google.com/?preview.text=Hi.%20I%27m%20Spencer.&preview.text_type=custom
"""

from flask import Flask, render_template, send_from_directory
from whitenoise import WhiteNoise


app = Flask(__name__)
app.static_folder = "static"
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/", prefix="assets/")


@app.route("/static/<path:name>")
def download_file(name):
    return send_from_directory()


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/writeups")
def writeups():
    return render_template("writeups.html")
