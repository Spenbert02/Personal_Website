"""
Links:
- google fonts: https://fonts.google.com/?preview.text=Hi.%20I%27m%20Spencer.&preview.text_type=custom
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def display_home():
    return render_template("templates/homepage.html")
