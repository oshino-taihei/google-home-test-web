from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def insert():
    data = request.args.get('data', type = str)

@app.route('/echo', methods=['GET', 'POST'])
def echo():
    message = request.json.get("result").get("parameters").get("message")
    output = {
        "speech": message
    }
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
