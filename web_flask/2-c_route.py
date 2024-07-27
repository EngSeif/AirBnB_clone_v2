#!/usr/bin/python3
""" Simple Flask App"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Home():
    """
    Welcome Text
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    HBNB Route
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Variable Rules
    """
    result = "C " + text.replace("_", " ")
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
