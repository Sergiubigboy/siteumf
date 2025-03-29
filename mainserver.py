from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('mainpage.html', title="Bine ați venit!")

@app.route('/despre')
def despre():
    return render_template('despre.html')

app.run(debug=True)