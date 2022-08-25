import os
from flask import Flask, render_template, send_from_directory
cwd = os.getcwd()

app = Flask(__name__, template_folder=cwd, static_folder=cwd)


@app.route("/")
def xash():
    return render_template("xash.html")


@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(cwd, path)


if __name__ == "__main__":
    if not os.path.isfile(cwd + "/hl1.zip"):
        os.system("zip -F hl1_split.zip --out hl1.zip")
    app.run(debug=True)
