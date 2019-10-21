import subprocess
import os

from dotenv import load_dotenv
from github_webhook import Webhook
from flask import Flask

load_dotenv()

app = Flask(__name__)
webhook = Webhook(app, os.getenv('ENDPOINT'), os.getenv('SECRET'))

@webhook.hook()
def on_push(data):
    subprocess.run([os.getenv('ONPUSH_SCRIPT')])

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all_route(path):
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
