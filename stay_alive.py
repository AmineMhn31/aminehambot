from flask import Flask
from threading import Thread
import os

from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
