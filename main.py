""" Melanie Egas
Doel programma: Welkom in mijn restaurant!
Als u in Almere woont kunt u bij eten bestellen.
Uw gegevens worden gevraagd voor de bestelling.
Er wordt gevraagt wat u wilt bestellen.
Het programma laat u weten wat u besteld heeft en wat de totaal prijs is.
Vervolgens laat het programma weten hoe laat het eten bezorgd word.
"""
import time
import datetime


def welkom():
    """Welkomsscherm. Geeft de gebruiker de keuze uit reserveren of bezorgen"""

    b_lijst = ["B", "b", "bestellen"]
    r_lijst = ["R", "r", "reserveren"]
    while True:
        print("Welkom bij Melanie's restaurant!")
        time.sleep(1)
        print(
            "-" * 20 + "HOOFDMENU" + "-" * 20 + "\n"
                                                "\t(B) Bezorgen\n"  # "
                                                "\t(R) Reserveren\n" + "_" * 49
        )
        keuze = str(input("Wilt u laten bezorgen of een tafel reserveren?>>>"))
        if keuze in b_lijst:
            bezorgen()
            break
        elif keuze in r_lijst:
            reserveren()
            break
        else:
            print(f"ONBEKENDE KEUZE: {keuze}. "
                  f"Probeert u het alstublieft opnieuw.")
            time.sleep(2)


def bezorgen():
    """Als de gebruiker voor bezorgen kiest word deze functie gestart."""
    postcode_bezorggebied = [
        1300,
        1301,
        1302,
        1303,
        1305,
        1309,
        1311,
        1312,
        1313,
        1314,
        1315,
        1316,
        1317,
        1318,
        1319,
        1320,
        1321,
        1322,
        1323,
        1324,
        1325,
        1326,
        1327,
        1328,
        1329,
        1331,
        1332,
        1333,
        1334,
        1335,
        1336,
        1338,
        1339,
        1341,
        1343,
        1349,
        1351,
        1352,
        1353,
        1354,
        1355,
        1356,
        1357,
        1358,
        1359,
        1361,
        1362,
        1363,
    ]
    while True:
        print("\n" * 15)
        print("U heeft gekozen voor bezorging\n")
        time.sleep(1)
        print(
            "Let op, wij bezorgen alleen in Almere. "
            "Wat is uw postcode (alleen cijfers)?"
        )
        global postcode_klant
        postcode_klant = int(input(">>>"))
        if (
                postcode_klant in postcode_bezorggebied
        ):  # Controleert of er bij de klant bezorgd kan worden
            print("Wij bezorgen bij u!")
            time.sleep(1)
            klant_info()
            break
        else:
            print("Helaas, wij bezorgen niet bij u. \n"
                  "U wordt teruggestuurd naar het hoofdmenu"
                  )
        time.sleep(1)
        welkom()
        time.sleep(1)
        break


def klant_info():
    """Deze functie word opgeroepen als er bij de gebruiker bezorgd kan worden.
    Vraagt om de gegevens van de gebruiker voor bezorging"""
    naam_klant = str(input("Wat is uw achternaam?\n>>>"))
    straatnaam_klant = str(input("Wat is uw straatnaam?\n>>>"))
    huisnummer_klant = str(input("Wat is huisnummer + "
                                 "eventuele toevoegingen?\n>>>"))
    telefoonnummer_klant = int(input("Wat is uw telefoonnummer?\n>>>"))
    print(f"-" * 20 + "Wij hebben de volgende gegevens van u ontvangen" +
          "-" * 20)
    print(
        f""
        f" naam: {naam_klant} \n"
        f" straatnaam: {straatnaam_klant} \n"
        f" huisnummer + toevoeging: {huisnummer_klant} \n"
        f" postcode: {postcode_klant} \n"
        f" telefoonnummer: {telefoonnummer_klant} \n"
    )
    check_gegevens = int(input("Kloppen deze gegevens? JA(1) NEE(2)>>>"))
    if check_gegevens == 1:
        time.sleep(2)
        bestelling_plaatsen()
    elif check_gegevens == 2:
        klant_info()
    else:
        print(
            f" KLANT GEGEVENS ONBEKENDE KEUZE: {check_gegevens}. "
            f"Probeert u het alstublieft opnieuw."
        )


def reserveren():
    """Deze functie word gestart als de gebruiker kiest voor reserveren"""
    while True:
        print(
            "Helaas. Ivm met de huidige corona maatregelen van"
            " de overheid zijn wij gesloten voor reserveringen. "
            "Wij bezorgen wel!"
        )
        time.sleep(4)
        welkom()


def bestelling_plaatsen():
    """Deze functie laat het menu zien en verwerkt de invoer van de gebruiker.
    Ook wordt er weergegeven wat de totaal prijs is en hoe laat de gebruiker
    de bestelling kan verwachten."""
    aflever_moment = datetime.datetime.now() + datetime.timedelta(minutes=30)
    menu_lijst = [
        ["1.", "Patat", float(3.45)],
        ["2.", "Pizza", float(5.19)],
        ["3.", "Hamburger", float(4.35)],
        [
            "4.",
            "Cola",
            float(1.75),
        ],
        ["5.", "Bier", float(1.95)],
        ["6.", "Cheesecake", float(3.75)],
    ]
    totaal_lijst = []
    artikel_lijst = []

    print("-" * 20 + "MENUKAART" + "-" * 20)
    for i in range(len(menu_lijst)):
        print(f"{(menu_lijst[i][0])} {(menu_lijst[i][1])}\n "
              f"€ {(menu_lijst[i][2])}")
        print("-" * 50)
    while True:
        keuze = int(input("\nWat wilt u bestellen? \n>>>")) - 1
        aantal = int(input("\nHoe veel porties wilt u?\n>>>"))
        toevoeg_lijst = ["1", "j", "ja", "yes", "y"]
        totaal_lijst.append(menu_lijst[keuze][2] * aantal)
        artikel_lijst.extend([[menu_lijst[keuze][1], aantal]])
        toevoegen = (input("Wilt u nog meer bestellen JA (1) NEE (2)")).lower()
        if toevoegen in toevoeg_lijst:
            pass
        else:
            break

    totaal_tekst = sum(totaal_lijst)
    print(
        "-" * 33 + "Bedankt "
                   "voor uw bestelling!" + "-" * 32 +
        "\nU Heeft het volgende besteld:\n"
    )
    for i in range(len(artikel_lijst)):
        print(f"{(artikel_lijst[i][1])} x {(artikel_lijst[i][0])}")
    print("-" * 94)

    print(
        f" De totaal prijs van uw bestelling is: {totaal_tekst:.2f} euro "
        f"\n \n" + "-" * 20 +
        "Wij bezorgen uw bestelling op " +
        (aflever_moment.strftime("%d-%m-%Y")) +
        " rond " + (
                aflever_moment.strftime("%H:%M:%S") + "-" * 20
        )  # Het prog laat de gebruiker weten hoelaat de bestelling komt
    )


welkom()