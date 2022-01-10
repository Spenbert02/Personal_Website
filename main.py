"""
Links:
- google fonts: https://fonts.google.com/?preview.text=Hi.%20I%27m%20Spencer.&preview.text_type=custom
"""

from flask import Flask, render_template
from whitenoise import WhiteNoise


app = Flask(__name__)
app.static_folder = "static"
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/", prefix="assets/")


@app.route("/")
def home():
    return render_template("homepage.html")
