from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'v4.0.0 - BROKEN VERSION!'  # Pretend this is broken

app.run(host='0.0.0.0', port=8080)