from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('mainpage.html', subtitlu="Acasa", title="Bine ați venit!")

@app.route('/despre')
def despre():
    return render_template('despre.html', subtitlu="Despre", title="Despre Noi")

@app.route('/elevi')
def elevi():
    return render_template('elevi.html', subtitlu="Elevi", title="Elevi")

@app.route('/profesori')
def profesori():
    return render_template('profesori.html', subtitlu="Profesori", title="Profesori")

@app.route('/echohub')
def echohub():
    return render_template('echohub.html', subtitlu="Echohub", title="Echohub")

@app.route('/premii')
def premii():
    return render_template('premii.html', subtitlu="Premii", title="Premii")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")