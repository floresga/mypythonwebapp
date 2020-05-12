from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/<path:path>')
def send_files(path):
    print path
    # return send_from_directory('static', path)

if __name__ == "__main__":
    app.run()
