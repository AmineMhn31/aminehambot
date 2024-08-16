from flask import Flask
from threading import Thread
import os

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    # Use the environment-specified port if available; otherwise, default to 4000
    port = int(os.environ.get('PORT', 8080)
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    # Start the web server in a new thread
    t = Thread(target=run)
    t.start()
