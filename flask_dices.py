from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to Dark Souls board game dice statistics'
