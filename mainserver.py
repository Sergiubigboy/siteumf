from flask import Flask, render_template, request
from date import CatalogPersonal, profesori, elevi, normalize_text, anunturi


# Inițializează catalogul profesorilor
Profesori = CatalogPersonal(profesori)
Elevi = CatalogPersonal(elevi)


app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('mainpage.html', subtitlu="Acasa", title="Bine ati venit!", background="static/images/bgmain.png", anunturi=anunturi)

@app.route('/contact')
def despre():
    return render_template('contact.html', subtitlu="Contact", title="Contact", no_hero=True)

@app.route('/clase')
def lista_clase():
    # Obține toate clasele distincte
    clase = sorted(set((elev["clasa"], elev["litera"], elev["profil"]) for elev in elevi))
    
    # Obține termenul de căutare
    search_query = request.args.get('search', '').lower()
    if search_query:
        clase = [
            (clasa, litera, profil) for clasa, litera, profil in clase
            if search_query in f"{clasa}{litera}{profil}".lower()
        ]
    return render_template(
        'elevi.html',
        clase=clase,
        subtitlu="Elevi",
        title="Elevi",
        background=f"static/images/pozaelevi.jpg"
    )
@app.route('/elevi/<int:clasa>/<litera>')
def elevi_clasa(clasa, litera):
    # Filtrează elevii din clasa specificată
    elevi_filtrati = [
        elev for elev in elevi if elev["clasa"] == clasa and elev["litera"] == litera
    ]
    # Obține profilul clasei (toți elevii din aceeași clasă au același profil)
    profil = elevi_filtrati[0]["profil"] if elevi_filtrati else "Necunoscut"
    return render_template(
        'elevi_clasa.html',
        elevi=elevi_filtrati,
        clasa=f"{clasa}{litera}",
        profil=profil,
        subtitlu=f"Clasa {clasa}{litera}",
        title=f"Clasa {clasa}{litera}",
        background=f"static/images/Poza-UMFST/grup{clasa}{litera}/bgclasa{clasa}{litera}.jpg",
        no_hero=True
    )

@app.route('/catalog')
def catalog():
    return render_template('catalog.html', title="Catalog", subtitlu="Catalog")

@app.route('/performante')
def performante():
    return render_template('performante.html', title="Performanțe", subtitlu="Performanțe")
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
        background="static/images/pozaprofesori.jpg"
    )

@app.route('/corp-profesoral/<nume>')
def pagina_profesor(nume):
    # Găsește profesorul după nume
    profesor = Profesori.findbyname(nume)
    if profesor:
        return render_template('pagina_profesor.html', profesor=profesor, subtitlu=profesor["nume"], title=profesor["nume"], background="bgmain.png", no_hero=True)
    else:
        return "Profesorul nu a fost găsit.", 404

@app.route('/activitati')
def echohub():
    return render_template('activitati.html', subtitlu="Activități", title="Activități", background="static/images/Poza-UMFST/grup9A/bgclasa9A.jpg")
@app.route('/regulamente')
def regulamente():
    return render_template('regulamente.html', title="Regulamente", subtitlu="Regulamente")

@app.route('/admitere')
def admitere():
    return render_template('admitere.html', subtitlu="Admiteri", title="Admiteri", background="bgmain.png")

@app.route('/transferuri')
def transferuri():
    return render_template('transferuri.html', subtitlu="Transferuri", title="Transferuri", background="bgmain.png")

@app.route('/proceduri')
def proceduri():
    return render_template('proceduri.html', subtitlu="Proceduri", title="Proceduri", background="bgmain.png")

@app.route('/facilitati')
def facilitati():
    return render_template('facilitati.html', title="Resurse materiale", subtitlu="Facilități")

@app.route('/corp-administrativ')
def corp_administrativ():
    return render_template(
        'administrativ.html',
        title="Corp Administrativ",
        subtitlu="Echipa Administrativă",
        background="static/images/Hero-principal.png"
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")