import unicodedata

activitati = [
    {
        "id": "campania-conversatii-in-jurul-scolii",
        "titlu": "Campanii",
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
    "1-ipostazelefeminitatii.jpg",
    "2-visdeiarna.jpg",
    "3-1decembrie.jpg",
    "4-cufaruleminescu.jpg",
    "5-24ianuarie.jpg",
    "6-voluntariatcopiimici.jpg",
    "7-intalnirecucampioana.jpg",
    "8-voluntariatolimpbio.jpg"
]
anunturi = [
    {"titlu": "Ziua porților deschise", "descriere": "Detalii despre anunț.", "imagine": "anunt1.png"},
    {"titlu": "Anunț 2", "descriere": "Detalii despre anunț (În curând).", "imagine": "bgmain.png"},
    {"titlu": "Anunț 3", "descriere": "Detalii despre anunț (În curând).", "imagine": "bgmain.png"},
    {"titlu": "Anunț 4", "descriere": "Detalii despre anunț (În curând).", "imagine": "bgmain.png"},
    {"titlu": "Anunț 5", "descriere": "Detalii despre anunț (În curând).", "imagine": "bgmain.png"},
    {"titlu": "Anunț 6", "descriere": "Detalii despre anunț (În curând).", "imagine": "bgmain.png"},
    {"titlu": "Anunț 7", "descriere": "Detalii despre anunț (În curând).", "imagine": "bgmain.png"},

]

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
            "coordonatori": ["Kutasi Reka, Corina Bozedean"]
        },
        "sportiv": {
            "titlu": "Club de activități sportive",
            "descriere": "Numeroși elevi care iubesc mișcarea, competiția și un stil de viață sănătos au șansa de a se bucura de facilitățile pe care le oferă campusul universității. Este un loc în care nu contează doar performanța, ci și spiritul de echipă, fairplayul și bucuria de a fi activ. În funcție de talentul elevilor se oferă o varietate de activități pentru fiecare nivel de experiență.",
            "imagine": "static/images/cluburi/sportiv.jpg",
            "coordonatori": ["Răzvan Alexandrescu"]
        }
    }

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
        "descriere": "Dorința de a deveni profesoară a fost mereu parte din parcursul meu, o chemare pe care am urmat-o cu pasiune. De aceea, fiecare oră este pentru mine o aventură în lumea cuvintelor, a culturilor, dar și a descoperirii. Îmi place să transform lecțiile în experiențe vii, în care atmosfera caldă și degajată, curiozitatea și învățarea se îmbină armonios. Convingerea mea după mulți ani dedicați însușirii și predării limbilor străine este că acestea se predau foarte frumos dintr-un manual, dar ele se pot însuși și mai frumos dacă se trăiesc. Cum se pot trăi? Simplu: prin joc, conversație, film, muzică sau diverse proiecte creative. Mi-am dorit mereu să fiu acel tip de dascăl care nu doar transmite cunoștințe, ci și formează caractere, inspiră, încurajează, ghidează spiritul curios și deschis al elevilor.",
        "citat": "Cu cretă, umor și talent, predau cu zâmbet, nu cu accent!",
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
        "descriere": "Cred în puterea mișcării, în disciplină și în dezvoltarea caracterului prin sport. Ca profesor de educație fizică și antrenor, îmi doresc să inspir elevii să devină mai buni în fiecare zi – nu doar fizic, ci și mental. La liceul UMFST, vom învăța împreună să ne depășim limitele, să lucrăm în echipă și să nu renunțăm, indiferent de obstacole.",
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
        "diriginte": "Bogdan Rațiu",
        "profil": "Științele Naturii",
        "citat": "Trasăm linii care nu se șterg",
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
        "citat": "Prin respect, crești - pe tine și pe ceilalți.",
        "elevi": [
            {"nume": "Biriș Sergiu"},
            {"nume": "Corondeanu Raul",
             "performante": [
                {
                    "titlu": "Olimpiada Națională de Lb. Engleză",
                    "locatie": "Tulcea, etapa națională",
                    "premiu": "Participare"
                }
             ]},
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
            {"nume": "Paca Raoul",
             "performante": [
                {
                    "titlu": "Olimpiada Națională de Informatică",
                    "locatie": "Tg Mureș, etapa județeană",
                    "premiu": "Premiul III"
                }
            ]},
            {"nume": "Pantea Tudor"},
            {"nume": "Pastia Catinca"},
            {"nume": "Someșan Adrian"},
            {"nume": "Staicu Eric"},
            {"nume": "Stîngă David"},
            {"nume": "Stoica Andrei"},
            {"nume": "Suciu Iustina"},
            {"nume": "Trifan Raul"},
            {"nume": "Turdean Cleo",
             "performante": [
                {
                    "titlu": "Concursul național „Vis de iarnă”",
                    "locatie": "Baia Mare, etapa națională",
                    "premiu": "Premiul I"
                }
             ]},
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
