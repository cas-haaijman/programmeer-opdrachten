# ======================================================================
#   werkblad python
# ======================================================================
#
naam = "Jouw_naam"
#
#   HOE WERK JE HIER MEE?
#   1. Vul jouw naam hierboven in
#   2. Lees DEEL A (uitleg).
#   3. Ga naar DEEL B en vul de opdrachten in. Je vervangt overal
#      waar >> None << staat jouw antwoord of jouw code.
#   4. Start het programma met de ▶ knop rechts boven het scherm. Het spel controleert je antwoorden.
#   5. Klopt iets niet? Verbeter je code en start opnieuw.
#   6. DEEL C (onderaan) hoef je niet te veranderen, dat zorgt dat alles werkt
#
# ======================================================================

# ======================================================================
#   DEEL A: Uitleg
# ======================================================================
#
# --- 1. VARIABELEN -----------------------------------------------------
#       leeftijd = 16          (de variabele 'leeftijd' krijgt de waarde 16, een integer)
#       naam = "Sam"           (de variabele 'naam' krijgt de waarde "Sam", een string)
#       heeft_sleutel = True   (de variabele 'heeft_sleutel' krijgt de waarde True, een boolean)
#
# --- 2. VERGELIJKEN (geeft altijd True of False) ------------------------
#       a == b    is a gelijk aan b?
#       a != b    is a NIET gelijk aan b?
#       a > b     is a groter dan b?
#       a < b     is a kleiner dan b?
#       a >= b    is a groter dan of gelijk aan b?
#       a <= b    is a kleiner dan of gelijk aan b?
#
# --- 3. BOOLEAN OPERATORS: and, or, not --------------------------------
#       A and B   True als A en B beide waar zijn
#       A or B    True als MINSTENS ÉÉN van de twee waar is, dus ook als A en B waar zijn
#       not A     draait om: True wordt False, False wordt True
#
#   Voorbeeld uit het dagelijks leven:
#       "Je mag naar binnen als je een kaartje hebt EN je bent 12 of ouder."
#       mag_naar_binnen = (heeft_kaartje) and (leeftijd >= 12)
#
#
# --- 4. IF / ELIF / ELSE ------------------------------------------------
#   Met if laat je het programma een keuze maken.
#
#       if temperatuur > 30:
#           print("Te warm!")          <- wordt alleen uitgevoerd als de vraag True is
#       elif temperatuur < 5:
#           print("Te koud!")          <- wordt alleen uitgevoerd als de eerste vraag False was
#       else:
#           print("Lekker weer")       <- wordt uitgevoerd als alle vragen hierboven False waren
#
# ======================================================================

# ======================================================================
#   DEEL B:  De opdrachten
# ======================================================================

# ----------------------------------------------------------------------
#   Opdracht 1:  booleans
# ----------------------------------------------------------------------

# De volgende waarden worden opgeslagen in variabelen:
a = 5
b = 8
c = 5
x = True
y = False

# Wat is de uitkomst van elke expressie in het volgende record: True of False?
# Vervang telkens >> None << door >> True << of >> False <<. 
# Maak een voorspelling wat het antwoord zou moeten zijn voordat je het test.
antwoorden_deel1 = {
    "a == c": None,
    "not (a == b)": None,
    "a > b": False,
    "a <= c": None,
    "x and y": None,
    "x or y": None,
    "not x": None,
    "(a == c) and (b > a)": None,
    "(a > b) or (x == True)": None,
    "not (y or False)": None,
}
# Had je een antwoord niet in één keer goed? schrijf hier onder wat je eerste gok was:
# ---------------------------------------------------------------------
# <ruimte voor jouw gemiste voorspellingen>
# ---------------------------------------------------------------------



# ----------------------------------------------------------------------
#   opdracht 2
# ----------------------------------------------------------------------
# Lees deze code goed. De functie krijgt een temperatuur binnen
# en geeft een tekst terug.
def kantine(temperatuur) -> None | str:
    if temperatuur >= 30:
        return "ijsjes"

# Welke tekst komt eruit bij elke temperatuur?
# Schrijf je antwoord als tekst, bijvoorbeeld "ijsjes".
# Gebeurt er niets? Schrijf dan "niets".
antwoorden_deel2 = {
    25: None,
    35: None,
    30: None,
}

# ----------------------------------------------------------------------
#   Opdracht 3
# ----------------------------------------------------------------------


# Schrijf zelf een functie die True teruggeeft als iemand
#    JONGER dan 18 is, maar WEL een ID heeft.
# Vervang None achter return door jouw uitdrukking. 
# Het antwoord moet in één regel.
def jonger_dan_18_met_id(leeftijd: int, heeftID: bool) -> None | bool:
    return None



# ----------------------------------------------------------------------
#   opdracht 4
# ----------------------------------------------------------------------
def beoordeling(cijfer: int | float) -> str:
    if cijfer >= 8:
        return "super"
    elif cijfer >= 5.5:
        return "voldoende"
    else:
        return "onvoldoende"


# Welke tekst komt eruit bij elk cijfer?
# Kies uit: "super", "voldoende" of "onvoldoende"
antwoorden_deel4 = {
    7: None,
    4: None,
    9: None,
    5.5: None,
}


# ----------------------------------------------------------------------
#   opdracht 5
# ----------------------------------------------------------------------
# Schrijf een if / elif / else voor deze situatie:
#   - leeftijd kleiner dan 12          ->  "Kind"
#   - leeftijd van 12 t/m 17           ->  "Tiener"
#   - anders                           ->  "Volwassene"
#
# Vervang het stukje 'return None' door jouw eigen code.
def leeftijdsgroep(leeftijd) -> None | bool:
    return None

# ----------------------------------------------------------------------
#   Extra 1
# ----------------------------------------------------------------------
# Bedenk zelf een functie met minstens TWEE boolean operators (and, or, not)
# in één if-statement.
#
# Beschrijving in woorden (schrijf het hier op):
#   ______________________________________________________________
#   ______________________________________________________________
#
def eigen_functie():
    print("(Je eigen opdracht is nog niet gemaakt.)")

# ----------------------------------------------------------------------
#   Extra 2
# ----------------------------------------------------------------------
# Lees Deel C goed. Je mag nu de code van deel C veranderen
# Opdracht 1: Wat doet de code in de functie `vergelijk`?
# Opdracht 2: Zorg dat opdracht_1 "Alles correct!" zegt zonder dat je
#             de 10 vragen juist hoeft te beantwoorden.
# 

# ======================================================================
#   DEEL C
#   >>> HIER HOEF JE NIETS TE VERANDEREN <<<
# ======================================================================

def lijn() -> None:
    print("-" * 64)

def kop(nummer) -> None:
    print()
    lijn()
    print(f"  opdracht {nummer}")
    lijn()


def vergelijk(juist, gegeven) -> bool:
    """Is het antwoord van de leerling correct?"""
    if isinstance(juist, bool):
        return gegeven is juist
    if isinstance(juist, str):
        return isinstance(gegeven, str) and gegeven.strip().lower() == juist.lower()
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
    try:
        return functie(*argumenten)
    except Exception as fout:
        print(f"  💥 Je code geeft een foutmelding: {fout}")
        return None


def rond_af(fouten, goed_tekst, fout_tekst) -> bool:
    print()
    if fouten == 0:
        print(goed_tekst)
        return True
    print(fout_tekst)
    return False


def opdracht_1() -> bool:
    kop(1)
    fouten = 0
    for nr, (expressie, gegeven) in enumerate(antwoorden_deel1.items(), start=1):
        juist = eval(expressie)
        if not beoordeel(nr, expressie, gegeven, juist):
            fouten += 1
    return rond_af(
        fouten,
        "  Alles correct! ",
        f"  Nog {fouten} vraag/vragen te gaan. Pas je antwoorden aan en start opnieuw.",
    )


def opdracht_2() -> bool:
    kop(2)
    fouten = 0
    for nr, (temperatuur, gegeven) in enumerate(antwoorden_deel2.items(), start=1):
        juist = kantine(temperatuur)
        if juist is None:
            juist = "niets"
        if not beoordeel(nr, f"temperatuur = {temperatuur}", gegeven, juist):
            fouten += 1
    return rond_af(
            fouten,
            "  Alles correct! ",
            f"  Nog {fouten} vraag/vragen te gaan. Pas je antwoorden aan en start opnieuw.",
        )

def opdracht_3() -> bool:
    kop(3)
    fouten = 0
    tests = [(16, True, True), (20, True, False), (16, False, False), (20, False, False)]
    for leeftijd_t, id_t, verwacht in tests:
        uitkomst = probeer(jonger_dan_18_met_id, leeftijd_t, id_t)
        if uitkomst is None:
            fouten += 1
            print(f"  Leerling van {leeftijd_t} met ID={id_t}: nog niets teruggegeven")
        elif uitkomst is verwacht:
            print(f"  Leerling van {leeftijd_t} met ID={id_t}: goed ({uitkomst})")
        else:
            fouten += 1
            print(f"  Leerling van {leeftijd_t} met ID={id_t}: jouw code zegt {uitkomst}")
    return rond_af(
            fouten,
            "  Correct! ",
            f"  Niet alle testwaardes kloppen. Pas je antwoord aan en start opnieuw.",
        )
 


def opdracht_4() -> bool:
    kop(4)
    fouten = 0
    for nr, (cijfer, gegeven) in enumerate(antwoorden_deel4.items(), start=1):
        juist = beoordeling(cijfer)
        if not beoordeel(nr, f"cijfer = {cijfer}", gegeven, juist):
            fouten += 1
    return rond_af(
            fouten,
            "  Alles correct! ",
            f"  Nog {fouten} vraag/vragen te gaan. Pas je antwoorden aan en start opnieuw.",
        )


def opdracht_5() -> bool:
    kop(5)
    tests = [(5, "Kind"), (11, "Kind"), (12, "Tiener"), (17, "Tiener"),
             (18, "Volwassene"), (40, "Volwassene")]
    fouten = 0
    for nr, (leeftijd_t, juist) in enumerate(tests, start=1):
        uitkomst = probeer(leeftijdsgroep, leeftijd_t)
        if not beoordeel(nr, f"leeftijd = {leeftijd_t} (moet \"{juist}\" zijn)", uitkomst, juist):
            fouten += 1
    return rond_af(
            fouten,
            "  Alles correct! ",
            f"  Nog {fouten} vraag/vragen te gaan. Pas je antwoorden aan en start opnieuw.",
        )


def start_spel() -> None:
    print()
    
    opdrachten = [opdracht_1, opdracht_2, opdracht_3, opdracht_4, opdracht_5, eigen_functie]
    for opdracht in opdrachten:
        if not opdracht():
            break
        input("\n(druk op Enter om door te gaan naar de volgende opdracht...)")

if __name__ == "__main__":
    start_spel()
