from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    print("Someone visited the home page")
    return render_template(f"index.html")

@app.errorhandler(500)
def internal_error(error):
    return "500"

app.run()