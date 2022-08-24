import os
from flask import Flask, render_template, send_from_directory
cwd = os.getcwd()

app = Flask(__name__, template_folder=cwd, static_folder=cwd)


@app.route("/")
def intro():
    return render_template("xash-intro.html")


@app.route("/xash.html")
def xash():
    return render_template("xash.html")


@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(cwd, path)


if __name__ == "__main__":
    app.run(debug=True)
