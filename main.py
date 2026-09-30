# ==========================================
# TASK MASTER
# ==========================================

fil_namn = "uppgifter.txt"


# ==========================================
# FILHANTERING
# ==========================================

def las_fran_fil():
    uppgifter = []

    try:
        # Öppnar filen och läser alla sparade tasks
        with open(fil_namn, "r", encoding="utf-8") as fil:
            rader = fil.readlines()

        # Går igenom varje rad i filen
        for rad in rader:
            rad = rad.strip()

            if rad != "":
                delar = rad.split("|")

                # Varje rad ska innehålla:
                # id | uppgift | prioritet | klar
                if len(delar) == 4:

                    try:
                        uppgift = {
                            "id": int(delar[0]),
                            "uppgift": delar[1],
                            "prioritet": delar[2],
                            "klar": delar[3] == "True"
                        }

                        uppgifter.append(uppgift)

                    except ValueError:
                        print(
                            "En rad i filen hade fel format "
                            "och hoppades över."
                        )

    except FileNotFoundError:
        # Första gången programmet körs
        # finns kanske inte filen ännu
        print(
            "Ingen sparad fil hittades. "
            "En ny lista skapas."
        )

    except OSError:
        print(
            "Ett fel uppstod när filen skulle läsas."
        )

    return uppgifter


def spara_till_fil(uppgifter):

    try:
        # "w" skriver den aktuella listan till filen
        with open(fil_namn, "w", encoding="utf-8") as fil:

            for uppgift in uppgifter:

                fil.write(
                    f'{uppgift["id"]}|'
                    f'{uppgift["uppgift"]}|'
                    f'{uppgift["prioritet"]}|'
                    f'{uppgift["klar"]}\n'
                )

    except OSError:
        print(
            "Ett fel uppstod när uppgifterna skulle sparas."
        )


# ==========================================
# DATA & LOGIK
# ==========================================

def lagg_till_uppgift(uppgifter):

    # Frågar vad användaren vill göra
    while True:

        namn = input(
            "Vad ska du göra? "
        ).strip()

        if namn != "":
            break

        print(
            "Fel! Uppgiften får inte vara tom."
        )

    # Frågar efter prioritet
    while True:

        prioritet = input(
            "Prioritet (Hög/Medium/Låg): "
        ).strip().capitalize()

        if prioritet in ["Hög", "Medium", "Låg"]:
            break

        print(
            "Fel! Välj Hög, Medium eller Låg."
        )

    # Skapar nytt ID
    if len(uppgifter) == 0:

        nytt_id = 1

    else:

        nytt_id = max(
            uppgift["id"]
            for uppgift in uppgifter
        ) + 1

    # Skapar tasken som en dictionary
    ny_uppgift = {
        "id": nytt_id,
        "uppgift": namn,
        "prioritet": prioritet,
        "klar": False
    }

    # Lägger tasken i listan
    uppgifter.append(ny_uppgift)

    # SPARAR DIREKT TILL FIL
    spara_till_fil(uppgifter)

    print(
        "Tasken har lagts till och sparats!"
    )


def lagg_till_flera_uppgifter(uppgifter, antal):

    for i in range(antal):

        print(
            f"\n--- TASK {i + 1} ---"
        )

        lagg_till_uppgift(
            uppgifter
        )


# ==========================================
# PRIORITERING
# ==========================================

def prioriterings_ordning(uppgift):

    # Hög visas först
    if uppgift["prioritet"] == "Hög":
        return 1

    # Medium visas efter Hög
    elif uppgift["prioritet"] == "Medium":
        return 2

    # Låg visas sist
    else:
        return 3


# ==========================================
# VISA ALLA TASKS
# ==========================================

def visa_alla_uppgifter(uppgifter):

    # Om listan är tom
    if len(uppgifter) == 0:

        print(
            "\nInga uppgifter hittades."
        )

        return

    # Sorterar efter prioritet
    sorterade_uppgifter = sorted(
        uppgifter,
        key=prioriterings_ordning
    )

    print(
        "\n--- DINA TASKS ---"
    )

    for uppgift in sorterade_uppgifter:

        if uppgift["klar"]:
            status = "KLAR ✓"

        else:
            status = "Ej klar"

        print(
            f'ID: {uppgift["id"]} | '
            f'{uppgift["uppgift"]} | '
            f'{uppgift["prioritet"]} | '
            f'{status}'
        )


# ==========================================
# BOCKA AV TASK
# ==========================================

def markera_klar(uppgifter):

    if len(uppgifter) == 0:

        print(
            "Det finns inga tasks att bocka av."
        )

        return

    try:

        task_id = int(
            input(
                "Vilket ID vill du bocka av? "
            )
        )

    except ValueError:

        print(
            "Fel! Du måste skriva ett ID-nummer."
        )

        return

    # Letar efter tasken
    for uppgift in uppgifter:

        if uppgift["id"] == task_id:

            # Kontrollerar om den redan är klar
            if uppgift["klar"]:

                print(
                    "Den tasken är redan klar."
                )

                return

            # Ändrar status
            uppgift["klar"] = True

            # SPARAR ÄNDRINGEN
            spara_till_fil(
                uppgifter
            )

            print(
                f'✓ {uppgift["uppgift"]} är nu klar!'
            )

            return

    print(
        "Fel! Det finns ingen task med det ID-numret."
    )


# ==========================================
# TA BORT TASK
# ==========================================

def ta_bort_uppgift(uppgifter):

    if len(uppgifter) == 0:

        print(
            "Det finns inga tasks att ta bort."
        )

        return

    sokning = input(
        "Ange ID eller namn på tasken du vill ta bort: "
    ).strip()

    if sokning == "":

        print(
            "Fel! Du måste ange ett ID eller namn."
        )

        return

    # Letar efter ID eller namn
    for uppgift in uppgifter:

        if (
            sokning == str(uppgift["id"])
            or
            sokning.lower() == uppgift["uppgift"].lower()
        ):

            # Tar bort tasken från listan
            uppgifter.remove(
                uppgift
            )

            # SPARAR DEN NYA LISTAN
            spara_till_fil(
                uppgifter
            )

            print(
                "Tasken har tagits bort och ändringen har sparats."
            )

            return

    print(
        "Fel! Tasken hittades inte."
    )


# ==========================================
# GRÄNSSNITT & MENYSYSTEM
# ==========================================

def visa_meny():

    print(
        "\n--- TASK MASTER ---"
    )

    print(
        "1. Lägg till tasks"
    )

    print(
        "2. Visa mina tasks"
    )

    print(
        "3. Bocka av task"
    )

    print(
        "4. Ta bort task"
    )

    print(
        "5. Avsluta"
    )


# ==========================================
# STARTA PROGRAMMET
# ==========================================

def starta_program():

    # LÄSER IN SPARADE TASKS NÄR PROGRAMMET STARTAR
    uppgifter = las_fran_fil()

    print(
        "\nHej! Välkommen till Task Master."
    )

    # Visar hur många sparade tasks som finns
    if len(uppgifter) > 0:

        print(
            f"Du har {len(uppgifter)} sparade tasks."
        )

    # Programmet fortsätter tills användaren
    # väljer att avsluta
    while True:

        visa_meny()

        val = input(
            "Välj 1-5: "
        ).strip()


        # ==================================
        # 1. LÄGG TILL TASKS
        # ==================================

        if val == "1":

            # Max 10 tasks totalt
            if len(uppgifter) >= 10:

                print(
                    "Du har redan 10 tasks."
                )

                continue

            while True:

                try:

                    antal = int(
                        input(
                            "Hur många tasks vill du lägga till? "
                        f"(1-{10 - len(uppgifter)}): "
                        )
                    )

                    # Räknar hur många platser som finns kvar
                    max_antal = 10 - len(uppgifter)

                    if 1 <= antal <= max_antal:
                        break

                    else:
                        print(
                            f"Fel! Du kan lägga till "
                            f"mellan 1 och {max_antal} tasks."
                        )

                except ValueError:

                    print(
                        "Fel! Du måste skriva ett nummer."
                    )

            lagg_till_flera_uppgifter(
                uppgifter,
                antal
            )


        # ==================================
        # 2. VISA TASKS
        # ==================================

        elif val == "2":

            visa_alla_uppgifter(
                uppgifter
            )


        # ==================================
        # 3. BOCKA AV TASK
        # ==================================

        elif val == "3":

            visa_alla_uppgifter(
                uppgifter
            )

            if len(uppgifter) > 0:

                markera_klar(
                    uppgifter
                )


        # ==================================
        # 4. TA BORT TASK
        # ==================================

        elif val == "4":

            visa_alla_uppgifter(
                uppgifter
            )

            if len(uppgifter) > 0:

                ta_bort_uppgift(
                    uppgifter
                )


        # ==================================
        # 5. AVSLUTA
        # ==================================

        elif val == "5":

            # Sparar en sista gång innan avslut
            spara_till_fil(
                uppgifter
            )

            print(
                "\nDina tasks har sparats."
            )

            print(
                "Task Master avslutas. Hej då!"
            )

            break


        # ==================================
        # FEL MENYVAL
        # ==================================

        else:

            print(
                "Fel! Välj 1, 2, 3, 4 eller 5."
            )


# ==========================================
# KÖR PROGRAMMET
# ==========================================

starta_program()
