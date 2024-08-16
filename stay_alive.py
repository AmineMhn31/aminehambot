from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is alive!'

def run():
    port = int(os.environ.get('PORT', 4000))  # Use PORT from environment or default to 4000
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
