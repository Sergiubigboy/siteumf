from flask import Flask, render_template, request
from date import Profesori, Clase, profesori, clase, normalize_text, anunturi, activitati, celebrari, cluburi, proiecte
import unicodedata

profesori = Profesori(profesori)
clase = Clase(clase)

app = Flask(__name__)

app.jinja_env.globals.update(normalize_text=normalize_text)

@app.route('/')
def mainpage():
    return render_template('mainpage.html', subtitlu="Acasa", title="Bine ați venit!", background="static/images/poze-hero/bgmain.png", anunturi=anunturi)

@app.route('/contact')
def despre():
    return render_template('contact.html', subtitlu="Contact", title="Contact", no_hero=True)

@app.route('/clase')
def lista_clase():
    clase_distincte = [
        (clasa["numar"], clasa["litera"], clasa["profil"])
        for clasa in clase.clase
    ]
    clase_distincte = sorted(clase_distincte)
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
@app.route('/elevi/an-scolar24-25')
def an_scolar_24_25():
    return render_template('an-scolar24-25.html', title="An școlar 24-25")


@app.route('/elevi/<int:clasa>/<litera>')
def elevi_clasa(clasa, litera):
    clasa_filtrata = next(
        (c for c in clase.clase if c["numar"] == clasa and c["litera"].lower() == litera.lower()), 
        None
    )
    if not clasa_filtrata:
        return f"Clasa {clasa}{litera} nu a fost găsită.", 404
    elevi_filtrati = clasa_filtrata["elevi"]
    profil = clasa_filtrata["profil"]
    elevi_cu_performante = [
        elev for elev in elevi_filtrati if "performante" in elev
    ]
    orar = f"orar{clasa}{litera}.PNG"
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
    search_query = request.args.get('search', '').lower()
    search_query_normalized = normalize_text(search_query)
    if search_query:
        profesori_filtrati = [
            profesor for profesor in profesori.personal
            if search_query_normalized in normalize_text(profesor["nume"]) or
               search_query_normalized in normalize_text(profesor["materie"])
        ]
    else:
        profesori_filtrati = profesori.personal
    return render_template(
        'profesori.html',
        profesori=profesori_filtrati,
        subtitlu="Corp Profesoral",
        title="Corp Profesoral",
        background="static/images/poze-hero/pozaprofesori.jpg"
    )

@app.route('/corp-profesoral/<nume>')
def pagina_profesor(nume):
    profesor = profesori.findbyname(nume)
    if profesor:
        return render_template('pagina_profesor.html', profesor=profesor, subtitlu=profesor["nume"], title=profesor["nume"], background="bgmain.png", no_hero=True)
    else:
        return "Profesorul nu a fost găsit.", 404

@app.route('/activitati')
def lista_activitati():
    return render_template(
        'activitati.html', 
        activitati=activitati,
        subtitlu="Activități", 
        title="Activități", 
        background="static/images/Poza-UMFST/grup9A/bgclasa9A.jpg"
    )

@app.route('/activitati/<id_activitate>')
def pagina_activitate(id_activitate):
    activitate = next((a for a in activitati if a["id"] == id_activitate), None)
    if not activitate:
        return f"Activitatea '{id_activitate}' nu a fost găsită.", 404

    
    hub_imagini = []
    if id_activitate == "mix-it-hub-umfst":
        hub_imagini = [
            "1-ipostazelefeminitatii.jpg",
            "2-visdeiarna.jpg",
            "3-1decembrie.jpg",
            "4-cufaruleminescu.jpg",
            "5-24ianuarie.jpg",
            "6-voluntariatcopiimici.jpg",
            "7-intalnirecucampioana.jpg",
            "8-voluntariatolimpbio.jpg"
        ]

    return render_template(
        activitate["template"],
        activitate=activitate,
        hub_imagini=hub_imagini,  
        subtitlu=activitate["titlu"],
        title=activitate["titlu"],
        no_hero=True,
    )

@app.route('/club/<club_name>')
def club_page(club_name):
    
    club = cluburi.get(club_name)
    if not club:
        return "Clubul nu a fost găsit.", 404
    return render_template(
        'club.html',
        titlu=club["titlu"],
        descriere=club["descriere"],
        coordonatori=club["coordonatori"],
        no_hero=True
    )

@app.route('/proiect/<proiect_name>')
def proiect_page(proiect_name):
   
    proiect = proiecte.get(proiect_name)
    if not proiect:
        return "Proiectul nu a fost găsit.", 404
    return render_template(
        'proiect.html',
        titlu=proiect["titlu"],
        subtitlu=proiect["subtitlu"],
        descriere=proiect["descriere"],
        no_hero=True
    )

@app.route('/celebrari/<celebrare_name>')
def celebrare_page(celebrare_name):
    

    
    celebrare = celebrari.get(celebrare_name)
    if not celebrare:
        return "Pagina pentru celebrarea solicitată nu a fost găsită.", 404

    
    return render_template(
        'celebrare.html',
        titlu=celebrare["titlu"],
        subtitlu=celebrare["subtitlu"],
        descriere=celebrare["descriere"],
        no_hero=True
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
@app.route('/developers')
def developari():
    return render_template('developers.html', title="Developers", subtitlu="developers", background="static/images/poze-hero/bgmain.png", no_hero=True)

@app.route('/corp-administrativ')
def corp_administrativ():
    return render_template(
        'administrativ.html',
        title="Corp Administrativ",
        subtitlu="Echipa Administrativă",
        background="static/images/poze-hero/Hero-principal.png"
    )

@app.route('/activitatiSub/echoReactor')
def echo_reactor():
    return render_template(
        'activitatiSub/echoReactor.html',
        title="Echo Reactor",
        subtitlu="Echo Reactor",
        no_hero=True
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")