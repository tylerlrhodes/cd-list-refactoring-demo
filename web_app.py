from flask import Flask
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='app.html'))



