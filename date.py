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
        },
        "ziua-mondiala-a-educatiei": {
            "titlu": "Ziua Mondială a Educației",
            "subtitlu": "5 octombrie",
            "descriere": """
            <p>Elevii și profesorii Liceului UMFST „George Emil Palade” au sărbătorit Ziua Mondială a Educației în 5 octombrie, un prilej de recunoștință și respect față de cei care se dedică educației și dau sens învățării.</p>
            <p>Educația înseamnă mai mult decât transmitere și acumulare de cunoștințe. Educația deschide mintea, cultivă gândirea critică și valorile morale esențiale.</p>
            <p>Educația reprezintă cea mai valoroasă și importantă investiție în viitorul generațiilor de azi și de mâine.</p>
            """,
            "imagine": None
        },
        "ziua-portilor-deschise-2026": {
            "titlu": "Ziua Porților Deschise 2026",
            "subtitlu": "Descoperă liceul UMFST",
            "descriere": """
            <p>Ziua Porților Deschise 2026 a adus în atenție misiunea liceului UMFST: o comunitate educațională deschisă, în care elevul devine participant activ în procesul său de formare.</p>
            <div class='row gx-3 gy-4'>
              <div class='col-md-6'>
                <img src='/static/images/zpd1.jpg' alt='Ziua Porților Deschise 2026' class='img-fluid rounded mb-3'>
                <p><strong>Viziunea pedagogică</strong> se sprijină pe cinci valori fundamentale: pasiunea pentru cunoaștere, excelența academică, dezvoltarea creativă și etică, perseverența și cultura colaborativă.</p>
              </div>
              <div class='col-md-6'>
                <img src='/static/images/zpd2.jpg' alt='Elevi și profesori UMFST' class='img-fluid rounded mb-3'>
                <p>Liceul construiește contexte în care cunoașterea nu este doar transmisă, ci experimentată și pusă în dialog cu întrebările reale ale elevilor.</p>
              </div>
            </div>
            <div class='row gx-3 gy-4'>
              <div class='col-md-6'>
                <img src='/static/images/zpd3.jpg' alt='Atmosfera evenimentului' class='img-fluid rounded mb-3'>
                <p>Educația are sens atunci când echilibrează calificarea riguroasă, socializarea autentică și formarea subiectivă a fiecărui elev.</p>
              </div>
              <div class='col-md-6'>
                <img src='/static/images/zpd4.jpg' alt='Program și dialog despre școală' class='img-fluid rounded mb-3'>
                <p>Programul a punctat dorința liceului de a crea un spațiu autentic de conversație despre educație, nevoile elevilor și felul în care construim o comunitate școlară relevantă.</p>
              </div>
            </div>
            <div class='pdf-card p-4 mt-4 rounded shadow-sm bg-light'>
              <h4 class='mb-3'>Viziunea pedagogică</h4>
              <p>Descopera modelul educațional UMFST și valorile care susțin formarea elevului de azi și de mâine.</p>
              <div class='ratio ratio-16x9 mb-3'>
                <iframe src='/static/images/viziune_pedagogica.pdf#view=FitH' title='Preview Viziune pedagogică' class='rounded border'></iframe>
              </div>
              <a href='/static/images/viziune_pedagogica.pdf' class='btn btn-outline-primary' target='_blank' rel='noopener noreferrer'>Vizualizează PDF în filă nouă</a>
            </div>
            <div class='mt-4 text-center'>
              <p class='mb-0 fst-italic small text-muted'>Mai multe fotografii de la eveniment sunt disponibile pe Instagram: <a href='https://www.instagram.com/liceul_umfst' target='_blank' rel='noopener noreferrer'>@liceul_umfst</a></p>
            </div>
            """,    
        },
        "ziua-recunostintei": {
            "titlu": "Ziua Recunoștinței",
            "subtitlu": "27 noiembrie 2025",
            "descriere": """
            <p>Elevii și profesorii Liceului UMFST „George Emil Palade” au sărbătorit joi, 27 noiembrie 2025, Ziua Recunoștinței printr-un eveniment inedit și într-o atmosferă memorabilă.</p>
            <p>Elevii din clasele a IX-a și a X-a, organizați în echipe mixte, au parcurs împreună Thanksgiving Journey și au realizat o serie de activități interactive inspirate din momente-cheie ale istoriei americane - de la St. Augustine și Plymouth până la proclamările prezidențiale care au modelat tradiția modernă. Prin jocuri colaborative și misiuni tematice, liceenii au explorat concepte precum încrederea, comunicarea, empatia și diversitatea culturală. Activitatea a avut caracter interdisciplinar: nu doar profesorii de limba engleză au coordonat sesiunile, ci și cei de chimie, matematică, limba română și informatică, care au comunicat în limba engleză, contribuind la atmosfera autentică și dinamică a evenimentului. Ziua s-a încheiat cu Washington’s Address și cu o sesiune de dans și voie bună.</p>
            <p>A fost o experiență educativă, bilingvă și distractivă - o adevărată sărbătoare a comunității noastre și a valorilor Zilei Recunoștinței. Le mulțumim pentru sprijin tuturor profesorilor implicați, alături de catedra de Limba engleză, elevilor din Consiliul elevilor și studentului Darius Cucuiet pentru componenta artistică.</p>
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
            <ul>
              <li>Lectura ca dialog: Întâlnire cu criticul literar Al. Cistelecan. De ce să (mai) citim?</li>
              <li>Lectura în spațiul urban: „Orașul care citește”.</li>
              <li>Lectura ca performance.</li>
              <li>Lectura ca responsabilitate civică: Manifest pentru lectură! De ce contează lectura pentru o societate democratică? Ce pierdem când nu citim?</li>
              <li>Lectura ca experiență socială, nu doar intelectuală.</li>
              <li>Cafeneaua literară: discuții libere despre o carte, nu analiză școlară, ci conversație culturală.</li>
              <li>Procesul operelor: pro și contra în fața unei opere.</li>
            </ul>
            <p>Vezi și materialul video: <a href="https://www.youtube.com/watch?v=fMlneB3wZ2U" target="_blank" rel="noopener noreferrer">https://www.youtube.com/watch?v=fMlneB3wZ2U</a></p>
            """,

        },
        "performanta-excelenta": {
            "titlu": "Performanță și excelență",
            "subtitlu": "O nouă ediție a podcastului „Banca din față” cu elevi de performanță.",
            "descriere": """
            <p>Performanța înseamnă talent, dar și un mediu care încurajează evoluția și excelența.</p>
            <p>În această ediție a podcastului „Banca din față”, îi avem invitați pe câțiva dintre elevii Liceului UMFST „George Emil Palade” care au participat la etapa națională a olimpiadelor de Limba și literatura română, Limba engleză, Biologie și Matematică.</p>
            <p>Discuția își propune să ofere o imagine asupra modului în care elevii liceului își pot dezvolta abilitățile, pasiunile și dorința de performanță, într-un mediu care susține excelența academică și evoluția personală.</p>
            """,

        },
        "stai-sigur-pe-net": {
            "titlu": "Stai sigur pe net!",
            "subtitlu": "Dezbatere interactivă despre siguranța în mediul online.",
            "descriere": """
            <p>Dezbaterea interactivă „Stai sigur pe net!” a fost organizată de Radio Târgu Mureș, cu participarea elevilor liceului UMFST și a profesorului Bogdan Rațiu.</p>
            <p>Invităm comunitatea să discute despre subiectele problematice pe care tinerii le întâlnesc în mediul digital și să înțeleagă cum pot naviga online cu mai multă responsabilitate și încredere.</p>
            """,

        },
        "antreprenori-fata-in-fata": {
            "titlu": "Antreprenori față în față",
            "subtitlu": "Întâlniri de business și antreprenoriat pentru liceeni.",
            "descriere": """
            <p>Elevii Liceului UMFST „George Emil Palade” au avut ocazia de a cunoaște mai mulți antreprenori și reprezentanți ai mediului de afaceri mureșean, în cadrul orelor de educație antreprenorială.</p>
            <p>Aceștia au interacționat cu invitații și au descoperit povești reale de inițiativă, curaj și dezvoltare profesională, dar și perspective concrete asupra modului în care ideile pot deveni proiecte și afaceri.</p>
            <p>Astfel de întâlniri îi ajută pe elevi să înțeleagă mai bine lumea antreprenoriatului și să descopere oportunitățile pe care inițiativa și implicarea le pot aduce în parcursul lor profesional.</p>
            <p><strong>Coordonator:</strong> dna prof. Mihaela Bucur</p>
            """,

        },
        "balul-bobocilor": {
            "titlu": "Balul Bobocilor",
            "subtitlu": "Prima ediție a Balului Bobocilor UMFST, februarie 2026.",
            "descriere": """
            <p>Balul Bobocilor al elevilor Liceului UMFST „George Emil Palade” a fost prima ediție din februarie 2026, având tema <strong>Our style. Our story.</strong></p>
            <p>Programul evenimentului a cuprins probe atent pregătite de colegii mai mari: proba de spontaneitate, proba de cultură generală și proba tactilă, un show de talente și stand-up comedy, dar mai ales distracție și voie bună.</p>
            <p>Bobocii au surprins membrii juriului cu energie, creativitate și autenticitate, creând o seară plină de emoție și momente memorabile.</p>
            """,
            "imagini": [
                "images/HUB/bal2026afis.JPG",
                "images/HUB/bal2026.JPG"
            ]
        },
        "engineering-escape-room": {
            "titlu": "Engineering Escape Room",
            "subtitlu": "O experiență practică STEM pentru liceenii UMFST.",
            "descriere": """
            <p>Studenții organizației ESTIEM LG Târgu Mureș au organizat, în laboratoarele Facultății de Inginerie și Tehnologia Informației, UMFST G.E. Palade Târgu Mureș, o provocare practică dedicată elevilor Liceului UMFST „George Emil Palade”.</p>
            <p>Evenimentul a fost conceput ca o experiență interactivă prin care elevii au avut ocazia să descopere ingineria într-un mod practic și atractiv.</p>
            <p>Probele au inclus descifrarea de coduri, exerciții de logică și cultură generală, precum și asamblarea și utilizarea unui microcontroller Arduino pentru rezolvarea unui puzzle tehnic.</p>
            <p>Succesul evenimentului deschide perspectiva continuării acestor inițiative, ca parte a implicării active a studenților ESTIEM în promovarea educației STEM.</p>
            <p><strong>Coordonator:</strong> dna prof. Mihaela Bucur</p>
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
            "descriere": "<p>Alături de Teatrul „Scena” din Târgu Mureș elevii Liceului UMFST „George Emil Palade” au parte de un atelier de actorie și de dezvoltare personală prin teatru. Atelierul este coordonat de actorul Liviu Pancu și le oferă elevilor Liceului UMFST oportunitatea de a-și îmbunătăți abilitățile de comunicare și vorbire în public, de a-și gestiona emoțiile și de a-și folosi creativitatea și imaginația într-un mod constructiv.</p>",
            "imagine": "static/images/activitati/club/teatru.jpg",
            "coordonatori": ["Liviu Pancu"]
        },
        "dezbateri": {
            "titlu": "Paideia - club de dezbateri și oratorie",
            "descriere": "<p>Numele clubului, Paideia, provine din cultura greacă antică și desemnează idealul formării integrale a omului prin educație, cultură și dialog. Alegerea acestui nume reflectă convingerea că dezbaterea și arta discursului sunt instrumente esențiale pentru dezvoltarea rațiunii, a caracterului și a spiritului civic.</p><p>Clubul Paideia are misiunea de a sprijini elevii să își dezvolte gândirea critică, exprimarea clară și responsabilă, respectul față de diversitatea opiniilor și capacitatea de a construi argumente solide.</p><p>Obiectivele principale sunt:</p><ul><li>dezvoltarea competențelor de argumentare, retorică și public speaking;</li><li>promovarea unei culturi a dialogului bazată pe respect, toleranță și fair-play;</li><li>participarea constantă la competiții de dezbateri și de public speaking la nivel local, național și internațional;</li><li>formarea unor atitudini morale și civice prin implicarea activă în activitățile clubului;</li><li>dezvoltarea capacității de a aborda teme interdisciplinare și actuale, prin documentare riguroasă;</li><li>cultivarea toleranței față de pluralismul opiniilor și a deschiderii către perspective diverse.</li></ul><p>Activitatea clubului include ateliere de public speaking și oratorie, sesiuni de dezbateri academice pe teme interdisciplinare, pregătirea echipelor pentru competiții și organizarea unor evenimente de tip „dialog socratic” sau mini-dezbateri interne. Elevii vor fi încurajați să participe în mod constant la concursuri de dezbateri și de oratorie înscrise în calendarele naționale și internaționale, reprezentând liceul cu profesionalism și responsabilitate.</p><p>Prin pregătirea dezbaterilor, elevii sunt motivați să realizeze documentări temeinice, dobândind astfel cunoștințe variate și actuale din domenii diverse – social, cultural, economic și politic. Susținerea pledoariilor în fața publicului contribuie la formarea abilităților de oratorie și retorică, dar și la consolidarea spiritului de echipă.</p><p>Impactul clubului Paideia se reflectă atât la nivelul dezvoltării personale a elevilor, cât și în comunitatea școlară. Elevii participanți dobândesc competențe de comunicare, gândire critică și cooperare, iar profesorii și părinții beneficiază indirect prin implicarea elevilor în activități de calitate. Comunitatea locală are, la rândul ei, de câștigat prin formarea unor tineri capabili să abordeze cu responsabilitate problemele lumii contemporane.</p>",
            "imagine": "static/images/cluburi/dezbateri.jpg",
            "coordonatori": ["Briena Stoica, Bogdan Rațiu"]
        },
        "robotica": {
            "titlu": "Club de robotică",
            "descriere": "<p>Robotica, alături de disciplinele Informatică și TIC, Matematică și Fizică, recomandă dezvoltarea competenţelor STEM (Știință, Tehnologie, Inginerie și Matematică) cu un caracter transdisciplinar.</p><p>Clubul de robotică este locul unde elevii pasionați de tehnologie pot învăța să construiască și să programeze roboți. Este o oportunitate excelentă de a dezvolta abilități tehnice și de a lucra în echipă.</p><p>Obiectivele principale sunt:</p><ul><li>formarea competenţelor de utilizare transdisciplinară și a achizițiilor din Fizică, Matematică, Informatică și TIC,</li><li>dezvoltarea creativităţii tehnice, a gândirii logice şi a gândirii algoritmice, a competenţelor de modelare, algoritmizare şi programare a algoritmilor</li><li>dezvoltarea unor capacităţi de cercetare şi de creaţie tehnică.</li></ul><p>Atingerea acestor scopuri se realizează prin conceperea şi asamblarea modelelor de roboţi şi elaborarea de algoritmi şi programe de conducere.</p><p>Prin studiul roboților, elevii pot dobândi achiziții de învățare relevante pentru domeniile: Inginerie, Tehnologie, Știința sistemelor și materialelor mecanice, electronice și sisteme electrice, concepte de programare și matematică aplicată. De asemenea, își formează abilități de muncă în echipă, leadership și rezolvarea problemelor. Activitățile de învățare propuse pot fi realizate în mod real cu ajutorul unor kit-uri achiziționate, sau într-un mediu de programare online, care permite programarea roboților. Prin intermediul a două proiecte (Fondul Științescu Mureș și proiect intern UMFST) au fost achiziționate kituri de electronica prin programare nivel începător și intermediar, kit-uri de Energie Verde (Casă Smart, Panou Solar, irigații plante) respectiv kit-uri de mașină robot, toate echipate cu mai mulți senzori electronici, și comandate prin sisteme Arduino.</p><p>Ne propunem, deasemenea participarea la Concursuri de Robotică atât la nivel local (intern UMFST și în colaborare cu alte licee) cât și la nivel national (ex. Nextlab).</p>",
            "coordonatori": ["Papp Botond, Peres Gyula"]
        },
        "informatica": {
            "titlu": "Clubul de informatica",
            "descriere": "<p>Clubul de informatica al liceului se adresează elevilor de la profilul Matematică-Informatică pasionați de programare, algoritmică și noile tehnologii. Clubul este conceput ca un spațiu de performanță și inovație, în care elevii se pot pregăti sistematic pentru concursuri și olimpiade de informatică, dar și pentru provocările reale ale domeniului IT.</p><p>Activitățile vizează atât aprofundarea noțiunilor de programare și rezolvarea de probleme de nivel competițional, cât și realizarea de proiecte practice, individuale și de echipă. Elevii lucrează într-un laborator modern, dotat cu calculatoare performante, tablă interactivă, imprimantă 3D, ochelari VR, sistem de videoconferință și scanner 3D, ceea ce le permite să experimenteze tehnologii actuale și să dezvolte aplicații și prototipuri inovatoare.</p><p>Prin participarea la Clubul de Informatică, elevii își dezvoltă gândirea logică, creativitatea, autonomia și capacitatea de colaborare, își construiesc un portofoliu relevant și dobândesc competențe esențiale pentru studiile universitare și pentru viitoarele cariere în domeniul STEM.</p><p>Clubul de Informatică este locul în care pasiunea pentru cod se transformă în performanță și în viitor profesional.</p>",
            "imagine": "",
            "coordonatori": ["Andreea Drăguș"]
        },
        "lectura": {
            "titlu": "Club de lectură",
            "descriere": "<p>Clubul de lectură este un spațiu de întâlnire în jurul textului. Nu este un loc al răspunsurilor „corecte”, ci al interpretărilor argumentate și al bucuriei de a gândi împreună. Textele sunt citite atent, discutate în profunzime și puse în relație cu experiențele de viață ale participanților, cu alte texte, cu idei din cultură, filosofie sau știință. Accentul cade pe sens, pe felul în care literatura ne ajută să ne înțelegem pe noi înșine și lumea.</p><p>Activitățile clubului includ:</p><ul><li>cercuri de lectură bazate pe discuție liberă, ghidată de întrebări deschise;</li><li>interpretarea textelor literare și nonliterare din perspective diferite;</li><li>formularea și susținerea punctelor de vedere prin argumente;</li><li>dialog între cititori, nu evaluare sau ierarhizare;</li><li>conexiuni între texte și realitatea contemporană;</li><li>exerciții de lectură reflexivă și scriere de reacție (jurnale de lectură, fragmente eseistice, note personale);</li><li>descoperirea plăcerii lecturii ca act intelectual și emoțional.</li></ul><p>Clubul pune accent pe:</p><ul><li>cititorul ca partener de dialog, nu ca simplu receptor;</li><li>respectul față de opiniile diferite;</li><li>ascultarea activă și capacitatea de a construi sens împreună;</li><li>dezvoltarea gândirii critice și a expresivității personale.</li></ul><p>Clubul de lectură este, în esență, o comunitate de cititori care cred că lectura bună se trăiește împreună și că sensul se construiește în dialog.</p>",
            "imagine": "",
            "coordonatori": ["Bogdan Rațiu"]
        },
        "sportiv": {
            "titlu": "Club de activități sportive",
            "descriere": "<p>Numeroși elevi care iubesc mișcarea, competiția și un stil de viață sănătos au șansa de a se bucura de facilitățile pe care le oferă campusul universității. Este un loc în care nu contează doar performanța, ci și spiritul de echipă, fairplayul și bucuria de a fi activ. În funcție de talentul elevilor se oferă o varietate de activități pentru fiecare nivel de experiență.</p>",
            "imagine": "static/images/cluburi/sportiv.jpg",
            "coordonatori": ["Cristian Petraș"]
        },
        "matematica": {
            "titlu": "Club de matematică",
            "descriere": "<p>Clubul de matematică este un spațiu dedicat explorării și aprofundării matematicii dincolo de programa școlară. Participanții au ocazia să descopere frumusețea și utilitatea matematicii prin activități interactive, provocări și proiecte creative.</p><p>Activitățile clubului includ:</p><ul><li>rezolvarea de probleme matematice interesante și provocatoare;</li><li>explorarea conceptelor matematice avansate (geometrie, algebră, teoria numerelor);</li><li>participarea la concursuri și olimpiade matematice;</li><li>dezvoltarea gândirii logice și a abilităților de rezolvare a problemelor;</li><li>crearea de proiecte matematice (modele, demonstrații, aplicații practice);</li><li>discuții despre istoria matematicii și contribuțiile marilor matematicieni;</li><li>jocuri matematice și puzzle-uri pentru dezvoltarea creativității.</li></ul><p>Clubul pune accent pe:</p><ul><li>înțelegerea profundă a conceptelor, nu doar memorarea;</li><li>aplicarea matematicii în viața de zi cu zi și în alte discipline;</li><li>colaborarea și schimbul de idei între participanți;</li><li>dezvoltarea încrederii în propriile abilități matematice;</li><li>plăcerea de a descoperi și de a crea în matematică.</li></ul><p>Clubul de matematică este potrivit pentru elevii pasionați de matematică, dar și pentru cei care doresc să își dezvolte gândirea logică și să descopere noi perspective asupra acestei științe fascinante.</p>",
            "imagine": "",
            "coordonatori": ["Larisa Gaga, Tamara Istrate"]
        },
        "biologie": {
            "titlu": "Clubul de biologie „Tânărul biolog” (LifeLab)",
            "descriere": "<p>Clubul de biologie „Tânărul biolog” (LifeLab) este un spațiu dedicat elevilor pasionați de științele vieții, care își doresc să înțeleagă biologia dincolo de manual și programă, prin explorare, cercetare și experiment. Activitatea clubului se desfășoară într-un cadru organizat, stimulativ și sigur, în care teoria este permanent conectată la practică.</p><p>Un element central al clubului îl reprezintă lucrul efectiv în laborator. Elevii desfășoară experimente și lucrări practice folosind resursele și dotările necesare: aparatură de laborator, materiale specifice și instrumente adecvate activităților experimentale. Astfel, conceptele biologice sunt investigate direct, observate, testate și înțelese prin experiență concretă.</p><p>Activitățile clubului includ:</p><ul><li>cercetare în echipe pe subiecte specifice de biologie;</li><li>redactarea de referate și articole științifice bazate pe research, cu aplicabilitate pentru concursuri și olimpiade de științe;</li><li>realizarea de experimente și lucrări practice;</li><li>pregătire pentru concursuri și olimpiade;</li><li>studii suplimentare, cu informații aprofundate, dincolo de programa școlară;</li><li>activități experimentale desfășurate în laboratoare specializate.</li></ul><p>Clubul își propune să creeze o comunitate de învățare formată din elevi cu interese, scopuri și valori comune, oferind oportunități reale de aprofundare pentru cei motivați de performanță și cunoaștere. Participanții sunt familiarizați cu contextul real al unei cariere în domeniul biologiei, învățând cum se desfășoară munca de cercetare, colaborarea în echipă și respectarea riguroasă a procedurilor științifice.</p><p>În același timp, clubul pune accent pe dezvoltarea dimensiunii umane a muncii științifice: colaborarea, empatia, proactivitatea și altruismul sunt cultivate constant, prin activități de echipă și proiecte comune. Legăturile dintre membri se consolidează, iar spiritul de echipă devine un fundament al învățării. Clubul de Biologie este locul în care biologia se trăiește, se experimentează și se transformă într-o vocație.</p>",
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
        "imagine": "larisa-gaga.jpg",


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
        "imagine": "andreea-bitca.jpg",
    },
    {
        "nume": "Daniel Raduly",
        "materie": "Limba franceză",
        "descriere": "„Câte limbi cunoști, de atâtea ori ești om” spuneau odinioară învățații vremii. Astăzi e adevărat, mai mult ca niciodată! Vom înceta să tratăm limba franceză ca un simplă disciplină de studiu din orar și vom încerca să valorizăm din plin potențialul lingvistic al fiecăruia, nu doar pentru o comunicare  mai bună și mai diversificată, ci și pentru a profita de oportunități profesionale și educaționale, pentru un acces mai fidel la educație și cultură sau pentru o dezvoltare personală și cognitivă susținută. Vă aștept cu drag să lucrăm împreună și la activități extrașcolare, cum ar fi : Festivalul Francofoniei, Ziua Europeană a limbilor, Festivalul de muzică „Chants, sons sur scène” , Festivalul de colinde „Boule de neige” sau diversele concursuri : Olimpiade, Plurilingvism, Dialog Plurilingv. În pregătirea noastră, ne vom lăsa ghidați de CECRL (Cadrul European de Referință pentru Limbi) și ne vom inspira pe cât posibil din structura examenelor de DELF  (Diplôme d'études en langue française), la care vă recomand să participați!",
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
        "imagine": "papp-botond.jpg"
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
        "imagine": "andreea-focsan.JPG"
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
            {"nume": "Danci Dora-Elena",
             "performante": [
                {
                    "titlu": "Concursul Interjudețean de Matematică \"Matematica, de drag\"",
                    "locatie": "Bistrița",
                    "premiu": "Mențiune II"
                },
                {
                    "titlu": "Concursul Județean \"Dialog Cultural Plurilingv\"",
                    "locatie": "Secțiunea engleză",
                    "premiu": "Mențiune II"
                }
             ]},
            {"nume": "Fărcaș Bogdan"},
            {"nume": "Gligor Adriana-Emanuela",
             "performante": [
                {
                    "titlu": "Olimpiada Națională de Matematică",
                    "locatie": "etapa județeană",
                    "premiu": "Locul I"
                },
                {
                    "titlu": "Olimpiada Națională de Matematică",
                    "locatie": "Alba-Iulia, etapa națională",
                    "premiu": "Participare"
                },
                {
                    "titlu": "Olimpiada Națională de Limba și Literatura Română",
                    "locatie": "etapa județeană",
                    "premiu": "Locul II"
                },
                {
                    "titlu": "Concursul Interjudețean de Matematică \"Alexandru Papiu Ilarian\"",
                    "locatie": "nivel interjudețean",
                    "premiu": "Mențiune"
                },
                {
                    "titlu": "Concursul Interjudețean de Matematică \"Matematica, de drag\"",
                    "locatie": "Bistrița, nivel interjudețean",
                    "premiu": "Mențiune III"
                },
                {
                    "titlu": "Concursul Național de Fizică Evrika",
                    "locatie": "Brașov, nivel național",
                    "premiu": "Participare"
                },
                {
                    "titlu": "Concursul Interdisciplinar de Matematică și Fizică \"Vrănceanu-Procopiu\"",
                    "locatie": "etapa județeană",
                    "premiu": "Locul I"
                },
                {
                    "titlu": "Concursul Interdisciplinar de Matematică și Fizică \"Vrănceanu-Procopiu\"",
                    "locatie": "Bacău, etapa națională",
                    "premiu": "Participare"
                },
                {
                    "titlu": "Festivalul Francofoniei - ediția XVIII",
                    "locatie": "nivel județean",
                    "premiu": "Mențiune"
                }
             ]},
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
            {"nume": "Rus Daria-Ioana",
             "performante": [
                {
                    "titlu": "Concursul Național de Procese Simulate \"Matei Cantacuzino\"",
                    "locatie": "etapa națională",
                    "premiu": "Locul II"
                }
             ]},
            {"nume": "Rusu Mihai"},
            {"nume": "Stoica Dalia"},
            {"nume": "Varga Cezar-Andrei"},
            {"nume": "Vasinc Daniel",
             "performante": [
                {
                    "titlu": "AI For Good",
                    "locatie": "etapa națională",
                    "premiu": "Locul I + calificare la etapa internațională"
                }
             ]},
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
            {"nume": "Bálint Erick", "performante": [
                {"titlu": "Olimpiada Națională de Franceză", "locatie": "etapa județeană", "premiu": "Locul II"},
                {"titlu": "Concursul de Plurilingvism", "premiu": "Mențiune I"},
                {"titlu": "Concursul Dialog Plurilingv", "premiu": "Locul IV"}
            ]},
            {"nume": "Bereholschi Maia-Sofia"},
            {"nume": "Blaga Nadia Veronica"},
            {"nume": "Blănaru Sara",
             "performante": [
                {
                    "titlu": "Olimpiada Națională de Biologie",
                    "locatie": "etapa județeană",
                    "premiu": "Locul III"
                }
             ]},
            {"nume": "Bogdan Diana"},
            {"nume": "Chiriac Patricia-Mădălina"},
            {"nume": "Chirilean Alexia-Ioana"},
            {"nume": "Cîmpan Maria"},
            {"nume": "Cotoară Radu-Ioan"},
            {"nume": "Crăciun Iris-Maria"},
            {"nume": "Gherendi Sofia"},
            {"nume": "Lenard Alexia"},
            {"nume": "Maier Alisia Eliza"},
            {"nume": "Matei Irina",
             "performante": [
                {
                    "titlu": "Olimpiada Națională de Argumentare, Dezbatere și Gândire Critică \"Tinerii dezbat\"",
                    "locatie": "etapa județeană",
                    "premiu": "Locul II (echipă) + Mențiune (vorbitor)"
                }
             ]},
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
            {"nume": "Bumbac Ileana",
             "performante": [
                {
                    "titlu": "Olimpiada Națională de Limba Engleză",
                    "locatie": "etapa județeană",
                    "premiu": "Locul I"
                }
             ]},
            {"nume": "Bumbu Luca"},
            {"nume": "Colcer Sonia"},
            {"nume": "Coșarcă Alexandru",
             "performante": [
                {
                    "titlu": "Olimpiada lectura ca abilitate de viață (OLAV)",
                    "locatie": "etapa județeană",
                    "premiu": "Mențiune II"
                }
             ]},
            {"nume": "Cotoi Iulius", "performante": [{"titlu": "Olimpiada Națională de Biologie","locatie": "Tg. Mureș, etapa județeană","premiu": "Mențiune III" }]},
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
            {"nume": "Pop Sara", "performante": [
                {"titlu": "Campioana națională la categoria U17 feminin sezonul 2025/2026"},
                {"titlu": "Premiul «Cea mai bună coordonatoare la categoria U17 feminin sezonul 2025/2026»"}
            ]},
            {"nume": "Sabău Raul"},
            {"nume": "Șandru Octavian"},
            {"nume": "Szasz Roberta", "performante" : [{"titlu": "Olimpiada Națională de Biologie", "locatie": "Tg. Mureș, etapa județeană", "premiu": "Mențiune II"}, {"titlu": "Olimpiada Națională de Limba și literatura română", "locatie": "etapa județeană", "premiu": "Locul I"}, {"titlu": "Olimpiada Națională de Limba și literatura română", "locatie": "Botoșani, etapa națională", "premiu": "Premiu special la nivel național"}, {"titlu": "Olimpiada Interdisciplinară „Culturalitate și spiritualitate românească“", "locatie": "Tg. Mureș, etapa județeană", "premiu": "Premiul III"}]},
            {"nume": "Vasiliu Anca",
             "performante": [
                {
                    "titlu": "Olimpiada Națională de Chimie",
                    "locatie": "etapa județeană",
                    "premiu": "Locul I"
                }
             ]},
            {"nume": "Vidican Andreea"},
            {"nume": "Vașloban Maria"}
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
            {"nume": "Biriș Sergiu",
             "performante": [
                {
                    "titlu": "AI For Good",
                    "locatie": "etapa națională",
                    "premiu": "Locul I + calificare la etapa internațională"
                },
                {
                    "titlu": "Olimpiada Națională de Argumentare, Dezbatere și Gândire Critică \"Tinerii dezbat\"",
                    "locatie": "etapa județeană",
                    "premiu": "Locul I + calificare la etapa națională"
                }
             ]},
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
            },
            {
                "titlu": "Concursul Național ENROLL FOR FUN, ediția a VIII-a, secțiunea creații literare, limba engleză",
                "locatie": "Targu Mureș",
                "premiu": "Locul II"
            },
            {
                "titlu": "Olimpiada Județeană de Chimie",
                "locatie": "etapa județeană",
                "premiu": "Locul III"
            },
            {
                "titlu": "Maratonul de Educație Antreprenorială",
                "locatie": "etapa județeană",
                "premiu": "Locul I + calificare la etapa națională"
            }
             ]},
            {"nume": "Cucuiet Andrei"},
            {"nume": "David Aiana"},
            {"nume": "Ercean David"},
            {"nume": "Gherman Cezara"},
            {"nume": "Jovrea Ștefan",
             "performante": [
                {
                    "titlu": "Olimpiada Națională de Lingvistică",
                    "locatie": "etapa județeană",
                    "premiu": "Locul II"
                },
                {
                    "titlu": "Olimpiada Națională de Geografie",
                    "locatie": "etapa județeană",
                    "premiu": "Locul III"
                },
                {
                    "titlu": "Olimpiada Națională de Limba Franceză",
                    "locatie": "etapa județeană",
                    "premiu": "Locul IV"
                }
             ]},
            {"nume": "Lazăr Cristian",
             "performante": [
                {
                    "titlu": "Concursul județean de Matematică „Simon Petru“, ediția a XXIII-a",
                    "locatie": "Tg Mureș, Colegiul Național „Unirea“",
                    "premiu": "Locul II, secțiunea Matematică-informatică"                },
                {
                    "titlu": "Olimpiada Națională de Chimie",
                    "locatie": "etapa județeană",
                    "premiu": "Locul II"                }
             ]},
            {"nume": "Maier Alia"},
            {"nume": "Mitoșeriu David",
             "performante": [
                {
                    "titlu": "Concursul Național ENROLL FOR FUN, ediția a VII-a, secțiunea creații literare, limba engleză",
                    "locatie": "Baia Mare",
                    "premiu": "Locul II"
                },
                {
                    "titlu": "Concursul Național ENROLL FOR FUN, ediția a VIII-a, secțiunea creații literare, limba engleză",
                    "locatie": "Targu Mureș",
                    "premiu": "Locul II"
                },
                {
                    "titlu": "AI For Good",
                    "locatie": "etapa națională",
                    "premiu": "Locul I + calificare la etapa internațională"
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
                "premiu": "Premiul I cu punctaj maxim"
            },
            {
                "titlu": "Concursul „Marian Țarina“",
                "locatie": "Cluj Napoca",
                "premiu": "Premiul III"
            },
            {
                "titlu": "Concursul „Argument“",
                "locatie": "Baia Mare",
                "premiu": "Premiul III"
            },
            {
                "titlu": "Concursul Național de Matematică și Informatică „Grigore Moisil“",
                "locatie": "Cluj Napoca",
                "premiu": "Premiul II"
            },
            {
                "titlu": "Olimpiada Națională de Matematică",
                "locatie": "etapa județeană",
                "premiu": "Locul II + calificare la etapa națională"
            },
            {
                "titlu": "Olimpiada Națională de Matematică",
                "locatie": "etapa națională, Botoșani",
                "premiu": "Locul 8 în clasamentul național"
            },
            {
                "titlu": "Olimpiada Națională de Matematică",
                "locatie": "Alba Iulia ",
                "premiu": "Medalie de Argint  + calificare la baraj"
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
            {"nume": "Oaneș Sofia",
             "performante": [
                {
                    "titlu": "AI For Good",
                    "locatie": "etapa națională",
                    "premiu": "Locul I + calificare la etapa internațională"
                }
             ]},
            {"nume": "Paca Raoul",
             "performante": [
                {
                    "titlu": "Olimpiada Națională de Informatică",
                    "locatie": "Tg Mureș, etapa județeană",
                    "premiu": "Premiul III"
                }
            ]},
            {"nume": "Pantea Tudor",
             "performante": [
                {
                    "titlu": "AI For Good",
                    "locatie": "etapa națională",
                    "premiu": "Locul I + calificare la etapa internațională"
                },
                {
                    "titlu": "Olimpiada Națională de Argumentare, Dezbatere și Gândire Critică \"Tinerii dezbat\"",
                    "locatie": "etapa județeană",
                    "premiu": "Locul I + calificare la etapa națională"
                }
             ]},
            {"nume": "Someșan Adrian",
             "performante": [
                {
                    "titlu": "Maratonul de Educație Antreprenorială",
                    "locatie": "etapa județeană",
                    "premiu": "Locul I + calificare la etapa națională"
                }
             ]},
            {"nume": "Staicu Eric"},
            {"nume": "Stîngă David"},
            {"nume": "Stoica Andrei"},
            {"nume": "Suciu Iustina"},
            {"nume": "Trifan Raul"},
            {"nume": "Turdean Cleo",
             "performante": [
                {   "titlu": "Concursul Național ENROLL FOR FUN, ediția a VIII-a, secțiunea creații literare, limba engleză",
                    "locatie": "Targu Mureș",
                    "premiu": "Locul II"
                },
                {
                    "titlu": "AI For Good",
                    "locatie": "etapa națională",
                    "premiu": "Locul I + calificare la etapa internațională"
                },
                
             ]},
            {"nume": "Ungur Filip",
             "performante": [
                {
                    "titlu": "Olimpiada Națională de Argumentare, Dezbatere și Gândire Critică \"Tinerii dezbat\"",
                    "locatie": "etapa județeană",
                    "premiu": "Locul I + calificare la etapa națională"
                }
             ]}
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
