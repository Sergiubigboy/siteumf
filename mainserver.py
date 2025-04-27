from flask import Flask, render_template, request
from date import Profesori, Clase, profesori, clase, normalize_text, anunturi, activitati
import unicodedata

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
        background="static/images/poze-hero/bgmain.png",
    )

@app.route('/club/<club_name>')
def club_page(club_name):
    cluburi = {
        "teatru": {
            "titlu": "Club de teatru",
            "descriere": "Alături de Teatrul „Scena” din Târgu Mureș elevii Liceului UMFST „George Emil Palade” au parte de un atelier de actorie și de dezvoltare personală prin teatru. Atelierul este coordonat de actorul Liviu Pancu și le oferă elevilor Liceului UMFST oportunitatea de a-și îmbunătăți abilitățile de comunicare și vorbire în public, de a-și gestiona emoțiile și de a-și folosi creativitatea și imaginația într-un mod constructiv.",
            "imagine": "static/images/activitati/club/teatru.jpg",
            "coordonatori": ["Liviu Pancu"]
        },
        "dezbateri": {
            "titlu": "Club de dezbateri",
            "descriere": "Atelierul este dedicat elevilor pasionați de idei, curioși, dornici să-și dezvolte gândirea critică și abilitățile de comunicare. În fiecare săptămână ne propunem să construim argumente solide, să analizăm perspective diferite și să ne exprimăm convingător asupra unor subiecte actuale.",
            "imagine": "static/images/cluburi/dezbateri.jpg",
            "coordonatori": ["Bogdan Rațiu"]
        },
        "robotica": {
            "titlu": "Club de robotică",
            "descriere": "Elevii pasionați de tehnologie, de soluții inteligente, au șansa de a participa la acest atelier în care imaginația se întâlnește cu știința, iar treptat ideile prin formă prin fire, senzori și cod. Liceenii lucrează în echipe pentru a proiecta, construi și programa roboți, iar clubul îți oferă șansa de a crea și de a concura în competiții locale și naționale.",
            "coordonatori": [""]
        },
        "muzica": {
            "titlu": "Club de muzică",
            "descriere": "Clubul de muzică încearcă să răspundă dorinței elevilor de a-și cultiva pasiunea pentru artă. Nu e vorba de un singur gen de muzică, pentru că elevii noștri au oportunitatea de a cânta atât în trupa școlii, cât și în concerte alături de Orchestra UMFST.",
            "imagine": "static/images/muzica.jpg",
            "coordonatori": [""]
        },
        "public-speaking": {
            "titlu": "Club de public speaking",
            "descriere": "La acest club alături de profesorii care predau limbi străine învățăm să transformăm emoțiile în energie și ideile în discursuri persuasive. Se realizează activități practice pornind din discursuri tematice, precum și exerciții de dicție și de retorică.",
            "imagine": "static/images/cluburi/public-speaking.jpg",
            "coordonatori": ["Bianca Han", "Andreea Ban"]
        },
        "sportiv": {
            "titlu": "Club de activități sportive",
            "descriere": "Numeroși elevi care iubesc mișcarea, competiția și un stil de viață sănătos au șansa de a se bucura de facilitățile pe care le oferă campusul universității. Este un loc în care nu contează doar performanța, ci și spiritul de echipă, fairplayul și bucuria de a fi activ. În funcție de talentul elevilor se oferă o varietate de activități pentru fiecare nivel de experiență.",
            "imagine": "static/images/cluburi/sportiv.jpg",
            "coordonatori": ["Răzvan Alexandrescu"]
        }
    }
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
    proiecte = {
        "bookflix": {
            "titlu": "Bookflix",
            "subtitlu": "Descoperă lumea fascinantă a cărților prin Bookflix!",
            "descriere": "Bookflix este o activitate complexă, care combină lectura în limba străină cu dezvoltarea si valorificarea abilităților digitale și de comunicare ale elevilor. Astfel, elevii reușesc să pună în scenă „digital skills” și „soft skills”, pornind de la lectura unei cărți în limba engleză.",
        },
        "saptamana-lecturii": {
            "titlu": "Săptămâna lecturii",
            "subtitlu": "Un eveniment dedicat promovării lecturii și literaturii.",
            "descriere": """
            <p>În perioada 10-16 februarie 2025, elevii Liceului UMFST celebrează lectura printr-o serie de activități speciale, menite să aducă mai aproape pasiunea pentru cărți și să încurajeze cititul în comunitate.</p>
            <p><strong>Cititori contra timp</strong><br>
            Pe tot parcursul săptămânii, elevii vor promova lectura pe rețelele sociale prin materiale video și mesaje puternice despre impactul cărților în viața lor. Vă invităm să îi urmăriți pe pagina administrată de elevi, @boboci_liceul_umfst.</p>
            <p><strong>Secretul din cărți (12 februarie)</strong><br>
            O activitate interactivă de tip vânătoare de comori, unde elevii vor descoperi titluri valoroase din patrimoniul cultural.</p>
            <p><strong>Cursa cărților (10-14 februarie)</strong><br>
            Membrii comunității academice UMFST sunt invitați să doneze cărți, între 10 și 13 februarie, în spațiul special amenajat la parterul clădirii principale a universității (holul liceului). Pe 14 februarie, elevii vor porni cu entuziasm într-o călătorie prin Târgu Mureș, unde vor oferi cărțile colectate comunității locale, încurajând astfel lectura.</p>
            <p><strong>Workshop didactic (15 februarie)</strong><br>
            Evenimentul care încheie săptămâna va fi dedicat cadrelor didactice din învățământul primar. Asist. univ. dr. Bogdan Rațiu va susține workshopul „Lectură literară vs. Literație?”, în care vor fi prezentate strategii de lectură și literație aplicabile la clasă.</p>
            """,

        },
        "vis-de-iarna": {
            "titlu": "Vis de iarnă",
            "subtitlu": "Un proiect magic pentru a sărbători frumusețea iernii.",
            "descriere": "În colaborare cu Palatul Copiilor din Baia Mare:  proiectul educațional național „Vis de iarnă”, la care au participat și elevii Liceului UMFST „George Emil Palade” din Târgu Mureș. Proiectul a avut patru secțiuni: concursul de creații literare cu tema „Iarna de odinioară versus iarna actuală”, ateliere de arte plastice și lucrări tridimensionale și concursul de interpretare vocală – colinde tradiționale. În data de 9 decembrie a avut loc și spectacolul de colinde „Vis de iarnă”.",

        }
    }
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
    celebrari = {
        "1-decembrie": {
    "titlu": "Ziua de 1 Decembrie",
    "subtitlu": "Ziua Națională a României",
    "descriere": """
    <p>Elevii și profesorii Liceului UMFST „George Emil Palade” au sărbătorit împreună Ziua Națională a României.</p>
    
    <p>Mână-n mână s-au creat proiecte despre Unire și despre România.</p>
    
    <p>Mână de la mână s-au strâns pe masă bunătăți tradiționale românești.</p>
    
    <p>Mână de mână ne-am prins în horă să ne bucurăm de Ziua Națională a României.</p>
    """,
    "imagine": "static/images/celebrari/1-decembrie.jpg"
},
        "mica-unire": {
            "titlu": "Mica Unire - 24 Ianuarie",
            "subtitlu": "Unirea Principatelor Române",
            "descriere": """
            <p>Mica Unire a fost sărbătorită la Liceul UMFST „George Emil Palade” printr-o altfel de oră de istorie susținută de conf. univ. dr. Georgeta Fodor. Cadrele didactice și elevii au încercat să reconstituie și să înțeleagă emoția și entuziasmul dublei alegeri a lui Alexandru Ioan Cuza prin sondarea și interpretarea unor surse istorice. Elevii celor două clase au devenit pentru o oră reprezentanți ai moldovenilor și muntenilor care au decis, „ad hoc”, alegerea aceluiași conducător. La final, elevii au reconstituit atmosfera alegerii lui Cuza pe baza operei de artă semnată de Theodor Aman: „Proclamarea Unirii (24 Ianuarie 1859)”. Activitatea este parte a inițiativelor coordonate de cadrele didactice ale Liceului UMFST „George Emil Palade” cu scopul de a le oferi elevilor repere fundamentale necesare devenirii lor ca cetățeni activi și conștienți de importanța implicării civice.</p>
            """,
            "imagine": "static/images/celebrari/mica-unire.jpg"
        },
        "ziua-culturii-nationale": {
            "titlu": "Ziua Culturii Naționale",
            "subtitlu": "Sărbătoarea culturii românești",
            "descriere": """
            <p>Ziua Culturii Naționale a fost sărbătorită la UMFST G.E. Palade Târgu Mureș miercuri, 15 ianuarie 2025, între orele 10:00 – 12:00, în Aula Magna (str. Nicolae Iorga), printr-un eveniment care îl va omagia pe poetul „nepereche” al românilor, Mihai Eminescu, și va pune în lumină aspecte valoroase din patrimoniul nostru cultural.
Prin coordonarea cadrelor didactice de la Facultatea de Științe și Litere „Petru Maior”, studenți și masteranzi ai facultății, alături de elevi de la Liceul UMFST „George Emil Palade”, au dat dovada talentului, implicării și inocenței lor.
Evenimentul a avut momente de recitări din poeziile eminesciene în limba română și traduse în limbi străine, momente de interpretare vocală și instrumentală din compozitori români, prezentarea unui videoclip cu un „tezaur uman” - meșter popular din județul Mureș, iar ca încununare a momentului artistic vor fi purtate cu mândrie cămăși naționale, iile cusute de un cadru didactic din universitate. Semnificația profundă a manifestării va fi expusă de cadre didactice
</p>
            """,
            "imagine":None
        },
        "ziua-cititului-impreuna": {
            "titlu": "Ziua Cititului Împreună",
            "subtitlu": "Istoria prin obiecte tangibile. Cufărul poetului Mihai Eminescu Cufărul lui Eminescu la Muzeul UMFST",
            "descriere": """
            <p>Muzeul Universității „George Emil Palade” are onoarea de a găzdui un obiect cu o profundă valoare istorică și culturală: cufărul lui Mihai Eminescu. Renumitul cufăr, marcat pe placheta centrală cu inscripția „M. Eminovici”, l-a însoțit pe Eminescu de-a lungul întregii sale vieți, devenind martor al călătoriilor sale prin țară și Europa încă din copilărie. În cadrul evenimentului cultural „Istoria prin obiecte tangibile. Cufărul poetului Mihai Eminescu”, care a avut loc în data de 5 februarie 2025, când a fost sărbătorită Ziua Internațională a Cititului Împreună, cei prezenți au avut ocazia să admire cufărul și să descopere povestea din spatele acestuia, dar și să participe la un moment special pregătit de elevii Liceului UMFST „George Emil Palade”. </p>
            """,
            "imagine": None
        }
    }

    
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
    return render_template('developers.html', title="Developers", subtitlu="developers", background="static/images/poze-hero/bgmain.png")

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