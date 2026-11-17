# ======================================================================
#   werkblad python: loops (while en for)
# ======================================================================
#
naam = "Jouw_naam"
#
#   HOE WERK JE HIER MEE?
#   1. Vul jouw naam hierboven in
#   2. Lees DEEL A (uitleg).
#   3. Ga naar DEEL B en vul de opdrachten in. Je vervangt overal
#      waar >> None << staat jouw antwoord of jouw code.
#   4. Start het programma met de ▶ knop rechts boven het scherm.
#      Het programma controleert je antwoorden.
#   5. Klopt iets niet? Verbeter je code en start opnieuw.
#   6. DEEL C (onderaan) hoef je niet te veranderen, dat zorgt dat alles werkt.
#
#   Zit je programma vast en stopt het niet meer? Dan zit er een oneindige
#   loop in. Druk op de stopknop (of Ctrl+C) en kijk je code nog eens na.
#
# ======================================================================


# ======================================================================
#   DEEL A: Uitleg
# ======================================================================
#
# --- 1. WAAROM LOOPS? -------------------------------------------------
#   Soms wil je iets vaker achter elkaar doen. Dat kun je uittypen:
#
#       print("Hallo")
#       print("Hallo")
#       print("Hallo")
#
#   Maar wat als je het 1000 keer wilt? Daarvoor bestaan loops 
#   (en functies). Python heeft twee soorten loops: while en for.
#
# --- 2. DE WHILE-LOOP: herhaal *zolang* iets waar is ------------------
#       teller = 0
#       while teller < 3: # <- de vraag
#           print("Hallo")
#           teller = teller + 1
#
#   Zo werkt het:
#   - Python checkt de vraag (teller < 3). Is die True? Dan voert hij het blok uit.
#   - Daarna springt hij terug naar boven en checkt de vraag opnieuw.
#   - Is de vraag False? Dan stopt de loop.
#
#   LET OP: verander je binnen de loop niets aan teller, dan blijft de vraag
#   altijd True en stopt de loop nooit. Dat heet een oneindige loop.
#
#   Handige afkorting: teller += 1 betekent hetzelfde als teller = teller + 1
#
# --- 3. DE FOR-LOOP: herhaal een vast aantal keer -----------------------
#       for i in range(3):
#           print("Hallo", i)
#.  
#   - i is de loopvariabele. Python maakt hem zelf en telt hem voor je op.
#   - range(3) geeft de getallen 0, 1, 2. 
#
#   Meer vormen van range:
#       range(5)          ->  0, 1, 2, 3, 4
#       range(2, 6)       ->  2, 3, 4, 5            (begin, einde: einde telt niet mee)
#       range(0, 10, 2)   ->  0, 2, 4, 6, 8         (begin, einde, stapgrootte)
#
# --- 4. EEN FOR-LOOP DOOR EEN LIJST ------------------------------------
#   Met een for-loop kun je alle waarden één voor één langs lopen:
#
#       cijfers = [6, 8, 4, 7]
#       len(cijfers)   # ->  4     (het aantal waarden in de lijst)
#
#       for cijfer in cijfers:
#           print(cijfer)
#
#   Dit print:  6   8   4   7
#
# --- 5. Voorbeeld         ----------------------------------------------
#   Je wilt een totaal bijhouden terwijl je door de loop gaat:
#
#       totaal = 0                       # <- begin voor de loop met 0
#       for cijfer in cijfers:
#           totaal = totaal + cijfer     # <- tel er in elke ronde iets bij op
#       print(totaal)                    # <- gebruik het resultaat NA de loop
#
#   Hetzelfde patroon werkt om te tellen:
#       aantal = 0
#       for cijfer in cijfers:
#           if cijfer >= 5.5:            <- if binnen een loop mag!
#               aantal = aantal + 1
#
# --- 6. FOR OF WHILE? ---------------------------------------------------
#   - Weet je van tevoren hoe vaak je iets moet doen (of heb je een lijst)? -> for
#   - Weet je dat niet en moet je doorgaan tot iets waar wordt?             -> while
#
# ======================================================================


# ======================================================================
#   DEEL B:  De opdrachten
# ======================================================================

# ----------------------------------------------------------------------
#   Opdracht 1
# ----------------------------------------------------------------------
# Lees deze code goed. De functie krijgt een getal n binnen
# en geeft een getal terug.
def som_van_range(n: int) -> int:
    totaal = 0
    for i in range(n):
        totaal = totaal + i
    return totaal

# Welk getal komt eruit bij elke waarde van n die je aan de functie geeft?
# Maak een voorspelling voordat je het test. Pak eventueel papier erbij.
# Vervang telkens >> None << door een getal.
antwoorden_opdracht_1 = {
    4: None,
    1: None,
    0: None,
    6: None,
}
# Had je een antwoord niet in één keer goed? schrijf hier onder wat je eerste gok was:
# ---------------------------------------------------------------------
# <ruimte voor jouw gemiste voorspellingen>
# ---------------------------------------------------------------------



# ----------------------------------------------------------------------
#   Opdracht 2
# ----------------------------------------------------------------------
# Deze functie begint bij 1 en verdubbelt telkens, tot de waarde
# de grens bereikt. Hij geeft terug hoeveel keer hij moest verdubbelen.
def verdubbel_tot(grens: int) -> int:
    waarde = 1
    stappen = 0
    while waarde < grens:
        waarde = waarde * 2
        stappen = stappen + 1
    return stappen

# Welk getal komt eruit bij elke grens?
# Tip: schrijf per ronde op wat waarde en stappen zijn.
antwoorden_opdracht_2 = {
    10: None,
    1: None,
    16: None,
    17: None,
}
# Had je een antwoord niet in één keer goed? schrijf hier onder wat je eerste gok was:
# ---------------------------------------------------------------------
# <ruimte voor jouw gemiste voorspellingen>
# ---------------------------------------------------------------------




# ----------------------------------------------------------------------
#   Opdracht 3
# ----------------------------------------------------------------------
# Je spaart voor een nieuwe telefoon. Je begint met 0 euro en spaart
# elke maand een vast bedrag. Hoeveel maanden duurt het voordat je
# minstens het doelbedrag hebt?
#   maanden_sparen(100, 25)  moet 4 teruggeven   (25, 50, 75, 100)
#
# Gebruik een while-loop. Je hebt twee variabelen nodig: het gespaarde
# bedrag en het aantal maanden.
def maanden_sparen(doel, per_maand):
    return None



# ----------------------------------------------------------------------
#   Opdracht 4
# ----------------------------------------------------------------------
# Schrijf een functie die telt hoeveel cijfers in de lijst
# een voldoende zijn (5.5 of hoger).
#   tel_voldoendes([4, 6, 8])  moet 2 teruggeven
#
# Gebruik een for-loop door de lijst en een if binnen de loop.
def tel_voldoendes(cijfers):
    return None



# ----------------------------------------------------------------------
#   Opdracht 5
# ----------------------------------------------------------------------
# Schrijf een functie die het gemiddelde van een lijst cijfers teruggeeft.
#   gemiddelde([6, 8])  moet 7 teruggeven
#
# - Tel eerst met een for-loop alle cijfers bij elkaar op.
# - Deel daarna door het aantal cijfers: len(cijfers)
# - Gebruik hier NIET de ingebouwde sum() functie, dat is te makkelijk. ;)
# - Is de lijst leeg? Geef dan 0 terug (delen door 0 kan niet).
def gemiddelde(cijfers):
    return None



# ----------------------------------------------------------------------
#   Opdracht 6
# ----------------------------------------------------------------------
# Schrijf een functie die een denneboom van sterretjes teruggeeft als tekst.
# je krijgt de hoogte van de boom mee als argument n. Voorbeeld voor n = 4:
#
#         *
#        ***
#       *****
#         |
#
# Tips:
# - Je mag een tekst vermenigvuldigen:  "*" * 3  geeft  "***"
# - Bouw de tekst op met een for-loop, maar dan met tekst in plaats van getallen.
def trap(n):
    return None



# ----------------------------------------------------------------------
#   Extra
# ----------------------------------------------------------------------
# Bedenk zelf een functie die een while-loop of een for-loop gebruikt.
#
# Beschrijving in woorden (schrijf het hier op):
#   ______________________________________________________________
#   ______________________________________________________________
#
def eigen_functie():
    print("(Je eigen opdracht is nog niet gemaakt.)")


# ======================================================================
#   DEEL C
#   >>> HIER HOEF JE NIETS TE VERANDEREN <<<
# ======================================================================

import sys


def lijn():
    print("-" * 64)


def kop(nummer):
    print()
    lijn()
    print(f"  opdracht {nummer}")
    lijn()


def normaliseer(tekst):
    """Haalt onzichtbare verschillen weg: spaties aan het eind van een regel
    en lege regels aan het begin en eind. Spaties vooraan blijven staan."""
    regels = tekst.strip("\n").split("\n")
    return "\n".join(regel.rstrip() for regel in regels)


def vergelijk(juist, gegeven) -> bool:
    """Is het antwoord van de leerling correct?"""
    if isinstance(juist, bool):
        return gegeven is juist
    if isinstance(juist, str):
        return isinstance(gegeven, str) and normaliseer(gegeven) == normaliseer(juist)
    return gegeven == juist


def beoordeel(nr, vraag, gegeven, juist) -> bool:
    """Geeft feedback op een vraag."""
    if gegeven is None:
        print(f"  Vraag {nr}: {vraag}  ->  nog niet ingevuld")
        return False
    if vergelijk(juist, gegeven):
        print(f"  Vraag {nr}: {vraag}  ->  goed!")
        return True
    print(f"  Vraag {nr}: {vraag}  ->  niet goed, kijk nog eens")
    return False


def probeer(functie, *argumenten):
    """Voert een functie van de leerling uit zonder dat het programma crasht.
    Stopt ook als de functie in een oneindige loop zit."""
    stappen = {"aantal": 0}

    def teller(frame, gebeurtenis, arg):
        stappen["aantal"] += 1
        if stappen["aantal"] > 200_000:
            raise RuntimeError("deze code blijft maar doorgaan (oneindige loop?)")
        return teller

    sys.settrace(teller)
    try:
        return functie(*argumenten)
    except Exception as fout:
        print(f"  💥 Je code geeft een foutmelding: {fout}")
        return None
    finally:
        sys.settrace(None)


def rond_af(fouten, goed_tekst, fout_tekst) -> bool:
    print()
    if fouten == 0:
        print(goed_tekst)
        return True
    print(fout_tekst)
    return False


def teken(tekst):
    """Print een tekst met meerdere regels, een beetje ingesprongen."""
    if not isinstance(tekst, str):
        print(f"    {tekst!r}")
        return
    for regel in tekst.split("\n"):
        print("    " + regel)


def beoordeel_voorspellingen(antwoorden, functie, naam_functie) -> bool:
    """Controleert een dictionary met voorspellingen."""
    fouten = 0
    for nr, (invoer, gegeven) in enumerate(antwoorden.items(), start=1):
        juist = functie(invoer)
        if not beoordeel(nr, f"{naam_functie}({invoer})", gegeven, juist):
            fouten += 1
    return rond_af(
        fouten,
        "  Alles correct! ",
        f"  Nog {fouten} vraag/vragen te gaan. Pas je antwoorden aan en start opnieuw.",
    )


def test_functie(functie, naam_functie, tests) -> bool:
    """Test een functie van de leerling met meerdere waarden."""
    fouten = 0
    for nr, (argumenten, juist) in enumerate(tests, start=1):
        uitkomst = probeer(functie, *argumenten)
        tekst = ", ".join(repr(a) for a in argumenten)
        if not beoordeel(nr, f"{naam_functie}({tekst}) moet {juist!r} zijn", uitkomst, juist):
            fouten += 1
    return rond_af(
        fouten,
        "  Alles correct! ",
        "  Niet alle testwaardes kloppen. Pas je code aan en start opnieuw.",
    )


def opdracht_1() -> bool:
    kop(1)
    print("  Lees de functie som_van_range() en voorspel wat eruit komt.\n")
    return beoordeel_voorspellingen(antwoorden_opdracht_1, som_van_range, "som_van_range")


def opdracht_2() -> bool:
    kop(2)
    print("  Lees de functie verdubbel_tot() en voorspel wat eruit komt.\n")
    return beoordeel_voorspellingen(antwoorden_opdracht_2, verdubbel_tot, "verdubbel_tot")


def opdracht_3() -> bool:
    kop(3)
    tests = [((100, 25), 4), ((100, 30), 4), ((0, 10), 0), ((10, 10), 1), ((95, 10), 10)]
    return test_functie(maanden_sparen, "maanden_sparen", tests)


def opdracht_4() -> bool:
    kop(4)
    tests = [(([4, 6, 8],), 2), (([],), 0), (([5.5, 5.4],), 1),
             (([10, 9, 8],), 3), (([1, 2, 3],), 0)]
    return test_functie(tel_voldoendes, "tel_voldoendes", tests)


def opdracht_5() -> bool:
    kop(5)
    tests = [(([6, 8],), 7), (([10],), 10), (([4, 5, 6, 7],), 5.5), (([],), 0)]
    return test_functie(gemiddelde, "gemiddelde", tests)


def opdracht_6() -> bool:
    kop(6)
    # n is de totale hoogte: (n - 1) regels met sterretjes en 1 regel met de stam.
    tests = [
        (2, "\n".join(["*",
                       "|"])),
        (3, "\n".join([" *",
                       "***",
                       " |"])),
        (4, "\n".join(["  *",
                       " ***",
                       "*****",
                       "  |"])),
        (6, "\n".join(["    *",
                       "   ***",
                       "  *****",
                       " *******",
                       "*********",
                       "    |"])),
    ]
    fouten = 0
    eerste_fout = None
    for nr, (n, juist) in enumerate(tests, start=1):
        uitkomst = probeer(trap, n)
        if not beoordeel(nr, f"trap({n})", uitkomst, juist):
            fouten += 1
            if eerste_fout is None and uitkomst is not None:
                eerste_fout = (n, uitkomst, juist)

    if eerste_fout is not None:
        n, uitkomst, juist = eerste_fout
        print(f"\n  Jouw boom voor n = {n}:")
        teken(uitkomst)
        print("  Dit had het moeten zijn:")
        teken(juist)

    gelukt = rond_af(
        fouten,
        "  Alles correct! ",
        "  Niet alle testwaardes kloppen. Pas je code aan en start opnieuw.",
    )
    if gelukt:
        print("  Een mooie boom, speciaal voor jou (n = 8):")
        teken(probeer(trap, 8))
    return gelukt


def start_spel():
    print()
    opdrachten = [opdracht_1, opdracht_2, opdracht_3, opdracht_4,
                  opdracht_5, opdracht_6, eigen_functie]
    for opdracht in opdrachten:
        if not opdracht():
            # break
            pass
        input("\n(druk op Enter om door te gaan naar de volgende opdracht...)")


if __name__ == "__main__":
    start_spel()