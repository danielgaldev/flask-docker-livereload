from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def root():
    things = ["list item" for i in range(0, 10)]
    json_content = {"name": "I am a text", "value": 12, "things": things}
    content = json.dumps(json_content, indent=4)
    return render_template("index.html", text=content)
