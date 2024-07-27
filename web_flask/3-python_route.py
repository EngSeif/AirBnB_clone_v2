#!/usr/bin/python3
""" Simple Flask App"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    result = "C " + text.replace("_", " ")
    return result


py_default = {'text': 'is cool'}


@app.route("/python/", defaults=py_default, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    result = "Python " + text.replace("_", " ")
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
