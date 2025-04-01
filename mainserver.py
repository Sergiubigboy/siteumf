from flask import Flask, render_template, request
from date import CatalogPersonal, profesori
import unicodedata

# Inițializează catalogul profesorilor
Profesori = CatalogPersonal(profesori)

def normalize_text(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    ).lower()

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

@app.route('/clasa_9a')
def clasa_9a():
    elevi = [
        "Biris Sergiu", "Corondeanu Raul", "Cucuiet Andrei", "Curta Rares",
        "David Aiana", "Ercean David", "Gherman Cezara", "Jovrea Stefan",
        "Lazar Cristian", "Maier Alia", "Marian Ciprian", "Mitoseriu David",
        "Muth Cristian", "Nagy Eliz", "Oanes Sofia", "Paca Raoul",
        "Pantea Tudor", "Pastia Catinca", "Somesan Adrian", "Staicu Eric",
        "Stinga David", "Stoica Andrei", "Suciu Iustina", "Trifan Raul",
        "Turdean Cleo", "Ungur Filip", "Vasloban Maria"
    ]
    return render_template('clasa_9a.html', elevi=elevi)

@app.route('/clasa_9b')
def clasa_9b():
    elevi = [
        "Bumbac Ileana", "Bumbu Luca", "Colcer Sonia", "Cosarca Alexandru",
        "Cotoi Iulius", "Cretu Daria", "Crisan Andrei", "Dumitru Radu",
        "Florea Sara", "Florea Rares", "Gherman Eric", "Hanc Mihai",
        "Harsa Sofia", "Lazar Larisa", "Loghin Ioana", "Lupsa Maria",
        "Macarie Rares", "Orban David", "Onisor Rares", "Ormenisan Anastatia",
        "Popa Cynthia", "Sabau Raul", "Sandru Octavian", "Serbu Raluca",
        "Szasz Roberta", "Vasiliu Anca", "Vidican Andreea"
    ]
    return render_template('clasa_9b.html', elevi=elevi, hero_text="Clasa a IX-a B")

@app.route('/corp-profesoral')
def lista_profesori():
    # Obține termenul de căutare din query string
    search_query = request.args.get('search', '').lower()
    search_query_normalized = normalize_text(search_query)
    
    # Filtrează profesorii pe baza termenului de căutare (nume sau materie)
    if search_query:
        profesori_filtrati = [
            profesor for profesor in Profesori.personal
            if search_query_normalized in normalize_text(profesor["nume"]) or
               search_query_normalized in normalize_text(profesor["materie"])
        ]
    else:
        profesori_filtrati = Profesori.personal

    # Transmite lista filtrată către șablon
    return render_template(
        'profesori.html',
        profesori=profesori_filtrati,
        subtitlu="Corp Profesoral",
        title="Corp Profesoral",
        background="bgmain.png"
    )

@app.route('/corp-profesoral/<nume>')
def pagina_profesor(nume):
    # Găsește profesorul după nume
    profesor = Profesori.findbyname(nume)
    if profesor:
        return render_template('pagina_profesor.html', profesor=profesor, subtitlu=profesor["nume"], title=profesor["nume"], background="bgmain.png")
    else:
        return "Profesorul nu a fost găsit.", 404

@app.route('/echohub')
def echohub():
    return render_template('echohub.html', subtitlu="Echohub", title="Echohub", background="bgmain.png")

@app.route('/podcast')
def premii():
    return "SOON!!!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")