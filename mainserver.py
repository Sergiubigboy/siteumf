from Flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def mainpage():
    return "Hello, World!"

app.run(debug=True)