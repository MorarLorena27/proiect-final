"""
PROIECT: ANALIZOR TEXT(Opțiunea C)
Proirct realizat de: Morar Lorena-Alexandra
"""

# Variabila globala care retine textul incarcat in memorie
text_curent = ""


# ==========================================
# FUNCTII DE INCARCARE SI ANALIZA BAZA
# ==========================================

def incarca_text():
    """
    Incarca un text pentru analiza .
    """
    global text_curent

    print("\n=== INCARCARE TEXT ===")
    print("1. Introducere manuala ")
    print("2. Text exemplu predefinit")

    optiune = input("Alegeti optiunea: ")

    if optiune == "1":
        print("Introduceti textul (tastati 'GATA' pe o linie noua pentru a termina):")
        linii = []
        while True:
            linie = input()
            if linie == "GATA":
                break
            linii.append(linie)

        text_curent = ""
        i = 0
        while i < len(linii):
            text_curent = text_curent + linii[i] + "\n"
            i = i + 1

    elif optiune == "2":
        text_curent = """Programarea este arta de a instrui calculatoarele sa execute sarcini.
Limbajul Python este unul dintre cele mai populare limbaje de programare din lume.
Python este apreciat pentru sintaxa sa clara si usurinta invatarii.

Algoritmii sunt pasi logici pentru rezolvarea problemelor. Un algoritm bun este eficient si corect. Structurile de date organizeaza informatiile pentru acces rapid.

In acest curs am studiat sortarea, cautarea si diverse tehnici algoritmice.
Greedy este o tehnica care alege mereu optiunea local optima. Divide et Impera imparte problemele in subprobleme mai mici.

Programarea necesita practica si rabdare. Fiecare proiect ne ajuta sa invatam ceva nou."""

        print(f"\nText incarcat: {len(text_curent)} caractere")
    else:
        print("Optiune invalida!")



# ==========================================
# FUNCTII UTILITARE (EXISTENTE)
# ==========================================

def extrage_cuvinte(text):
    """
    Extrage cuvintele din text, curatate de punctuatie.
    """
    # Inlocuim caracterele speciale cu spatii
    text_curat = ""
    i = 0
    while i < len(text):
        caracter = text[i]
        if caracter.isalnum() or caracter == " ":
            text_curat = text_curat + caracter.lower()
        else:
            text_curat = text_curat + " "
        i = i + 1

    # Impartim in cuvinte
    cuvinte = []
    cuvant_curent = ""

    i = 0
    while i < len(text_curat):
        if text_curat[i] != " ":
            cuvant_curent = cuvant_curent + text_curat[i]
        else:
            if len(cuvant_curent) > 0:
                cuvinte.append(cuvant_curent)
                cuvant_curent = ""
        i = i + 1

    if len(cuvant_curent) > 0:
        cuvinte.append(cuvant_curent)

    return cuvinte


def numar_propozitii(text):
    """Numara propozitiile bazat pe semnele de punctuatie (. ! ?)."""
    numar = 0
    i = 0
    while i < len(text):
        if text[i] in ".!?":
            numar = numar + 1
        i = i + 1

    if numar == 0 and len(text) > 0:
        numar = 1
    return numar


def numar_paragrafe(text):
    """Numara paragrafele din text."""
    paragrafe = 0
    in_paragraf = False

    i = 0
    while i < len(text):
        if text[i] != "\n" and text[i] != " ":
            if not in_paragraf:
                in_paragraf = True
                paragrafe = paragrafe + 1
        elif text[i] == "\n":
            # Verificam daca urmeaza o linie goala
            if i + 1 < len(text) and text[i + 1] == "\n":
                in_paragraf = False
        i = i + 1
    return paragrafe



def statistici_de_baza():
    """Afiseaza statisticile de baza ale textului"""
    global text_curent

    if len(text_curent) == 0:
        print("\nNu exista text incarcat!")
        return

    cuvinte = extrage_cuvinte(text_curent)

    print("\n=== STATISTICI TEXT ===")
    print(f"Numar caractere (cu spatii): {len(text_curent)}")

    # Caractere fara spatii
    caractere_fara_spatii = 0
    i = 0
    while i < len(text_curent):
        if text_curent[i] not in " \n\t":
            caractere_fara_spatii =caractere_fara_spatii + 1
        i =i + 1

    print(f"Numar caractere (fara spatii): {caractere_fara_spatii}")
    print(f"Numar cuvinte: {len(cuvinte)}")
    print(f"Numar propozitii: {numar_propozitii(text_curent)}")
    print(f"Numar paragrafe: {numar_paragrafe(text_curent)}")

    # Lungime medie cuvant
    if len(cuvinte) > 0:
        suma_lungimi = 0
        i = 0
        while i < len(cuvinte):
            suma_lungimi =suma_lungimi + len(cuvinte[i])
            i =i + 1
        medie = suma_lungimi / len(cuvinte)
        print(f"Lungime medie cuvant: {medie:.1f} caractere")
    #Cuvinte per propozitie
    n_prop = numar_propozitii(text_curent)
    if n_prop > 0:
        cuvinte_per_prop = len(cuvinte) / n_prop
        print(f"Cuvinte per propozitie {medie}: {cuvinte_per_prop:.1f}")


def frecventa_cuvinte():
    """Analizeaza frecventa cuvintelor si afiseaza top cele mai folosite."""
    global text_curent
    if len(text_curent) == 0:
        print("\nNu exista text incarcat!")
        return

    cuvinte = extrage_cuvinte(text_curent)

    #Construim dictionarul de frecvente
    frecvente = {}

    i = 0
    while i < len(cuvinte):
        cuvant = cuvinte[i]
        if cuvant in frecvente:
            frecvente[cuvant] = frecvente[cuvant] + 1
        else:
            frecvente[cuvant] = 1
        i = i + 1

    # Convertim in lista pentru sortare
    lista_frecvente = []
    for cuvant in frecvente:
        lista_frecvente.append((cuvant, frecvente[cuvant]))

    # Sortam descrescator dupa frecventa (bubble sort)
    n = len(lista_frecvente)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if lista_frecvente[j][1] < lista_frecvente[j + 1][1]:
                lista_frecvente[j], lista_frecvente[j + 1] = lista_frecvente[j + 1], lista_frecvente[j]
            j =j + 1
        i =i + 1

    print("\n=== TOP 15 CUVINTE FRECVENTE ===")
    limita = 15
    if len(lista_frecvente) < 15:
        limita = len(lista_frecvente)

    if limita > 0 and lista_frecvente[0][1] > 0:
        val_max = lista_frecvente[0][1]
        i=0
        while i < limita:
            cuvant = lista_frecvente[i][0]
            frecv = lista_frecvente[i][1]

            if len(cuvant) > 15:
                cuvant = cuvant[0:12] + "..."

            lungime = int(frecv*30/val_max)
            bara = "█" * lungime

            print(f"{i + 1:2}. {cuvant:15}| {bara}({frecv})")
            i = i + 1


def histograma_lungimi_cuvinte():
    """Afiseaza o histograma a lungimilor cuvintelor."""
    global text_curent
    if len(text_curent) == 0:
        print("\nNu exista text incarcat!")
        return

    cuvinte = extrage_cuvinte(text_curent)
    #Grupam pe lungimi
    lungimi = {}

    i = 0
    while i < len(cuvinte):
        lung = len(cuvinte[i])
        if lung in lungimi:
            lungimi[lung] =lungimi[lung] + 1
        else:
            lungimi[lung] = 1
        i =i + 1

    # Gasim min si max lungime
    lung_min = 100
    lung_max = 0
    for lung in lungimi:
        if lung < lung_min:
            lung_min = lung
        if lung > lung_max:
            lung_max = lung

    # Gasim frecventa maxima
    freq_max = 0
    for lung in lungimi:
        if lungimi[lung] > freq_max:
            freq_max = lungimi[lung]

    print("\n=== HISTOGRAMA LUNGIMI CUVINTE ===")
    print()

    lung = lung_min
    while lung <= lung_max:
        if lung in lungimi:
            frecv = lungimi[lung]
        else:
            frecv = 0

        if freq_max > 0:
            lungime_bara = int(frecv * 40 / freq_max)
        else:
            lungime_bara = 0

        bara = "█" * lungime_bara
        print(f"{lung:2} caractere | {bara}({frecv})")
        lung = lung + 1


def cauta_in_text():
    """Cauta un cuvant sau o fraza in text ."""
    global text_curent
    if len(text_curent) == 0:
        print("\nNu exista text incarcat!")
        return

    print("\n=== CAUTARE IN TEXT ===")
    termen = input("\nIntroduceti termenul de cautat: ").lower()
    text_lower = text_curent.lower()

    #Numaram aparitiile
    numar = 0
    pozitii = []
    i = 0
    while i <= len(text_lower) - len(termen):
        # Verificam daca gasim termenul la pozitia i
        gasit = True
        j = 0
        while j < len(termen) and gasit:
            if text_lower[i + j] != termen[j]:
                gasit = False
            j = j + 1
        if gasit:
            numar = numar + 1
            pozitii.append(i)
        i = i + 1
    print(f"\nTermenul '{termen}' apare de {numar} ori.")
    if numar > 0 and numar <= 5:
        print("Context:")
        i = 0
        while i < len(pozitii):
            # Afisam context in jurul aparitiei
            start = pozitii[i] - 30
            if start < 0:
                start = 0
            sfarsit = pozitii[i] + len(termen) + 30
            if sfarsit > len(text_curent):
                sfarsit = len(text_curent)
            context = text_curent[start:sfarsit].replace("\n", " ")
            print(f"  ...{context}...")
            i = i + 1


# ==========================================
# FUNCTIONALITATI SUPLIMENTARE (NOI)
# ==========================================

def cautare_cuvinte_dupa_inceput():
    """
    [FUNCTIONALITATE 1]
    Permite utilizatorului sa introduca un prefix (ex: 'pro') si afiseaza
    toate cuvintele din text care incep cu acele litere.
    Indeplineste cerinta de 'Mecanisme imbunatatite de cautare'.
    """
    global text_curent
    if len(text_curent) == 0:
        print("\n[!] Nu exista text incarcat!")
        return

    cuvinte = extrage_cuvinte(text_curent)
    prefix = input("\nIntroduceti inceputul cuvantului (prefix): ").lower()

    # Folosim un set pentru a nu afisa dubluri (ex: daca 'programare' apare de 2 ori)
    cuvinte_gasite = []

    i = 0
    while i < len(cuvinte):
        # Verificam daca cuvantul incepe cu prefixul dat
        if cuvinte[i].startswith(prefix):
            # Adaugam in lista doar daca nu exista deja
            if cuvinte[i] not in cuvinte_gasite:
                cuvinte_gasite.append(cuvinte[i])
        i += 1

    print(f"\n=== CUVINTE CARE INCEP CU '{prefix}' ===")
    if len(cuvinte_gasite) == 0:
        print("Nu s-au gasit cuvinte.")
    else:
        # Le afisam
        k = 0
        while k < len(cuvinte_gasite):
            print(f"- {cuvinte_gasite[k]}")
            k += 1


def analiza_diversitate_lexicala():
    """
    [FUNCTIONALITATE 2 ]
    Calculeaza diversitatea vocabularului (Lexical Diversity).
    Numara cuvintele unice si face raportul fata de totalul cuvintelor.
    Un scor mic inseamna text repetitiv. Un scor mare inseamna text bogat.
    """
    global text_curent

    # Validare text
    if len(text_curent) == 0:
        print("\n[!] Nu exista text incarcat!")
        return

    # Obtinem cuvintele
    cuvinte = extrage_cuvinte(text_curent)
    total_cuvinte = len(cuvinte)

    if total_cuvinte == 0:
        print("\nTextul nu contine cuvinte valide.")
        return

    # Gasim cuvintele unice (Manual, fara functia set() pentru a fi explicit)
    cuvinte_unice = []
    i = 0
    while i < total_cuvinte:
        cuvant = cuvinte[i]

        # Verificam daca am mai intalnit acest cuvant
        deja_exista = False
        k = 0
        while k < len(cuvinte_unice):
            if cuvinte_unice[k] == cuvant:
                deja_exista = True
            k += 1

        if not deja_exista:
            cuvinte_unice.append(cuvant)

        i += 1

    nr_unice = len(cuvinte_unice)

    # Calculam procentul (Diversitatea)
    # Formula: (Cuvinte Unice / Total Cuvinte) * 100
    diversitate = (nr_unice / total_cuvinte) * 100

    print("\n=== ANALIZA DIVERSITATE LEXICALA ===")
    print(f"Total cuvinte: {total_cuvinte}")
    print(f"Cuvinte unice: {nr_unice}")
    print(f"Scor Diversitate: {diversitate:.2f}%")

    print("\nInterpretare:")
    if diversitate < 30:
        print("-> Text REPETITIV (vocabular restrans).")
    elif diversitate < 60:
        print("-> Text ECHILIBRAT (folosire moderata a cuvintelor).")
    else:
        print("-> Text BOGAT (vocabular variat).")


def inlocuire_cuvant():
    """
    [FUNCTIONALITATE 3]
    Cauta un cuvant in text si il inlocuieste cu altul specificat.
    Aceasta modifica variabila globala 'text_curent'.
    Demonstreaza modificarea datelor.
    """
    global text_curent
    if len(text_curent) == 0:
        print("\n[!] Nu exista text incarcat!")
        return

    print("\n=== INLOCUIRE CUVANT ===")
    tinta = input("Ce cuvant doriti sa inlocuiti? : ")

    # Verificam daca exista
    if tinta not in text_curent:
        print(f"Cuvantul '{tinta}' nu a fost gasit in text.")
        return

    nou = input(f"Cu ce doriti sa inlocuiti '{tinta}'? : ")

    # Numaram aparitiile inainte de inlocuire
    nr_aparitii = text_curent.count(tinta)

    # Realizam inlocuirea
    text_curent = text_curent.replace(tinta, nou)

    print(f"\n[Succes] S-au efectuat {nr_aparitii} inlocuiri.")
    print("Puteti alege optiunea 'Statistici de baza' pentru a vedea noile date.")


def cea_mai_lunga_propozitie():
    """
    [FUNCTIONALITATE 4]
    Identifica si afiseaza propozitia cu cele mai multe cuvinte.
    Parcurge textul, separa propozitiile si le numara cuvintele.
    """
    global text_curent

    if len(text_curent) == 0:
        print("\n[!] Nu exista text incarcat!")
        return

    print("\n=== CEA MAI LUNGA PROPOZITIE ===")

    propozitie_curenta = ""
    max_cuvinte = 0
    propozitie_castigatoare = ""

    i = 0
    while i < len(text_curent):
        caracter = text_curent[i]
        propozitie_curenta = propozitie_curenta + caracter

        # Verificam finalul de propozitie sau text
        if caracter in ".!?" or i == len(text_curent) - 1:

            propozitie_curata = propozitie_curenta.strip()
            cuvinte_prop = extrage_cuvinte(propozitie_curata)
            nr_cuvinte = len(cuvinte_prop)

            if nr_cuvinte > max_cuvinte:
                max_cuvinte = nr_cuvinte
                propozitie_castigatoare = propozitie_curata

            propozitie_curenta = ""

        i += 1

    if max_cuvinte > 0:
        print(f"Cea mai lunga propozitie are {max_cuvinte} cuvinte:")
        print(f"-> \"{propozitie_castigatoare}\"")
    else:
        print("Nu s-au putut identifica propozitii valide.")


# ==========================================
# MENIU PRINCIPAL
# ==========================================

def meniu_principal():
    """Gestioneaza interactiunea cu utilizatorul si ruleaza programul."""
    ruleaza = True

    while ruleaza:
        print("\n" + "=" * 50)
        print("       ANALIZOR TEXT")
        print("=" * 50)
        print("1. Incarca text")
        print("2. Statistici de baza")
        print("3. Frecventa cuvinte")
        print("4. Histograma lungimi cuvinte")
        print("5. Cauta in text")
        print("-" * 50)
        print("6. [NOU] Cautare cuvinte dupa inceput")
        print("7. [NOU] Analiza Diversitate Lexicala")
        print("8. [NOU] Inlocuire Cuvant in Text")
        print("9. [NOU] Cea Mai Lunga Propozitie")
        print("-" * 50)
        print("0. Iesire")
        print("=" * 50)

        optiune = input("Alegeti optiunea: ")

        if optiune == "1":
            incarca_text()
        elif optiune == "2":
            statistici_de_baza()
        elif optiune == "3":
            frecventa_cuvinte()
        elif optiune == "4":
            histograma_lungimi_cuvinte()
        elif optiune == "5":
            cauta_in_text()
        elif optiune == "6":
            cautare_cuvinte_dupa_inceput()
        elif optiune == "7":
            analiza_diversitate_lexicala()
        elif optiune == "8":
            inlocuire_cuvant()
        elif optiune == "9":
            cea_mai_lunga_propozitie()
        elif optiune == "0":
            print("\nLa revedere!")
            ruleaza = False
        else:
            print("Optiune invalida!")


# Pornire aplicatie
if __name__ == "__main__":
    meniu_principal()