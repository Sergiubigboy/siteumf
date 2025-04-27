import unicodedata

activitati = [
    {
        "id": "campania-conversatii-in-jurul-scolii",
        "titlu": "Campania: Conversații în jurul școlii",
        "imagine": "activitati/campania.jpg",
        "template": "activitatiSub/campania.html"
    },
    {
        "id": "lyceumcloud-umfst",
        "titlu": "LyceumCloud.UMFST",
        "imagine": "activitati/lyceumcloud.jpg",
        "template": "activitatiSub/lyceumcloud-umfst.html"
    },
    {
        "id": "banca-din-fata",
        "titlu": "Banca din față",
        "imagine": "BancaDinFata.jpg",
        "template": "activitatiSub/banca-din-fata.html"
    },
    {
        "id": "mix-it-hub-umfst",
        "titlu": "Mix IT Hub UMFST – Centrul pasiunilor elevilor",
        "imagine": "BancaDinFata.jpg",
        "template": "activitatiSub/mix-it-hub-umfst.html"
    },
    {
        "id": "act4change",
        "titlu": "Act4Change",
        "imagine": "activitati/act4change.jpg",
        "template": "activitatiSub/act4change.html"
    },
    {
        "id": "echo-reactor",
        "titlu": "Echo Reactor",
        "imagine": "BancaDinFata.jpg",
        "template": "activitatiSub/echoReactor.html"
    }
]
hub_imagini = [
    "1-ipostazealefeminitatii.jpg",
    "2-visdeiarna.jpg",
    "3-1decembrie.jpg",
    "4-cufaruleminescu.jpg",
    "5-24ianuarie.jpg",
    "6-voluntariatcopiimici.jpg",
    "7-intalnirecucampioana.jpg",
    "8-voluntariatolimpbio.jpg"
]
anunturi = [
    {"titlu": "Anunț 1", "descriere": "Detalii despre anunțul 1 (În curând).", "imagine": "bgmain.png"},
    {"titlu": "Anunț 2", "descriere": "Detalii despre anunțul 2 (În curând).", "imagine": "bgmain.png"},
    {"titlu": "Anunț 3", "descriere": "Detalii despre anunțul 3 (În curând).", "imagine": "bgmain.png"},
    {"titlu": "Anunț 4", "descriere": "Detalii despre anunțul 4 (În curând).", "imagine": "bgmain.png"},
    {"titlu": "Anunț 5", "descriere": "Detalii despre anunțul 5 (În curând).", "imagine": "bgmain.png"},
    {"titlu": "Anunț 6", "descriere": "Detalii despre anunțul 6 (În curând).", "imagine": "bgmain.png"},
    {"titlu": "Anunț 7", "descriere": "Detalii despre anunțul 7 (În curând).", "imagine": "bgmain.png"},

]

profesori = [
    {
        "nume": "Bogdan Rațiu",
        "materie": "Limba și literatura română",
        "descriere": "Mereu mi-am dorit ca sala de curs să fie un spațiu în care cu toții să fim angrenați într-un exercițiu intelectual și într-un proces de formare. De aceea, îi provoc pe elevi să iasă din zona de confort și să-și descopere propria voce, îi îndrum să înțeleagă profund textele și să fie atenți la o expresie corectă. Sper că sunt un bun observator al emoțiilor și al nevoilor elevilor,  iar lecțiile să reprezinte un ghid în care se îmbină rigoarea științifică cu empatia profundă. În continuare, orele de Limba și literatura română vor fi un spațiu dinamic, cu idei, deschideri culturale vaste și multă reflecție. ",
        "citat": "Traim local, gandim global.",
        "imagine": "",
        "rol": "Conducere",

    },
    {
        "nume": "Nicola Oprea",
        "materie": "Matematică",
        "descriere": "",
        "citat": "",
        "imagine": "",


    },
    {
        "nume": "Bianca Han",
        "materie": "Limba engleză",
        "descriere": "Scriem împreună o filă nouă în cartea celor mai noi elevi ai celui mai nou liceu din Târgu-Mureș, Liceul UMFST „George Emil Palade”, liceul pe care ei l-au pus pe hartă ca fiind cel mai bun liceu din județ în urma rezultatelor la admitere. Să fii cel mai bun e greu, să rămâi cel mai bun e și mai greu, dar nu imposibil. Și asta vom demonstra noi împreună, pentru că acești tineri frumoși vor ajunge la stele.",
        "citat": "Live. Love. Teach. Teaching hearts, shaping minds.",
        "imagine": "",
        "rol": "Conducere",
    },
    {
        "nume": "Kutasi Reka",
        "materie": "Limba engleză",
        "descriere": "Sunt o persoană empatică, deschisă și dornică de a sprijini elevii în procesul lor de învățare și dezvoltare personală. Cred cu tărie că rolul unui dascăl nu se limitează doar la transmiterea cunoștințelor, ci implică și formarea unor oameni integri, capabili să gândească critic și să acționeze cu responsabilitate. Consider că fiecare elev are un potențial unic, iar rolul meu, ca profesor, este să îl descopăr, să îl cultiv și să îl susțin cu răbdare și implicare. Prin activitatea mea urmăresc să inspir, să încurajez și să contribui la dezvoltarea unei generații conștiente și bine pregătite pentru provocările lumii de mâine. ",
        "citat": "Educația este cea mai puternică armă pe  care o putem folosi pentru a schimba lumea. Nelson Mandela",
        "imagine": ""
    },
    {
        "nume": "Corina Bozedean",
        "materie": "Limba franceză",
        "descriere": "",
        "citat": "",
        "imagine": ""
    },
    {
        "nume": "Andreea-Romana Ban",
        "materie": "Limba germană",
        "descriere": "",
        "citat": "",
        "imagine": "",
        "rol": "Conducere",
    },
    {
        "nume": "Ioan Tușnea",
        "materie": "Fizică",
        "descriere": "",
        "citat": "",
        "imagine": ""
    },
    {
        "nume": "Mihai Babotă",
        "materie": "Chimie",
        "descriere": "Aflată la granița dintre știință, empirism și mister, chimia ne descoperă dincolo de reacții, formule și structuri esența proceselor care guvernează existența micro și macro universului, precum și modul în care omul poate trăi în echilibru cu el însuși și cu mediul înconjurător.Ca disciplină de studiu și știință exactă transpusă în cotidian, cred că ne explică faptul că \"E chimie între noi\" - parafrazând titlul unei melodii. Chimia e realitate frumoasă, plină de culoare și fascinație, pe care o trăim și o simțim în viața de zi cu zi.",
        "citat": "",
        "imagine": ""
    },
    {
        "nume": "Corneliu Tănase",
        "materie": "Biologie",
        "descriere": "În fiecare lecție de biologie se ascunde o poveste despre viață — despre echilibru, frumusețe, fragilitate și uimire. Ca profesor de biologie, cred că educația înseamnă să le trezești elevilor mirarea în fața vieții și să-i înveți să observe, să înțeleagă și să respecte lumea vie.",
        "citat": "Cunoașterea vieții ne învață să o prețuim.",
        "imagine": ""
    },
    {
        "nume": "Georgeta Fodor",
        "materie": "Istorie",
        "descriere": "Există o expresie celebră, “nu pentru școală ci pentru viața” care redă succint misiunea școlii și a profesorilor . Este ceea ce încerc să le transmit studenților mei, să îi conving ca școala este o experiență de învățare și nu o goană nebună după cat mai multe note de 10. Nu trebuie să facem parada cu ceea ce știm ci să acumulăm pentru a pune în practică, pentru a deveni cea mai bună versiune a noastră. O astfel de abordare presupune a renunța la “marșul triumfal spre “a termina materia” la sfârșit de an. Nu cred ca este relevant cât putem memora ci cum ceea ce acumulăm ne transformă, ne bucura, ne determină să vrem mai mult. Ca om și ca profesor sunt la fel! Îmi place să descopăr lucruri noi, învăț permanent, citesc și cred în puterea magică a cărților, mă respect și îi respect pe toți cei din jurul meu!",
        "citat": "Nu pentru școală ci pentru viața",
        "imagine": ""
    },
    {
        "nume": "Crina Chirilă",
        "materie": "Geografie",
        "descriere": "De mică, am fost pasionată de explorarea lumii și de înțelegerea fenomenelor naturale, iar din pasiune mi-am creat o profesie. Ca profesoară de geografie încerc sa deschid orizonturi noi pentru elevii mei, transformând hărțile în povești. Geografia este una dintre disciplinele care ne creează „conștiința eco”, iar pentru a nu face rău lumii din jur avem nevoie să înțelegem dinamica pământului și modul în care timpul ne-a construit din adâncul oceanelor în vârful munților. Sper ca fiecare lecție să-i ajute pe elevi să cunoască lumea și să le ofere șansa de a-și găsi un loc în ea.",
        "citat": " Natura are un limbaj propriu și, dacă îi înțelegem semnele și ritmul, ne dezvăluie taine pe care nimic altceva nu le poate exprima",
        "imagine": ""
    },
    {
        "nume": "Nora Dumbravă",
        "materie": "Logică",
        "descriere": " ",
        "citat": "Să înveți fără să gândești este fără sens; să gândești fără să înveți este periculos. - Confucius",
        "imagine": ""
    },
    {
        "nume": "Bârsan Ovidiu",
        "materie": "Religie",
        "descriere": "Cred în miracolul terapeutic al bucuriei, al zâmbetului și al lacrimii. De aici convingerea că zâmbim ca să nu murim și plângem ca să înviem. Am pariat pe capacitatea omului de a câștiga meciul cu el însuși, sub asistența harului divin, pentru a deveni un adevărat selecționer de valori culturale și spirituale. De altminteri, perena educație începe și dăinuie printr-un arest al autosuficienței, pur și simplu.Dar mai presus de toate, cred că existăm ca să iubim și iubind vom birui oriunde.",
        "citat": "",
        "imagine": ""
    },
    {
        "nume": "Bogdan Bucur",
        "materie": "Educație vizuală",
        "descriere": "",
        "citat": "",
        "imagine": ""
    },
    {
        "nume": "Răzvan Alexandrescu",
        "materie": "Educație fizică",
        "descriere": "",
        "citat": "Cred în puterea mișcării, în disciplină și în dezvoltarea caracterului prin sport. Ca profesor de educație fizică și antrenor, îmi doresc să inspir elevii să devină mai buni în fiecare zi – nu doar fizic, ci și mental. La liceul UMFST, vom învăța împreună să ne depășim limitele, să lucrăm în echipă și să nu renunțăm, indiferent de obstacole.",
        "imagine": ""
    },
    {
        "nume": "Jeddi Tünde",
        "materie": "Educație muzicală",
        "descriere": "",
        "citat": "",
        "imagine": ""
    },
    {
        "nume": "Roland Bolboacă",
        "materie": "Informatică",
        "descriere": "",
        "citat": "",
        "imagine": ""
    },
     {
        "nume": " Feier Adrian",
        "materie": "Informatică",
        "descriere": "",
        "citat": "",
        "imagine": ""
    }
]



clase = [
    {
        "numar": 9,
        "litera": "B",
        "diriginte": "Bogdan Rațiu",
        "profil": "Științele Naturii",
        "citat": "",
        "elevi": [
            {"nume": "Bumbac Ileana"},
            {"nume": "Bumbu Luca"},
            {"nume": "Colcer Sonia"},
            {"nume": "Coșarcă Alexandru"},
            {"nume": "Cotoi Iulius", "performante": [{"titlu": "Olimpiada Națională de Biologie","locatie": "Tg. Mureș, etapa județeană","premiu": "Mențiune 1" }]},
            {"nume": "Crețu Daria"},
            {"nume": "Crișan Andrei"},
            {"nume": "Dumitru Radu"},
            {"nume": "Florea Sara"},
            {"nume": "Florea Rareș"},
            {"nume": "Gherman Eric"},
            {"nume": "Hanc Mihai"},
            {"nume": "Harșa Sofia"},
            {"nume": "Lazăr Larisa"},
            {"nume": "Loghin Ioana","performante": [ {"titlu": "Olimpiada Națională de Limba Engleză","locatie": "Tg. Mureș, etapa județeană","premiu": "Premiul III"}]},
            {"nume": "Lupșa Maria"},
            {"nume": "Macarie Rareș"},
            {"nume": "Orban David"},
            {"nume": "Onisor Rares"},
            {"nume": "Ormenișan Anastasia"},
            {"nume": "Popa Cynthia"},
            {"nume": "Sabău Raul"},
            {"nume": "Șandru Octavian"},
            {"nume": "Șerbu Raluca"},
            {"nume": "Szasz Roberta", "performante" : [{"titlu": "Olimpiada Națională de Biologie", "locatie": "Tg. Mureș, etapa județeană", "premiu": "Premiul II"}, {"titlu": "Olimpiada Interdisciplinară „Culturalitate și spiritualitate românească“", "locatie": "Tg. Mureș, etapa județeană", "premiu": "Premiul III"}]},
            {"nume": "Vasiliu Anca"},
            {"nume": "Vidican Andreea"}
        ]
    },
    {
        "numar": 9,
        "litera": "A",
        "diriginte": "Bianca Han",
        "profil": "Mate-Informatică",
        "citat": "",
        "elevi": [
            {"nume": "Biriș Sergiu"},
            {"nume": "Corondeanu Raul"},
            {"nume": "Cucuiet Andrei"},
            {"nume": "Curta Rares"},
            {"nume": "David Aiana"},
            {"nume": "Ercean David"},
            {"nume": "Gherman Cezara"},
            {"nume": "Jovrea Ștefan"},
            {"nume": "Lazăr Cristian"},
            {"nume": "Maier Alia"},
            {"nume": "Marian Ciprian"},
            {"nume": "Mitoșeriu David"},
            {"nume": "Muth Cristian",
              "performante": [
            {
                "titlu": "Concursul Interjudețean Alexandru Papiu Ilarian",
                "locatie": "",
                "premiu": "Premiul II"
            },
            {
                "titlu": "Concursul Interdisciplinar de Matematică și Fizică „Vranceanu-Procopiu“",
                "locatie": "Bacău, etapa națională",
                "premiu": "Mențiune"
            },
            {
                "titlu": "Concursul „Prin Labirintul Matematicii“",
                "locatie": "Baia Mare",
                "premiu": "Premiul I, cu punctaj maxim"
            },
            {
                "titlu": "Concursul „Matematica de drag“",
                "locatie": "Bistrița Năsăud",
                "premiu": "Mențiune"
            },
            {
                "titlu": "Concursul „Marian Țarina“",
                "locatie": "Cluj Napoca",
                "premiu": "Premiul III"
            },
            {
                "titlu": "Concursul „Argument“",
                "locatie": "Baia Mare",
                "premiu": "Premiul I"
            },
            {
                "titlu": "Concursul Național de Matematică și Informatică „Grigore Moisil“",
                "locatie": "Cluj Napoca",
                "premiu": "Premiul II"
            },
            {
                "titlu": "Olimpiada Județeană de Matematică",
                "locatie": "Botoșani",
                "premiu": "Premiul II și calificare la națională"
            },
            {
                "titlu": "Olimpiada Județeană de Fizică",
                "locatie": "Slobozia",
                "premiu": "Premiul I și calificare la etapa națională"
            }
        ]},
            {"nume": "Nagy Eliz", 
             "performante": [
            {
                "titlu": "Convocare Lotul Național U16",
                "locatie": "Bulgaria, Sofia",
                "premiu": "Participare la Turul 1 de calificare pentru Turneul final al Campionatului European"
            },
            {
                "titlu": "Campionat Național volei U19",
                "locatie": "Timișoara",
                "premiu": "Locul I, Etapa semifinală"
            },
            {
                "titlu": "Calificare turneu final U19 Campionat Național",
                "locatie": "Ediția 2024/2025",
                "premiu": "Cele mai bune 6 echipe din țară"
            },
            {
                "titlu": "Calificare turneu final Cupa României U19",
                "locatie": "Ediția 2024/2025",
                "premiu": "Cele mai bune 8 echipe"
            },
            {
                "titlu": "Convocare Lotul Național U16",
                "locatie": "Slovenia, Maribor",
                "premiu": "Participare la Turul 2 de calificare pentru Turneul final al Campionatului European"
            },
            {
                "titlu": "Calificare turneu final de promovare Divizia A1",
                "locatie": "Liga I senioare, ediția 2024/2025",
                "premiu": ""
            }
        ]},
            {"nume": "Oaneș Sofia"},
            {"nume": "Paca Raoul"},
            {"nume": "Pantea Tudor"},
            {"nume": "Pastia Catinca"},
            {"nume": "Someșan Adrian"},
            {"nume": "Staicu Eric"},
            {"nume": "Stîngă David"},
            {"nume": "Stoica Andrei"},
            {"nume": "Suciu Iustina"},
            {"nume": "Trifan Raul"},
            {"nume": "Turdean Cleo"},
            {"nume": "Ungur Filip"},
            {"nume": "Vașloban Maria"}
        ]
    }
]

def normalize_text(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    ).lower()

class Profesori:
    def __init__(self, personal):
        self.personal = personal
        for pers in self.personal:
            pers['imagine'] = normalize_text(pers['nume'].replace(" ", "-").lower() + ".jpg")



    def findbyname(self, nume):
        return next((prof for prof in self.personal if prof["nume"] == nume), None)

    def findbykey(self, materie, cheie):
        return [prof for prof in self.personal if prof[cheie] == materie]

class Clase:
    def __init__(self, clase):
        self.clase = clase
        self.elevi_performante = []
        for clasa in self.clase:
            for elev in clasa["elevi"]:
                if "performante" in elev:
                    self.elevi_performante.append(elev)

    def findbykey(self, cheie, valoare):
        return [cls for cls in self.clase if cls[cheie] == valoare]

if __name__ == "__main__":
    catalog = Profesori(profesori)

    profesor = catalog.findbyname("Bogdan Rațu")
    if profesor:
        print(f"Profesor găsit: {profesor}")
    else:
        print("Profesorul nu a fost găsit.")

    clase = Clase(clase)
    for elev in clase.elevi_performante:
        print(elev["nume"])
