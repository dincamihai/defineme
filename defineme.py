import flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    with open('static/jsons/links.json') as f:
        data = flask.json.loads(f.read())
        return render_template('index.html', **data)

if __name__ == "__main__":
    app.run()
