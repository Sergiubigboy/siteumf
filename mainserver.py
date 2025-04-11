from flask import Flask, render_template, request
from date import Profesori, Clase, profesori, clase, normalize_text, anunturi, activitati
import unicodedata


# Inițializează catalogul profesorilor
profesori = Profesori(profesori)
clase = Clase(clase)


app = Flask(__name__)

app.jinja_env.globals.update(normalize_text=normalize_text)

@app.route('/')
def mainpage():
    return render_template('mainpage.html', subtitlu="Acasa", title="Bine ati venit!", background="static/images/poze-hero/bgmain.png", anunturi=anunturi)

@app.route('/contact')
def despre():
    return render_template('contact.html', subtitlu="Contact", title="Contact", no_hero=True)

@app.route('/clase')
def lista_clase():
    # Obține toate clasele din obiectul Clase
    clase_distincte = [
        (clasa["numar"], clasa["litera"], clasa["profil"])
        for clasa in clase.clase
    ]
    
    # Sortează clasele
    clase_distincte = sorted(clase_distincte)

    # Obține termenul de căutare
    search_query = request.args.get('search', '').lower()
    if search_query:
        clase_distincte = [
            (numar, litera, profil) for numar, litera, profil in clase_distincte
            if search_query in f"{numar}{litera}{profil}".lower()
        ]
    
    return render_template(
        'elevi.html',
        clase=clase_distincte,
        subtitlu="Elevi",
        title="Elevi",
        background="static/images/poze-hero/pozaelevi.jpg"
    )
@app.route('/elevi/<int:clasa>/<litera>')
def elevi_clasa(clasa, litera):
    # Filtrează clasa specificată
    clasa_filtrata = next(
        (c for c in clase.clase if c["numar"] == clasa and c["litera"].lower() == litera.lower()), 
        None
    )

    if not clasa_filtrata:
        return f"Clasa {clasa}{litera} nu a fost găsită.", 404

    # Obține elevii și profilul clasei
    elevi_filtrati = clasa_filtrata["elevi"]
    profil = clasa_filtrata["profil"]

    # Filtrează elevii cu performanțe
    elevi_cu_performante = [
        elev for elev in elevi_filtrati if "performante" in elev
    ]

    # Setează orarul în funcție de clasă
    orar = f"static/images/orar{clasa}{litera}.PNG"

    return render_template(
        'elevi_clasa.html',
        elevi=elevi_filtrati,
        elevi_cu_performante=elevi_cu_performante,
        clasa=f"{clasa}{litera}",
        profil=profil,
        citat=clasa_filtrata["citat"],
        subtitlu=f"Clasa {clasa}{litera}",
        title=f"Clasa {clasa}{litera}",
        background=f"static/images/Poza-UMFST/grup{clasa}{litera}/bgclasa{clasa}{litera}.jpg",
        orar=orar,
        no_hero=True
    )


@app.route('/corp-profesoral')
def lista_profesori():
    # Obține termenul de căutare din query string
    search_query = request.args.get('search', '').lower()
    search_query_normalized = normalize_text(search_query)
    
    # Filtrează profesorii pe baza termenului de căutare (nume sau materie)
    if search_query:
        profesori_filtrati = [
            profesor for profesor in profesori.personal
            if search_query_normalized in normalize_text(profesor["nume"]) or
               search_query_normalized in normalize_text(profesor["materie"])
        ]
    else:
        profesori_filtrati = profesori.personal

    # Transmite lista filtrată către șablon
    return render_template(
        'profesori.html',
        profesori=profesori_filtrati,
        subtitlu="Corp Profesoral",
        title="Corp Profesoral",
        background="static/images/poze-hero/pozaprofesori.jpg"
    )

@app.route('/corp-profesoral/<nume>')
def pagina_profesor(nume):
    # Găsește profesorul după nume
    profesor = profesori.findbyname(nume)
    if profesor:
        return render_template('pagina_profesor.html', profesor=profesor, subtitlu=profesor["nume"], title=profesor["nume"], background="bgmain.png", no_hero=True)
    else:
        return "Profesorul nu a fost găsit.", 404

@app.route('/activitati')
def echohub():
    return render_template('activitati.html', subtitlu="Activități", title="Activități", background="static/images/Poza-UMFST/grup9A/bgclasa9A.jpg", activitati=activitati)

@app.route('/campania-conversatii-in-jurul-scolii')
def activitate_1():
    activitate = {
        "titlu": "Campania: Conversații în jurul școlii",
        "imagine": "BancaDinFata.jpg",
    }
    return render_template(
        'campania.html',
        activitate=activitate,
        subtitlu=activitate["titlu"],
        title=activitate["titlu"]
    )

@app.route('/lyceumcloud-umfst')
def activitate_2():
    activitate = {
        "titlu": "LyceumCloud.UMFST",
        "imagine": "BancaDinFata.jpg",
    }
    return render_template(
        'lyceumcloud-umfst.html',
        activitate=activitate,
        subtitlu=activitate["titlu"],
        title=activitate["titlu"]
    )

@app.route('/banca-din-fata')
def activitate_3():
    activitate = {
        "titlu": "Banca din față",
        "imagine": "BancaDinFata.jpg",
    }
    return render_template(
        'banca-din-fata.html',
        activitate=activitate,
        subtitlu=activitate["titlu"],
        title=activitate["titlu"]
    )

@app.route('/mix-it-hub-umfst')
def activitate_4():
    activitate = {
        "titlu": "Mix IT Hub UMFST – Centrul pasiunilor elevilor",
        "imagine": "BancaDinFata.jpg",
    }
    return render_template(
        'mix-it-hub-umfst.html',
        activitate=activitate,
        subtitlu=activitate["titlu"],
        title=activitate["titlu"]
    )

@app.route('/act4change')
def activitate_5():
    activitate = {
        "titlu": "Act4Change",
        "imagine": "BancaDinFata.jpg",
    }
    return render_template(
        'act4change.html',
        activitate=activitate,
        subtitlu=activitate["titlu"],
        title=activitate["titlu"]
    )

@app.route('/portile-deschise-umfst')
def activitate_6():
    activitate = {
        "titlu": "Porțile deschise ale liceului UMFST",
        "imagine": "BancaDinFata.jpg",
    }
    return render_template(
        'portile-deschise-umfst.html',
        activitate=activitate,
        subtitlu=activitate["titlu"],
        title=activitate["titlu"]
    )

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
    return render_template('facilitati.html', title="Facilități", subtitlu="Facilități", background="static/images/poze-hero/facilitati1.jpg")

@app.route('/corp-administrativ')
def corp_administrativ():
    return render_template(
        'administrativ.html',
        title="Corp Administrativ",
        subtitlu="Echipa Administrativă",
        background="static/images/poze-hero/Hero-principal.png"
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")