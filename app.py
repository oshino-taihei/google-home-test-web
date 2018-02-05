import sys
import json
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def insert():
    data = request.args.get('data', type = str)

@app.route('/echo')
def echo():
    output = {
        "speech": "hello"
    }
    return json.dumps(output)

if __name__ == "__main__":
    app.run(debug=True)
