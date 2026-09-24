uppgifter = []

def lagg_till_uppgift(uppgift, prioritet):
    if len(uppgifter) == 0:
        nytt_id = 1
    else:
        nytt_id = uppgifter[-1]["id"] + 1

    nytt_uppgift = {
        "id" : nytt_id,
        "uppgift" : uppgift,
        "prioritet" : prioritet
    }

    uppgifter.append(nytt_uppgift)
    return uppgifter

def prioriterad_uppgifter(hamta_uppgiftens_prioritet):
    prio = hamta_uppgiftens_prioritet["prioritet"].lower()
    if prio == "hög":
        return 1
    elif prio == "medium":
        return 2
    elif prio == "låg":
        return 3

def visa_alla_uppgifter():
    if len(uppgifter) == 0:
        print("Inga uppgifter hittades.")
        return
    else:
        sorterad = sorted(uppgifter, key=prioriterad_uppgifter)
        for i in sorterad:
            print(f"ID: {i["id"]} \n Uppgift: {i["uppgift"]} \n Prioritet: {i["prioritet"]}")
        
def ta_bort_uppgift(delete):
    hittad = False

    for i in uppgifter:
        if delete == str(i["id"]) or delete == i["uppgift"]:
            uppgifter.remove(i)
            hittad = True
            break

    if hittad == False:
        print("Felaktig id nummer eller uppgift namn")

    return uppgifter

print