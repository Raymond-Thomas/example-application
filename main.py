import os
from flask import Flask


app = Flask(__name__)
version = os.getenv("APP_VERSION", "unknown")

@app.route('/')
def index():
    return f'Hello Argo v3.0 - Blue/Green Deployment!'

app.run(host='0.0.0.0', port=8080)