from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/<path:path>')
def hello(path):
    return "[GUILLERMO] Hello World!"
