#!/usr/bin/python3
""" Simple Flask App"""
from flask import Flask, render_template
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


py_default = {'text': 'is cool'}


@app.route("/python/", defaults=py_default, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    Variable Rules Python
    """
    result = "Python " + text.replace("_", " ")
    return result


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Number Display
    """
    result = str(n) + " is a number"
    return result


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_html(n):
    """
    Number Display in a Page
    """
    return render_template('5-number.html', n=str(n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
