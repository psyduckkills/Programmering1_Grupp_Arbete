# Task Master Pyton Program

## Redovisning
* Demo av Koden


### Förklara Kod Snutt 
---
[Mitt GitHub Repo](https://github.com/psyduckkills/Programmering1_Grupp_Arbete/tree/Khilkhil)
---
Två string-methods
---
```
    status = input("Vad för rank är uppgiften? Hög; Medel eller Låg Prioritet ? ").upper().strip()
```
#### strip() = tar bort 1 och sista mellanslag
#### upper = gör str till STORA bokstäver
Fil Hantering
---
```
  tom_lista_av_uppgifter = ""
    with open(fil_namn, "w", encoding="utf-8") as f:
        ta_bort_alla_uppgifter = f.write(tom_lista_av_uppgifter)
```
#### tom_lista_av_uppgifter är en "TOM" sträng
#### with open(fil_namn, "w") as f:  
#### *Hittar Filen, öppar i write mode
#### f.write(tom_lista_av_uppgifter)
#### Skriver över all text i filen med "TOM"-sträng

Fel-Hantering 
---
```
    try:
        if hittad:
            with open(fil_namn, 'w', encoding="utf-8") as rad:
                rad.writelines(rader)
            print("Uppgiften har ändrats. ")
        else:
            print("Det finns ingen uppgift med det ID:t.")
    except FileNotFoundError:
         print("Filen finns inte.")

```
#### try blocket används för fel-hantering
#### except tillkommer när koden inte funkat
#### Användning: Inte bli hackad
#### (Användaren vet ej p.språket)

For-Loop
---
```
    for i in range(len(rader)):
        if rader[i].strip() == "ID Nr: " + id_som_ska_andras:
            hittad = True

            ny_uppgift = input("Ny Uppgift: ")
            ny_beskriving = input("Ny beskrivning: ")
            ny_status = input("Ny status: ")

            rader[i + 1] = "Uppgift: " + ny_uppgift + "\n"
            rader[i + 2] = "Beskrivinig: " + ny_beskriving  + "\n"
            rader[i + 3] = "Status: " + ny_status + "\n"
            break
```
#### for i in range(len(rader)): Kollar Filen rad för rad
#### i I detta sammanhang är där ID Nr är hittad
#### Man lägger in ny information genom att lägga in i [i + 1-3] 
#### Detta pågrund av ordningen som man gett informationen i txt.filen. 