import unicodedata

anunturi = [
    {"titlu": "Anunț 1", "descriere": "Detalii despre anunțul 1."},
    {"titlu": "Anunț 2", "descriere": "Detalii despre anunțul 2."},
    {"titlu": "Anunț 3", "descriere": "Detalii despre anunțul 3."},
    {"titlu": "Anunț 4", "descriere": "Detalii despre anunțul 3."},
    {"titlu": "Anunț 5", "descriere": "Detalii despre anunțul 3."},
    {"titlu": "Anunț 6", "descriere": "Detalii despre anunțul 3."},
    {"titlu": "Anunț 7", "descriere": "Detalii despre anunțul 3."},

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



elevi = [
    # Clasa 9B
    {"nume": "Bumbac Ileana", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Bumbu Luca", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Colcer Sonia", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Cosarca Alexandru", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Cotoi Iulius", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Cretu Daria", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Crisan Andrei", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Dumitru Radu", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Florea Sara", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Florea Rares", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Gherman Eric", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Hanc Mihai", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Harsa Sofia", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Lazar Larisa", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Loghin Ioana", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Lupsa Maria", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Macarie Rares", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Orban David", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Onisor Rares", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Ormenisan Anastatia", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Popa Cynthia", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Sabau Raul", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Sandru Octavian", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Serbu Raluca", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Szasz Roberta", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Vasiliu Anca", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},
    {"nume": "Vidican Andreea", "clasa": 9, "litera": "B", "profil": "Științele Naturii"},

    # Clasa 9A
    {"nume": "Biris Sergiu", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Corondeanu Raul", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Cucuiet Andrei", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Curta Rares", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "David Aiana", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Ercean David", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Gherman Cezara", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Jovrea Stefan", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Lazar Cristian", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Maier Alia", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Marian Ciprian", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Mitoseriu David", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Muth Cristian", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Nagy Eliz", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Oanes Sofia", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Paca Raoul", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Pantea Tudor", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Pastia Catinca", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Somesan Adrian", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Staicu Eric", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Stinga David", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Stoica Andrei", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Suciu Iustina", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Trifan Raul", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Turdean Cleo", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Ungur Filip", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"},
    {"nume": "Vasloban Maria", "clasa": 9, "litera": "A", "profil": "Mate-Informatică"}
]

def normalize_text(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    ).lower()

class CatalogPersonal:
    def __init__(self, personal):
        self.personal = personal
        for pers in self.personal:
            pers['imagine'] = normalize_text(pers['nume'].replace(" ", "-").lower() + ".jpg")



    def findbyname(self, nume):
        return next((prof for prof in self.personal if prof["nume"] == nume), None)

    def findbykey(self, materie, cheie):
        return [prof for prof in self.personal if prof[cheie] == materie]


if __name__ == "__main__":
    catalog = CatalogPersonal(profesori)

    # Testează funcția findbyname
    profesor = catalog.findbyname("Jeddi Tunde")
    if profesor:
        print(f"Profesor găsit: {profesor}")
    else:
        print("Profesorul nu a fost găsit.")