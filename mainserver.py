from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('mainpage.html')

app.run(debug=True)