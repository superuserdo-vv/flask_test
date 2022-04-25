from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def users():
    return "<p>{}<br>{}</p>".format(request.method, request.url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)