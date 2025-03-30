from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('mainpage.html', subtitlu="Acasa", title="Bine ați venit!", background="bgmain.png")

@app.route('/despre')
def despre():
    return render_template('despre.html', subtitlu="Despre", title="Despre Noi", background="liceu2.jpeg")

@app.route('/elevi')
def elevi():
    return render_template('elevi.html', subtitlu="Elevi", title="Elevi", background="bgmain.png")

@app.route('/profesori')
def profesori():
    return render_template('profesori.html', subtitlu="Profesori", title="Corp Profesoral", background="bgmain.png")

@app.route('/echohub')
def echohub():
    return render_template('echohub.html', subtitlu="Echohub", title="Echohub", background="bgmain.png")

@app.route('/premii')
def premii():
    return render_template('premii.html', subtitlu="Premii", title="Premii", background="bgmain.png")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")