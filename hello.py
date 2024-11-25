from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(f"index.html")

@app.errorhandler(500)
def internal_error(error):
    return "500"
