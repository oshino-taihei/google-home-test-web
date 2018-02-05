import sys
import json
from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def insert():
    data = request.args.get('data', type = str)

@app.route('/echo', methods=['GET', 'POST'])
def echo():
    output = {
        "speech": "hello"
    }
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
