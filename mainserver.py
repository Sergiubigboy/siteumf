from flask import Flask, render_template
from date import CatalogPersonal, profesori

Profesori = CatalogPersonal(profesori)
app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('mainpage.html', subtitlu="Acasa", title="Bine ați venit!", background="bgmain.png")

@app.route('/revista')
def despre():
    return render_template('despre.html', subtitlu="Despre", title="Despre Noi", background="liceu2.jpeg")

@app.route('/elevi')
def elevi():
    return render_template('elevi.html', subtitlu="Elevi", title="Elevi", background="bgmain.png")

@app.route('/corp-profesoral')
def profesori():
    return render_template('profesori.html', subtitlu="Profesori", title="Corp Profesoral", background="bgmain.png")

@app.route('/echohub')
def echohub():
    return render_template('echohub.html', subtitlu="Echohub", title="Echohub", background="bgmain.png")

@app.route('/podcast')
def premii():
    return "SOON!!!"



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")