
profesori = [
    {
        "nume": "Bogdan Rațiu",
        "materie": "Limba și literatura română",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Nicola Oprea",
        "materie": "Matematică",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Bianca Han",
        "materie": "Limba engleză",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Kutasi Réka",
        "materie": "Limba engleză",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Corina Bozedean",
        "materie": "Limba franceză",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Andreea-Romana Ban",
        "materie": "Limba germană",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Ioan Tușnea",
        "materie": "Fizică",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Mihai Babotă",
        "materie": "Chimie",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Corneliu Tanase",
        "materie": "Biologie",
        "descriere": "",
        "imagine": "images/Corneliu-Tanase.png"
    },
    {
        "nume": "Georgeta Fodor",
        "materie": "Istorie",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Crina Chirilă",
        "materie": "Geografie",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Nora Dumbravă",
        "materie": "Logică",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Barsan",
        "materie": "Religie",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Bogdan Bucur",
        "materie": "Educație vizuală",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Răzvan Alexandrescu",
        "materie": "Educație fizică",
        "descriere": "",
        "imagine": ""
    },
    {
        "nume": "Jeddi Tunde",
        "materie": "Educație muzicală",
        "descriere": "",
        "imagine": ""
    }
]

class CatalogPersonal:
    def __init__(self, personal):
        self.personal = personal
        
    def findbyname(self, nume):
        return next((prof for prof in self.personal if prof["nume"] == nume), None)

    def findbysubject(self, materie):
        return [prof for prof in self.personal if prof["materie"] == materie]


if __name__ == "__main__":
    catalog = CatalogPersonal(profesori)

    # Testează funcția findbyname
    profesor = catalog.findbyname("Jeddi Tunde")
    if profesor:
        print(f"Profesor găsit: {profesor}")
    else:
        print("Profesorul nu a fost găsit.")

    # Testează funcția findbysubject
    profesori_engleza = catalog.findbysubject("Limba engleză")
    print(f"Profesori de Limba engleză: {profesori_engleza}")