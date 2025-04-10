import unicodedata

activitati = [
    {
        "id":1,
        "titlu": "Campania: Conversații în jurul școlii",
        "imagine": "BancaDinFata.jpg",
    },
    {
        "id":2,
        "titlu": "LyceumCloud.UMFST",
        "imagine": "BancaDinFata.jpg",
        "link": "#",
    },
    {
       "id":3,
        "titlu": "Banca din față",
        "imagine": "BancaDinFata.jpg",
        "link": "#",
    },
    {
        "id":4,
        "titlu": "Mix IT Hub UMFST – Centrul pasiunilor elevilor",
        "imagine": "BancaDinFata.jpg",
        "link": "#",
    },
    {
        "id":5,
        "titlu": "Campania: Conversații în jurul școlii",
        "imagine": "BancaDinFata.jpg",
        "link": "#",
    },
    {
        "id":6,
        "titlu": "Act4Change",
        "imagine": "BancaDinFata.jpg",
        "link": "#",
    },
    {
        "id":7,
        "titlu": "Porțile deschise ale liceului UMFST",
        "imagine": "BancaDinFata.jpg",
        "link": "#",
    },
]

anunturi = [
    {"titlu": "Anunț 1", "descriere": "Detalii despre anunțul 1.", "imagine": "bgmain.png"},
    {"titlu": "Anunț 2", "descriere": "Detalii despre anunțul 2.", "imagine": "bgmain.png"},
    {"titlu": "Anunț 3", "descriere": "Detalii despre anunțul 3.", "imagine": "bgmain.png"},
    {"titlu": "Anunț 4", "descriere": "Detalii despre anunțul 3.", "imagine": "bgmain.png"},
    {"titlu": "Anunț 5", "descriere": "Detalii despre anunțul 3.", "imagine": "bgmain.png"},
    {"titlu": "Anunț 6", "descriere": "Detalii despre anunțul 3.", "imagine": "bgmain.png"},
    {"titlu": "Anunț 7", "descriere": "Detalii despre anunțul 3.", "imagine": "bgmain.png"},

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
        "descriere": "",
        "citat": "Live. Love. Teach. Teaching hearts, shaping minds.",
        "imagine": "",
        "rol": "Conducere",
    },
    {
        "nume": "Kutasi Reka",
        "materie": "Limba engleză",
        "descriere": "",
        "citat": "",
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
        "descriere": "",
        "citat": "",
        "imagine": ""
    },
    {
        "nume": "Corneliu Tănase",
        "materie": "Biologie",
        "descriere": "",
        "citat": "",
        "imagine": ""
    },
    {
        "nume": "Georgeta Fodor",
        "materie": "Istorie",
        "descriere": "",
        "citat": "",
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
        "citat": "",
        "imagine": ""
    },
    {
        "nume": "Bârsan Ovidiu",
        "materie": "Religie",
        "descriere": "",
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
        "citat": "",
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
        "diriginte": "Crina Chirilă",
        "profil": "Științele Naturii",
        "citat": "Natura are un limbaj propriu și, dacă îi înțelegem semnele și ritmul, ne dezvăluie taine pe care nimic altceva nu le poate exprima",
        "elevi": [
            {"nume": "Bumbac Ileana"},
            {"nume": "Bumbu Luca"},
            {"nume": "Colcer Sonia"},
            {"nume": "Cosarca Alexandru"},
            {"nume": "Cotoi Iulius", "performante": [{"titlu": "Olimpiada Națională de Biologie","locatie": "Tg. Mureș, etapa județeană","premiu": "Mențiune 1" }]},
            {"nume": "Cretu Daria"},
            {"nume": "Crisan Andrei"},
            {"nume": "Dumitru Radu"},
            {"nume": "Florea Sara"},
            {"nume": "Florea Rares"},
            {"nume": "Gherman Eric"},
            {"nume": "Hanc Mihai"},
            {"nume": "Harsa Sofia"},
            {"nume": "Lazar Larisa"},
            {"nume": "Loghin Ioana","performante": [ {"titlu": "Olimpiada Națională de Limba Engleză","locatie": "Tg. Mureș, etapa județeană","premiu": "Premiul III"}]},
            {"nume": "Lupsa Maria"},
            {"nume": "Macarie Rares"},
            {"nume": "Orban David"},
            {"nume": "Onisor Rares"},
            {"nume": "Ormenisan Anastatia"},
            {"nume": "Popa Cynthia"},
            {"nume": "Sabau Raul"},
            {"nume": "Sandru Octavian"},
            {"nume": "Serbu Raluca"},
            {"nume": "Szasz Roberta", "performante" : [{"titlu": "Olimpiada Națională de Biologie", "locatie": "Tg. Mureș, etapa județeană", "premiu": "Premiul II"}, {"titlu": "Olimpiada Interdisciplinară „Culturalitate și spiritualitate românească“", "locatie": "Tg. Mureș, etapa județeană", "premiu": "Premiul III"}]},
            {"nume": "Vasiliu Anca"},
            {"nume": "Vidican Andreea"}
        ]
    },
    {
        "numar": 9,
        "litera": "A",
        "diriginte": "Roland Bolboacă",
        "profil": "Mate-Informatică",
        "citat": "Live. Love. Teach. Teaching hearts, shaping minds.",
        "elevi": [
            {"nume": "Biris Sergiu"},
            {"nume": "Corondeanu Raul"},
            {"nume": "Cucuiet Andrei"},
            {"nume": "Curta Rares"},
            {"nume": "David Aiana"},
            {"nume": "Ercean David"},
            {"nume": "Gherman Cezara"},
            {"nume": "Jovrea Stefan"},
            {"nume": "Lazar Cristian"},
            {"nume": "Maier Alia"},
            {"nume": "Marian Ciprian"},
            {"nume": "Mitoseriu David"},
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
            {"nume": "Oanes Sofia"},
            {"nume": "Paca Raoul"},
            {"nume": "Pantea Tudor"},
            {"nume": "Pastia Catinca"},
            {"nume": "Somesan Adrian"},
            {"nume": "Staicu Eric"},
            {"nume": "Stinga David"},
            {"nume": "Stoica Andrei"},
            {"nume": "Suciu Iustina"},
            {"nume": "Trifan Raul"},
            {"nume": "Turdean Cleo"},
            {"nume": "Ungur Filip"},
            {"nume": "Vasloban Maria"}
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

    # Testează funcția findbyname
    profesor = catalog.findbyname("Bogdan Rațu")
    if profesor:
        print(f"Profesor găsit: {profesor}")
    else:
        print("Profesorul nu a fost găsit.")

    clase = Clase(clase)
    for elev in clase.elevi_performante:
        print(elev["nume"])
    