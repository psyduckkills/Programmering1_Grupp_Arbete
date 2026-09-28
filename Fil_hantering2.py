# Fil hantering 
# Version 2 
'''Information som kan vara bra att veta '''
#------------------------------------------------
'''
person = {"name": "Alice", "age": 30, "active": True}

# Accessing
person["name"]                      # "Alice" (KeyError if missing)
person.get("missing")               # None
person.get("missing", "default")    # "default"

# Modifying
person["age"] = 31                  # update
person["email"] = "a@b.com"        # add new key
del person["active"]                # remove
removed = person.pop("email")       # remove and return
person.update({"age": 32, "city": "London"})

# Iterating
for key in person: ...
for value in person.values(): ...
for key, value in person.items(): ...

# Merging (Python 3.9+)
merged = dict1 | dict2
dict1 |= dict2              # in-place merge

# defaultdict
from collections import defaultdict
word_count = defaultdict(int)    # missing keys default to 0
for word in text.split():
    word_count[word] += 1
'''
#------------------------------------------------------------------------
'''
# Reading text
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()           # entire file as string

with open("data.txt", "r") as f:
    for line in f:               # memory-efficient line iteration
        print(line.strip())

# Writing text
with open("output.txt", "w") as f:    # w: overwrite
    f.write("Line one\n")

with open("log.txt", "a") as f:       # a: append
    f.write("New entry\n")

# CSV
import csv
with open("data.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# JSON
import json
with open("data.json", "r") as f:
    data = json.load(f)

with open("output.json", "w") as f:
    json.dump(data, f, indent=2)

json.loads('{"key": "value"}')    # parse JSON string
json.dumps({"key": "value"})      # convert to JSON string

'''
#-----------------------------------------------------------

fil_namn = "uppgifter.txt"
fil_namn2 = "klara_uppgifter.txt"

# tar bort zip i dict(zip(....)) för att zip tar emot 1 keyword argument , 5 var givna 

# uppgift_variable = dict(uppgift_id= "N/a", uppgift = "N/a", beskrivning = "N/a", inte_klar = True, status = "N/a")

'''Funkar '''
def skapa_uppgift(): 
    print("-----Skapa en Uppgift --------")
    uppgift_id = input("Vad är nummret på uppgiften? Format Uppgift... I punkt lägg nummer: ")
    uppgift = input("Namnet på Uppgiften? ")
    beskrivning = input("Mer anteckningar för uppgiften? ")
    inte_klar = True
    status = input("Vad för rank är uppgiften? Hög Prioritet ; Medel Prioritet ; Liten Prioritet ? ")
    print("----------------------------------")

    if uppgift_id == "":
        print("Felaktig inmatning")
        go_back_id = input("Välj C för att forsätta , Välj M för att gå tillbaka till Meny").lower()
        if go_back_id == "c":
            return uppgift_id
        elif go_back_id == "m":
            return hantera_meny()
        else:
            return uppgift_id
    else:
        with open(fil_namn, 'a',encoding="utf-8") as f:
                uppgift_id_input = f.write(f"-------------------------\nTask Nr: {uppgift_id}\n")


        if uppgift == "":
                print("Felaktig inmatning")
                go_back_uppgift = input("Välj C för att forsätta , Välj M för att gå tillbaka till Meny").lower()
                if go_back_uppgift == "c":
                    return uppgift
                elif go_back_id == "m":
                    return hantera_meny()
                else:
                    return uppgift
        else:
            with open(fil_namn, 'a',encoding="utf-8") as f:
                task_input = f.write(f"Task: {uppgift}\n")


    if beskrivning == "":
        print("Felaktig inmatning")
        go_back_description = input("Välj C för att forsätta , Välj M för att gå tillbaka till Meny").lower()
        if go_back_beskrivning == "c":
            return beskrivning
        elif go_back_description == "m":
            return hantera_meny()
        else:
            return beskrivning
    else:
        with open(fil_namn, 'a',encoding="utf-8") as f:
            decription_input = f.write(f"Description: {beskrivning}\n")


    if status == "":
        print("Felaktig inmatning")
        go_back_status = input("Välj C för att forsätta , Välj M för att gå tillbaka till Meny").lower()
        if go_back_status == "c":
            return status
        elif go_back_status == "m":
            return hantera_meny()
        else:
            return status
    else:
        with open(fil_namn, 'a',encoding="utf-8") as f:
            status_input = f.write(f"Status: {status}\n \n -------------------------\n")

#__Above this line the code works ______________________________________________________

''' Arbeta mer på koden '''

def andra_av_uppgift():
    print("-----Ändra Uppgift-----------")
    val_av_andra_uppgift = input("Vilken uppgift vill du ändra ? ")
    with open(fil_namn, "r", encoding="utf-8") as andraUppgift:
        andraUppgift.readline(id_uppgift)
        print("-----Ändra Uppgift --------")
        uppgift_id = input("Vad är ID på uppgiften? Format Uppgift... I punkt lägg nummer: ")
        id_uppgift = uppgift_id
        id_uppgift = dict(uppgift = "N/a", beskrivning = "N/a", inte_klar = True, status = "N/a")
        uppgift = input("Namnet på Uppgiften? ")
        beskrivning = input("Mer anteckningar för uppgiften? ")
        inte_klar = True
        status = input("Vad för rank är uppgiften? 1-10 ? ")
        print("----------------------------------")

    if uppgift_id == "":
        print("Felaktig inmatning")
        go_back_id = input("Välj C för att forsätta , Välj M för att gå tillbaka till Meny").lower()
        if go_back_id == "c":
            return uppgift_id
        elif go_back_id == "m":
            return hantera_meny()
        else:
            return uppgift_id
    else:
        with open(fil_namn, 'w',encoding="utf-8") as f:
            uppgift_id_input = f.write(f"-------------------------\nTask Nr: {uppgift_id}\n")

    if uppgift == "":
               print("Felaktig inmatning")
               go_back_uppgift = input("Välj C för att forsätta , Välj M för att gå tillbaka till Meny").lower()
               if go_back_uppgift == "c":
                return uppgift
               elif go_back_id == "m":
                return hantera_meny()
               else:
                   return uppgift
    else:
        with open(fil_namn, 'w',encoding="utf-8") as f:
            task_input = f.write(f"Task: {uppgift}\n")

    if beskrivning == "":
        print("Felaktig inmatning")
        go_back_description = input("Välj C för att forsätta , Välj M för att gå tillbaka till Meny").lower()
        if go_back_beskrivning == "c":
            return beskrivning
        elif go_back_description == "m":
            return hantera_meny()
        else:
            return beskrivning
    else:
        with open(fil_namn, 'w',encoding="utf-8") as f:
            decription_input = f.write(f"Beskrivning: {beskrivning}\n")

    if status == "":
        print("Felaktig inmatning")
        go_back_status = input("Välj C för att forsätta , Välj M för att gå tillbaka till Meny").lower()
        if go_back_status == "c":
            return status
        elif go_back_status == "m":
            return hantera_meny()
        else:
            return status
    else:
        
        with open(fil_namn, 'w',encoding="utf-8") as f:
            status_input = f.write(f"Status: {status}\n Uppgiften är ändrad \n -------------------------\n")


    if val_av_andra_uppgift != id_uppgift:
        with open(fil_namn, 'r', encoding="utf-8") as andraUppgift:
            andraUppgift.write(id_uppgift)
    vill_du_andra = input("Välj C för att forsätta , Välj M för att gå tillbaka till Meny").lower()
    if vill_du_andra == "c":
        return andra_av_uppgift
    elif vill_du_andra == "m":
            return hantera_meny()
    else:
            print("Felaktig inmatning")
            return andra_av_uppgift





def ta_bort_uppgift():
    namn_av_uppgiften = input("vad är namnet på uppgiften som du vill ta bort? ")
    with open (fil_namn, "a",encoding="utf-8") as ta_bort_id_uppgift:
        ta_bort_id_uppgift.readline()
        

    
'''Funkar'''
def se_hela_uppgift_listan():
    print("-----Se Alla Uppgifter-----")
    with open(fil_namn, "r", encoding="utf-8") as v_l:
        readlist = v_l.read()
        print(readlist)

    tillbaka_till_meny = input("Tryck M : Tillbaka till Meny \nTryck X: Gå ut från programmet\n: ").upper()
    if tillbaka_till_meny == "M":
            return hantera_meny()
    
    elif tillbaka_till_meny == "X":
            print("Trevlig Forsättninng")
            exit()
    else:
        print("Felaktig inmatning, försök igen")
        return se_hela_uppgift_listan
#____Above this line the code works___________



def uppgift_klar():
    r_uppgiften_klar = input("Är uppgiften klar? ").upper()
    if r_uppgiften_klar == "Yes":
        inte_klar = True
    else:
        inte_klar = False 

        if inte_klar == False:
            with open(fil_namn2, 'a',encoding="utf-8") as d_l:
                donelist = d_l.readlines()
                print(donelist)
        else:
            uppgift_forsatt = input("'Är uppgiften klar? Skriv Ja om det stämmer").upper()
            if uppgift_forsatt == "Ja":
                print("TillBaka till Menyn")
                #return hantera_meny()

            else:
                with open(fil_namn2, 'a',encoding="utf-8") as k_l:
                    klarlist = k_l.readlines()
                    print(klarlist)

    
def max_list_uppgifter():
    with open(fil_namn, "r", encoding="utf-8") as maxUppgifter:
        for lines in maxUppgifter:
            maxUppgifter.readline()
    if maxUppgifter > 10:
        print("För många uppgifter i listan ")
        ut_ur_max_lista = input("Tryck M: Tillbaka till Meny \nTryck X: Gå ut ur Programmet").upper()
        if ut_ur_max_lista == "M":
            print("Tillbaka till Meny")
            return hantera_meny()
    
        elif ut_ur_max_lista == "X":
            print("Trevlig fortsättning")
            exit()
        else:
            print("Felaktig input, försök igen")
            return ut_ur_max_lista

        return hantera_meny()
    
    else:
        print("Finns fortfarande plats i listan")
        return hantera_meny()




def min_list_uppgifter():
    with open(fil_namn, "r", encoding="utf-8") as maxUppgifter:
        for lines in maxUppgifter:
            maxUppgifter.readline()
    if maxUppgifter > 10:
        print("För många uppgifter i listan ")
        ut_ur_max_lista = input("Tryck M: Tillbaka till Meny \nTryck X: Gå ut ur Programmet").upper()
        if ut_ur_max_lista == "M":
            print("Tillbaka till Meny")
            return hantera_meny()
    
        elif ut_ur_max_lista == "X":
            print("Trevlig fortsättning")
            exit()
        else:
            print("Felaktig input, försök igen")
            return ut_ur_max_lista

        return hantera_meny()
    
    else:
        print("Finns fortfarande plats i listan")
        return hantera_meny()
    


