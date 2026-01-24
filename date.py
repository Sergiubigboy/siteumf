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
    "8-voluntariatolimpbio.jpg",
    "atelier.jpeg",
    "bookflix.jpg",
    "club-de-muzica.jpg",
    "culturii.jpeg",
    "debateexpress.jpeg",
    "empatia.jpeg",
    "heropodcast.jpg",
    "pozecarti.jpeg",
    "prezentare.jpeg",
    "prislop.jpeg",
    "sapt-lecturii.jpg",
    "voleisport.jpeg"
]
anunturi = [
    {"titlu": "Depunere dosare înscriere", "descriere": "24-29 iulie", "imagine": "anunt.jpg"},

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
            <p>Muzeul Universității „George Emil Palade” are onoarea de a găzdui un obiect cu o profundă valoare istorică și culturală: cufărul lui Mihai Eminescu. Renumitul cufăr, marcat pe placheta centrală cu inscripția „M. Eminovici”, l-a însoțit pe Eminescu de-a lungul întregii sale vieți, devenind martor al călătoriilor sale prin țară și Europa încă din copilărie. </p>
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
            "titlu": "Paideia - club de dezbateri și oratorie",
            "descriere": "Numele clubului, Paideia, provine din cultura greacă antică și desemnează idealul formării integrale a omului prin educație, cultură și dialog. Alegerea acestui nume reflectă convingerea că dezbaterea și arta discursului sunt instrumente esențiale pentru dezvoltarea rațiunii, a caracterului și a spiritului civic.\nClubul Paideia are misiunea de a sprijini elevii să își dezvolte gândirea critică, exprimarea clară și responsabilă, respectul față de diversitatea opiniilor și capacitatea de a construi argumente solide. Obiectivele principale sunt:\n- dezvoltarea competențelor de argumentare, retorică și public speaking;\n- promovarea unei culturi a dialogului bazată pe respect, toleranță și fair-play;\n- participarea constantă la competiții de dezbateri și de public speaking la nivel local, național și internațional;\n- formarea unor atitudini morale și civice prin implicarea activă în activitățile clubului;\n- dezvoltarea capacității de a aborda teme interdisciplinare și actuale, prin documentare riguroasă;\n- cultivarea toleranței față de pluralismul opiniilor și a deschiderii către perspective diverse.\nActivitatea clubului include ateliere de public speaking și oratorie, sesiuni de dezbateri academice pe teme interdisciplinare, pregătirea echipelor pentru competiții și organizarea unor evenimente de tip „dialog socratic” sau mini-dezbateri interne. Elevii vor fi încurajați să participe în mod constant la concursuri de dezbateri și de oratorie înscrise în calendarele naționale și internaționale, reprezentând liceul cu profesionalism și responsabilitate.\nPrin pregătirea dezbaterilor, elevii sunt motivați să realizeze documentări temeinice, dobândind astfel cunoștințe variate și actuale din domenii diverse – social, cultural, economic și politic. Susținerea pledoariilor în fața publicului contribuie la formarea abilităților de oratorie și retorică, dar și la consolidarea spiritului de echipă.\nImpactul clubului Paideia se reflectă atât la nivelul dezvoltării personale a elevilor, cât și în comunitatea școlară. Elevii participanți dobândesc competențe de comunicare, gândire critică și cooperare, iar profesorii și părinții beneficiază indirect prin implicarea elevilor în activități de calitate. Comunitatea locală are, la rândul ei, de câștigat prin formarea unor tineri capabili să abordeze cu responsabilitate problemele lumii contemporane.",
            "imagine": "static/images/cluburi/dezbateri.jpg",
            "coordonatori": ["Briena Stoica, Bogdan Rațiu"]
        },
        "robotica": {
            "titlu": "Club de robotică",
            "descriere": "Robotica, alături de disciplinele Informatică și TIC, Matematică și Fizică, recomandă dezvoltarea competenţelor STEM (Știință, Tehnologie, Inginerie și Matematică) cu un caracter transdisciplinar.\nClubul de robotică este locul unde elevii pasionați de tehnologie pot învăța să construiască și să programeze roboți. Este o oportunitate excelentă de a dezvolta abilități tehnice și de a lucra în echipă.\nObiectivele principale sunt:\nformarea competenţelor de utilizare transdisciplinară și a achizițiilor din Fizică, Matematică, Informatică și TIC,\ndezvoltarea creativităţii tehnice, a gândirii logice şi a gândirii algoritmice, a competenţelor de modelare, algoritmizare şi programare a algoritmilor \ndezvoltarea unor capacităţi de cercetare şi de creaţie tehnică.\nAtingerea acestor scopuri se realizează prin conceperea şi asamblarea modelelor de roboţi şi elaborarea de algoritmi şi programe de conducere.\nPrin studiul roboților, elevii pot dobândi achiziții de învățare relevante pentru domeniile: Inginerie, Tehnologie, Știința sistemelor și materialelor mecanice, electronice și sisteme electrice, concepte de programare și matematică aplicată. De asemenea, își formează abilități de muncă în echipă, leadership și rezolvarea problemelor. Activitățile de învățare propuse pot fi realizate în mod real cu ajutorul unor kit-uri achiziționate, sau într-un mediu de programare online, care permite programarea roboților. Prin intermediul a două proiecte (Fondul Științescu Mureș și proiect intern UMFST) au fost achiziționate kituri de electronica prin programare nivel începător și intermediar, kit-uri de Energie Verde (Casă Smart, Panou Solar, irigații plante) respectiv kit-uri de mașină robot, toate echipate cu mai mulți senzori electronici, și comandate prin sisteme Arduino. \nNe propunem, deasemenea participarea la Concursuri de Robotică atât la nivel local (intern UMFST și în colaborare cu alte licee) cât și la nivel national (ex. Nextlab).",
            "coordonatori": ["Papp Botond, Peres Gyula"]
        },
        "muzica": {
            "titlu": "Club de muzică",
            "descriere": "Clubul de muzică încearcă să răspundă dorinței elevilor de a-și cultiva pasiunea pentru artă. Nu e vorba de un singur gen de muzică, pentru că elevii noștri au oportunitatea de a cânta atât în trupa școlii, cât și în concerte alături de Orchestra UMFST.",
            "imagine": "static/images/muzica.jpg",
            "coordonatori": [""]
        },
        "lectura": {
            "titlu": "Club de lectură",
            "descriere": "Clubul de lectură este un spațiu de întâlnire în jurul textului. Nu este un loc al răspunsurilor „corecte”, ci al interpretărilor argumentate și al bucuriei de a gândi împreună. Textele sunt citite atent, discutate în profunzime și puse în relație cu experiențele de viață ale participanților, cu alte texte, cu idei din cultură, filosofie sau știință. Accentul cade pe sens, pe felul în care literatura ne ajută să ne înțelegem pe noi înșine și lumea.\nActivitățile clubului includ:\ncercuri de lectură bazate pe discuție liberă, ghidată de întrebări deschise;\ninterpretarea textelor literare și nonliterare din perspective diferite;\nformularea și susținerea punctelor de vedere prin argumente;\ndialog între cititori, nu evaluare sau ierarhizare;\nconexiuni între texte și realitatea contemporană;\nexerciții de lectură reflexivă și scriere de reacție (jurnale de lectură, fragmente eseistice, note personale);\ndescoperirea plăcerii lecturii ca act intelectual și emoțional.\nClubul pune accent pe:\ncititorul ca partener de dialog, nu ca simplu receptor;\nrespectul față de opiniile diferite;\nascultarea activă și capacitatea de a construi sens împreună;\ndezvoltarea gândirii critice și a expresivității personale.\nClubul de lectură este, în esență, o comunitate de cititori care cred că lectura bună se trăiește împreună și că sensul se construiește în dialog.",
            "imagine": "",
            "coordonatori": ["Bogdan Rațiu"]
        },
        "sportiv": {
            "titlu": "Club de activități sportive",
            "descriere": "Numeroși elevi care iubesc mișcarea, competiția și un stil de viață sănătos au șansa de a se bucura de facilitățile pe care le oferă campusul universității. Este un loc în care nu contează doar performanța, ci și spiritul de echipă, fairplayul și bucuria de a fi activ. În funcție de talentul elevilor se oferă o varietate de activități pentru fiecare nivel de experiență.",
            "imagine": "static/images/cluburi/sportiv.jpg",
            "coordonatori": ["Cristian Petraș"]
        },
        "matematica": {
            "titlu": "Club de matematică",
            "descriere": "Cercul de Matematică este un spațiu dedicat elevilor care își doresc să aprofundeze matematica dincolo de cerințele standard ale programei, să își dezvolte gândirea logică și capacitatea de rezolvare a problemelor complexe. Activitatea cercului este construită pe ideea de excelență, rigoare intelectuală și plăcerea descoperirii matematice. În cadrul cercului se lucrează sistematic pe exerciții de nivel avansat, care solicită raționament, creativitate și transfer de cunoștințe. Elevii sunt provocați să analizeze situații-problemă autentice, să formuleze strategii de rezolvare, să compare metode diferite și să argumenteze matematic soluțiile obținute.\nUn accent important este pus pe:\nprobleme care pornesc din situații reale și necesită modelare matematică;\nsarcini deschise, cu mai multe soluții posibile, în care contează procesul de gândire;\ninterpretarea și analiza datelor, inclusiv utilizarea graficelor, tabelelor și funcțiilor;\ndemonstrații, justificări și explicații clare ale pașilor parcurși;\nconexiuni între algebră, analiză matematică, geometrie și statistică.\nActivitățile includ:\nexerciții de excelență și probleme de concurs;\nrezolvarea de seturi complexe de probleme structurate pe niveluri de dificultate;\nsarcini de investigare matematică, în care elevii explorează un concept, formulează ipoteze și le verifică;\nmini-proiecte individuale sau de grup, bazate pe cercetare matematică;\nprobleme de tip „studiu de caz”, care cer aplicarea matematicii în contexte interdisciplinare;\nantrenament pentru evaluări scrise care solicită claritate, structură și argumentare;\ndezvoltarea limbajului matematic și a exprimării riguroase.\nCercul de Matematică încurajează gândirea critică și autonomia intelectuală. Elevii sunt învățați să își explice raționamentele, să își revizuiască soluțiile și să privească eroarea ca parte firească a procesului de învățare. Activitatea se desfășoară într-un cadru colaborativ, în care elevii lucrează individual, în perechi sau în echipe, învățând să își confrunte ideile și să construiască soluții împreună. Sunt valorificate atât performanța individuală, cât și capacitatea de cooperare. Este un loc în care matematica devine exercițiu al gândirii profunde, al disciplinei intelectuale și al bucuriei de a înțelege.",
            "imagine": "",
            "coordonatori": ["Larisa Gaga, Tamara Istrate"]
        },
        "biologie": {
            "titlu": "Clubul de biologie „Tânărul biolog” (LifeLab)",
            "descriere": "Clubul de Biologie este un spațiu dedicat elevilor pasionați de științele vieții, care își doresc să înțeleagă biologia dincolo de manual și programă, prin explorare, cercetare și experiment. Activitatea clubului se desfășoară într-un cadru organizat, stimulativ și sigur, în care teoria este permanent conectată la practică. Un element central al clubului îl reprezintă lucrul efectiv în laborator. Elevii desfășoară experimente și lucrări practice folosind resursele și dotările necesare: aparatură de laborator, materiale specifice și instrumente adecvate activităților experimentale. Astfel, conceptele biologice sunt investigate direct, observate, testate și înțelese prin experiență concretă.\nActivitățile clubului includ:\ncercetare în echipe pe subiecte specifice de biologie;\nredactarea de referate și articole științifice bazate pe research, cu aplicabilitate pentru concursuri și olimpiade de științe;\nrealizarea de experimente și lucrări practice;\npregătire pentru concursuri și olimpiade;\nstudii suplimentare, cu informații aprofundate, dincolo de programa școlară;\nactivități experimentale desfășurate în laboratoare specializate.\nClubul își propune să creeze o comunitate de învățare formată din elevi cu interese, scopuri și valori comune, oferind oportunități reale de aprofundare pentru cei motivați de performanță și cunoaștere. Participanții sunt familiarizați cu contextul real al unei cariere în domeniul biologiei, învățând cum se desfășoară munca de cercetare, colaborarea în echipă și respectarea riguroasă a procedurilor științifice. În același timp, clubul pune accent pe dezvoltarea dimensiunii umane a muncii științifice: colaborarea, empatia, proactivitatea și altruismul sunt cultivate constant, prin activități de echipă și proiecte comune. Legăturile dintre membri se consolidează, iar spiritul de echipă devine un fundament al învățării. Clubul de Biologie este locul în care biologia se trăiește, se experimentează și se transformă într-o vocație.",
            "imagine": "",
            "coordonatori": ["Corneliu Tanase"]
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
        "nume": "Tamara Istrate",
        "materie": "Matematică",
        "descriere": "",
        "citat": "",
        "imagine": "tamara-istrate.jpg",


    },
    {
        "nume": "Maria Larisa Gaga",
        "materie": "Matematică",
        "descriere": "Am intrat în învățământ cu dorința de a schimba percepția asupra matematicii – să nu mai fie privită ca o disciplină rigidă și dificilă, ci ca un spațiu al logicii clare, o provocare pentru dezvoltarea gândirii. Cred că fiecare elev poate găsi sens și încredere în învățarea matematicii, dacă este ghidat cu răbdare, încurajare și deschidere.",
        "citat": "„Învăţând matematică, înveţi să gândeşti.” Grigore Moisil",
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
        "imagine": "kutasi-reka.jpg"
    },
    {
        "nume": "Daniela Lazăr",
        "materie": "Limba engleză",
        "descriere": "Limba engleză este, pentru mine, o cheie către cultură, către diversitate, către înțelegerea lumii și a celuilalt. În egală măsură, învățarea autentică nu este posibilă fără empatie. De aceea, sala de clasă este un spațiu al bucuriei de a fi împreună. Sunt un profesor responsabil și implicat, pentru că știu că fiecare oră lasă urme. Îmi doresc să-i înțeleg pe elevi dincolo de rezultate, să le ascult poveștile, să le recunosc fragilitățile și să le valorific potențialul. Nu cred în etichete, ci în posibilitatea fiecărui copil de a da tot ce are mai bun, atunci când se simte în siguranță. Rigoarea mea nu exclude căldura, iar exigența nu anulează blândețea. Cred într-o eleganță a meseriei de profesor: în modul de a vorbi, de a corecta, de a îndruma, de a fi. Eleganța care se vede în respectul față de elev, față de limbaj și față de actul educațional. A fi profesor, pentru mine, înseamnă a fi prezent. A însoți, a provoca, a susține. A crede în copii chiar și atunci când ei nu cred încă în ei înșiși. Și, mai ales, a nu uita niciodată că educația este, înainte de toate, o relație umană.",
        "citat": "„Cred că toți avem empatie. S-ar putea să nu avem suficient curaj să o arătăm.” – Maya Angelou",
        "imagine": "daniela-lazar.jpg",
    },
    {
        "nume": "Stoica Briena",
        "materie": "Limba engleză",
        "descriere": "Cred că educația este o lucrare vie, care modelează nu doar mintea, ci și modul nostru de a fi în lume. Ea începe în interior — în cultivarea înțelegerii, a discernământului și a responsabilității — și se împlinește în afară, în felul în care relaționăm, gândim și acționăm în comunitate. Educația nu este o simplă transmitere de cunoștințe, ci o formare a conștiinței și a caracterului, o paideia prin care omul învață să trăiască cu sens, să caute binele și să contribuie la ordinea morală a lumii din jurul său. În acest proces, profesorul nu este doar un ghid al învățării, ci un însoțitor în devenire — un martor al creșterii interioare care face posibilă o lume mai dreaptă, mai luminoasă și mai umană. De aceea iubesc să fiu profesor: pentru că în fiecare elev se reflectă posibilitatea unei lumi întregite prin cunoaștere și caracter.",
        "citat": "Educația este legătura vie dintre formarea interioară a omului și lumea pe care o zidește prin prezența și faptele sale",
        "imagine": "briena-stoica.jpg",
    },
    {
        "nume": "Andreea Bîtcă",
        "materie": "Limba engleză",
        "descriere": "Iubitoare de om şi de frumos, spirit ludic, scopul meu principal la fiecare oră de curs este să duc activitatea de la clasă dincolo de exerciţiul intelectual spre o înflorire a spiritului. Apreciez creativitatea, exprimarea liberă a opiniilor, jocul cu noţiuni şi cunoştinţe, dar şi rigoarea, conştiinciozitatea şi tenacitatea. Consider că munca desfăşurată alături de adolescenţi este nepreţuită şi sper în fiecare zi ca fervorii şi setei de cunoaştere specific adolescentine să le aduc claritate, curajul de a-şi menţine mintea şi sufletul deschise, precum şi dorinţa de a lăsa fiecare părticică de viaţă pe care elevii o vor atinge mai frumoasă, mai bună, mai luminoasă.",
        "citat": "„Fii schimbarea pe care vrei să o vezi în lume.” (Mahatma Ghandi)",
        "imagine": "",
    },
    {
        "nume": "Daniel Raduly",
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
        "imagine": "siteumf/static/images/Poza-UMFST/profesori/andreea-romana-ban.jpg",
        "rol": "Conducere",
    },
    {
        "nume": "Papp Botond",
        "materie": "Fizică",
        "descriere": "Sunt un profesor de fizică pasionat de cercetare și de felul în care legile universului pot deveni inteligibile pentru mintea unui adolescent. Investesc constant în digitalizarea conținutului de fizică, transformând concepte abstracte în simulări, modele vizuale și experiențe interactive. Încerc să cultiv gândirea științifică: formularea ipotezelor, verificarea lor, acceptarea erorii ca parte a cunoașterii. Îi învăț pe elevi să nu le frică de probleme dificile, ci să le descompună, să le modeleze și să le înțeleagă pas cu pas. În sala de clasă, fizica nu se memorează, ci se construiește. Este locul în care rigoarea se întâlnește cu pasiunea, iar legile naturii capătă sens, frumusețe și relevanță.",
        "citat": "",
        "imagine": ""
    },
    {
        "nume": "Mihai Babotă",
        "materie": "Chimie",
        "descriere": "Aflată la granița dintre știință, empirism și mister, chimia ne descoperă dincolo de reacții, formule și structuri esența proceselor care guvernează existența micro și macro universului, precum și modul în care omul poate trăi în echilibru cu el însuși și cu mediul înconjurător.Ca disciplină de studiu și știință exactă transpusă în cotidian, cred că ne explică faptul că \"E chimie între noi\" - parafrazând titlul unei melodii. Chimia e realitate frumoasă, plină de culoare și fascinație, pe care o trăim și o simțim în viața de zi cu zi.",
        "citat": "",
        "imagine": "mihai-babota.jpg"
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
        "nume": "Szabolcs-Lehel Szakács",
        "materie": "Geografia/Istoria UK si SUA",
        "descriere": "Pentru mine, educația nu e o linie dreaptă, ci o potecă sinuoasă, desenată de pașii curiozității. Este arta de a crea un mediu în care elevii pot explora liber, pot formula întrebări autentice și pot gândi dincolo de granițele obișnuinței. Cred într-un mod de predare care provoacă, care inspiră și care invită fiecare minte să devină coautor al semnificațiilor. Fie că urmărim cauzele revoluțiilor sau contururile continentelor, învățarea devine un dialog viu, în care cunoașterea și imaginația se întâlnesc în libertate. Sunt ferm convins că libertatea adevărată începe acolo unde avem curajul să punem sub semnul întrebării fiecare aspect al lumii în care trăim. Curajul de a întreba fără garanții valorează mai mult decât liniștea unui răspuns imposibil de contestat.",
        "citat": ": “I would rather have questions that can't be answered than answers that can't be questioned.” ― Richard Feynman",
        "imagine": "Lehel.jpg",
    },
    {
        "nume": "Crina Chirilă",
        "materie": "Geografie",
        "descriere": "De mică, am fost pasionată de explorarea lumii și de înțelegerea fenomenelor naturale, iar din pasiune mi-am creat o profesie. Ca profesoară de geografie încerc sa deschid orizonturi noi pentru elevii mei, transformând hărțile în povești. Geografia este una dintre disciplinele care ne creează „conștiința eco”, iar pentru a nu face rău lumii din jur avem nevoie să înțelegem dinamica pământului și modul în care timpul ne-a construit din adâncul oceanelor în vârful munților. Sper ca fiecare lecție să-i ajute pe elevi să cunoască lumea și să le ofere șansa de a-și găsi un loc în ea.",
        "citat": " Natura are un limbaj propriu și, dacă îi înțelegem semnele și ritmul, ne dezvăluie taine pe care nimic altceva nu le poate exprima",
        "imagine": "crina-chirila.jpg"
    },
    {
        "nume": "Nora Dumbravă",
        "materie": "Logică/Psihologie",
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
        "nume": "Cristian Petraș",
        "materie": "Educație fizică",
        "descriere": "",
        "citat": "",
        "imagine": ""
    },
    {
        "nume": "Jeddi Tünde-Mária",
        "materie": "Educație muzicală",
        "descriere": "",
        "citat": "",
        "imagine": ""
    },
    {
        "nume": "Mihaela Bucur",
        "materie": "Educație antreprenorială",
        "descriere": "",
        "citat": "",
        "imagine": "",
    },
    {
        "nume": "Andreea-Ioana Focșan",
        "materie": "Informatică",
        "descriere": "Meseria de profesor este cea mai completă: trebuie să fii profesor, mentor, ghid, uneori psiholog, alteori motivator, uneori avocat sau judecător – de toate câte puțin. La orele de informatică nu există loc pentru plictiseală – fiecare elev e invitat să gândească, să experimenteze și să găsească soluții proprii. Deși sunt o persoană riguroasă și cerințele mele sunt clare, am răbdare să explic fiecare concept cu exemple din viața de zi cu zi, astfel încât materia să devină mai ușor de înțeles. Îmi place să provoc elevii prin probleme care stimulează gândirea critică și creativitatea și să folosesc metode moderne care fac învățarea mai activă și mai captivantă. Orele mele sunt un spațiu dinamic în care rigoarea se îmbină cu curiozitatea, iar greșelile devin oportunități de descoperire. Îmi doresc să lucrez cu elevii care sunt curioși, dornici să exploreze, să pună întrebări și să învețe prin experiență.",
        "citat": "Algoritmi pentru minți curioase și învățători neobosiți.",
        "imagine": ""
    },
     {
        "nume": "Peres Gyula Dániel",
        "materie": "TIC",
        "descriere": "Pentru mine predarea nu înseamnă doar transmiterea de informații, ci mai mult de atât, formarea elevilor în oameni integri, înțelepți și maturi. Eu văd profesorii ca pe niște mentori - responsabili nu doar pentru a transmite cunoștințe, ci pentru a modela oameni capabili să se descurce în viața de zi cu zi și să folosească ceea ce învață în mod înțelept.",
        "citat": "„Înțelepciunea este folosirea potrivită a cunoașterii.” Charles Spurgeon",
        "imagine": "peres-gyula.jpg"
    }
]



clase = [
    {
        "numar": 9,
        "litera": "A",
        "diriginte": "Daniela Lazăr",
        "profil": "Mate-Informatică",
        "citat": "",
        "imagine": "9A.jpeg",
        "elevi": [
            {"nume": "Bârlean Daria Andreea"},
            {"nume": "Bârlean Sofia Alexia"},
            {"nume": "Blaga Amalia"},
            {"nume": "Boantă Doru-Șerban"},
            {"nume": "Cerghizan Adrian-Gabriel"},
            {"nume": "Chirteș Maria"},
            {"nume": "Cozma Ruxandra"},
            {"nume": "Danci Dora-Elena"},
            {"nume": "Fărcaș Bogdan"},
            {"nume": "Gligor Adriana-Emanuela"},
            {"nume": "Huza Cosmin"},
            {"nume": "Ignat Ariana Raluca"},
            {"nume": "Laurenț Cezar-Ioan"},
            {"nume": "Lőbl Carla-Sabrina"},
            {"nume": "Mărginean Antonia-Maria"},
            {"nume": "Morar Alexandra-Bianca"},
            {"nume": "Mureșan Alexia-Cristina"},
            {"nume": "Oltean Cristina-Nicoleta"},
            {"nume": "Petrea Luca-Alexandru"},
            {"nume": "Popa Vlad-Ștefan"},
            {"nume": "Rus Daria-Ioana"},
            {"nume": "Rusu Mihai"},
            {"nume": "Stoica Dalia"},
            {"nume": "Varga Cezar-Andrei"},
            {"nume": "Vasinc Daniel"},
            {"nume": "Velcherean Ana"}
        ]
    },
    {
        "numar": 9,
        "litera": "B",
        "diriginte": "Mihai Babotă",
        "profil": "Științele Naturii",
        "citat": "",
        "imagine": "9B.jpeg",
        "elevi": [
            {"nume": "Bálint Erick"},
            {"nume": "Bereholschi Maia-Sofia"},
            {"nume": "Blaga Nadia Veronica"},
            {"nume": "Blănaru Sara"},
            {"nume": "Bogdan Diana"},
            {"nume": "Chiriac Patricia-Mădălina"},
            {"nume": "Chirilean Alexia-Ioana"},
            {"nume": "Cîmpan Maria"},
            {"nume": "Cotoară Radu-Ioan"},
            {"nume": "Crăciun Iris-Maria"},
            {"nume": "Gherendi Sofia"},
            {"nume": "Lenard Alexia"},
            {"nume": "Maier Alisia Eliza"},
            {"nume": "Matei Irina"},
            {"nume": "Mihai Giulia-Elena"},
            {"nume": "Moldovan David-Rareș"},
            {"nume": "Nagy Victor-Alex"},
            {"nume": "Nicușan Ștefania-Bianca"},
            {"nume": "Pop Izabella-Ana"},
            {"nume": "Rațiu Ana-Maria"},
            {"nume": "Sălăgeanu Diana-Maria"},
            {"nume": "Sârb Maria"},
            {"nume": "Stoica Delia"},
            {"nume": "Șoiom Ana-Bianca"},
            {"nume": "Ștefan Mara-Bianca"},
            {"nume": "Tancău Antonia"},
            {"nume": "Truța Cristian"},
            {"nume": "Zilahi Irina-Maria"}
        ]
    },
    {
        "numar": 10,
        "litera": "B",
        "diriginte": "Bogdan Rațiu",
        "profil": "Științele Naturii",
        "citat": "Trasăm linii care nu se șterg",
        "imagine": "10B.jpg",
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
            {"nume": "Pastia Catinca"},
            {"nume": "Pop Sara"},
            {"nume": "Sabău Raul"},
            {"nume": "Șandru Octavian"},
            {"nume": "Szasz Roberta", "performante" : [{"titlu": "Olimpiada Națională de Biologie", "locatie": "Tg. Mureș, etapa județeană", "premiu": "Premiul II"}, {"titlu": "Olimpiada Interdisciplinară „Culturalitate și spiritualitate românească“", "locatie": "Tg. Mureș, etapa județeană", "premiu": "Premiul III"}]},
            {"nume": "Vasiliu Anca"},
            {"nume": "Vidican Andreea"}
        ]
    },
    {
        "numar": 10,
        "litera": "A",
        "diriginte": "Bianca Han",
        "profil": "Mate-Informatică",
        "citat": "Prin respect, crești - pe tine și pe ceilalți.",
        "imagine": "10A.jpg",
        "elevi": [
            {"nume": "Biriș Sergiu"},
            {"nume": "Corondeanu Raul",
             "performante": [
                {
                    "titlu": "Olimpiada Națională de Lb. Engleză",
                    "locatie": "Tulcea, etapa națională",
                    "premiu": "Participare"
                },   
            {
                "titlu": "Concursul Național ENROLL FOR FUN, ediția a VII-a, secțiunea creații literare, limba engleză",
                "locatie": "Baia Mare",
                "premiu": "Locul II"
            }
             ]},
            {"nume": "Cucuiet Andrei"},
            {"nume": "David Aiana"},
            {"nume": "Ercean David"},
            {"nume": "Gherman Cezara"},
            {"nume": "Jovrea Ștefan"},
            {"nume": "Lazăr Cristian",
             "performante": [
                {
                    "titlu": "Concursul județean de Matematică „Simon Petru“, ediția a XXIII-a",
                    "locatie": "Tg Mureș, Colegiul Național „Unirea“",
                    "premiu": "Locul II, secțiunea Matematică-informatică"
                }
             ]},
            {"nume": "Maier Alia"},
            {"nume": "Mitoșeriu David",
             "performante": [
                {
                    "titlu": "Concursul Național ENROLL FOR FUN, ediția a VII-a, secțiunea creații literare, limba engleză",
                    "locatie": "Baia Mare",
                    "premiu": "Locul II"
                }
             ]},
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
                "titlu": "Olimpiada Națională De Matematică",
                "locatie": "1-6 aprilie, Botoșani",
                "premiu": "Premiul II la etapa județeană și calificare la etapa națională"
            },
            {
                "titlu": "Olimpiada Națională de Fizică",
                "locatie": "10-15 aprilie, Slobozia",
                "premiu": "Premiul I la etapa județeană și calificare la etapa națională"
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
            if not pers.get('imagine'):
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
