"""
Links:
- google fonts: https://fonts.google.com/?preview.text=Hi.%20I%27m%20Spencer.&preview.text_type=custom
"""

from flask import Flask, render_template
from whitenoise import WhiteNoise


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def display_home():
        return render_template("homepage.html")

    app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/", prefix="assets/")

    return app
