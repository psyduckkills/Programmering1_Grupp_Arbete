# Lägga till och ta bort filer 
# Samt skapa en klar lista 
# Detta blir Modulen Fil_Hantering 
'''
• Använd avancerade datastrukturer (t.ex. en lista av dictionarys: [{'id': 1,
'uppgift': 'Handla', 'prioritet': 'Hög'}]).
• Använd filhantering (open, write, readlines).
• Använd funktioner för varje huvudfunktion (t.ex. visa_alla_uppgifter(),
spara_till_fil()).
• Använd en while-loop för att hålla programmet igång tills användaren väljer att avsluta.
• Implementera robust felhantering (t.ex. vad händer om filen saknas eller om användaren
anger felaktigt ID?).
'''

''' Icke klar , beta version '''



def task_master_variabler1():
    task_id:int = []
    task:str = []
    description: str = []
    status:str = []
    task_data = dict(zip(task_id, task,description,status))
    return task_data


def skapa_task_lista():
    task_master_variabler1()
    task_id = input("Vilket id ska detta task ha? ")
    try:
        with open("uppgifter.txt", 'w') as tl:
             task_in = tl.readlines(task_id)
             
    except InterruptedError:
        print('Try again')
        return task_master_variabler1()

    if task_id == "":
            print('Du lämna Task_ ID tom. Tryck x för att lämna programmet')
            task_id_exit_input = input('Vill du lämna programmet?tryck X för Exit , för Y för Meny ')
            if task_id_exit_input == 'x'.lower():
                print('Tack för idag!')
                exit()
            elif task_id_exit_input == 'y'.lower():
                return hantera_meny()

            else:
                return task_master_variabler1
    

    task = input("Vad är namnet på din task? ")
    if task == '':
        print('Du lämna Task tom. Tryck x för att lämna programmet')
        task_exit_input = input('Vill du lämna programmet?tryck X för Exit , för Y för Meny ')
        if task_exit_input == 'x'.lower():
            print('Tack för idag!')
            exit()
        elif task_exit_input == 'y'.lower():
            return hantera_meny()
        
        else:
            return skapa_task_lista
    
    try:
        with open("uppgifter.txt", 'r') as t:
            task = t.readline(t)
    except InterruptedError:
        print('try again')
        return task_master_variabler1()




    beskrivning = input("Något särskillt du behöver komma ihåg om din task? ")
    if beskrivning == '':
        print('Du lämna Beskrivning tom. Tryck x för att lämna programmet')
        beskrivning_exit_input = input('Vill du lämna programmet?tryck X för Exit , för Y för Meny ')
        if beskrivning_exit_input == 'x'.lower():
            print('Tack för idag!')
            exit()
        elif beskrivning_exit_input == 'y'.lower():
            return hantera_meny()
        
        else:
            return skapa_task_lista

    try:
        with open("uppifter.txt", 'r') as b:
            beskrivning_in = b.readline(beskrivning)
    except InterruptedError:
            print('try again')
            return task_master_variabler1()
    
    status = input("Vad är din status? ")
    if status == '':
            print('Du lämna status tom. Tryck x för att lämna programmet')
            status_exit_input = input('Vill du lämna programmet?tryck X för Exit , för Y för Meny ')
            if status_exit_input == 'x'.lower():
                print('Tack för idag!')
                exit()
            elif status_exit_input == 'y'.lower():
                return hantera_meny()
            
            else:
                return skapa_task_lista
    
    try:
        with open("uppgift.txt", 'r') as s:
                status_in = s.readline(status)
    except InterruptedError:
        print('try again')
        return task_master_variabler1()



    
task_master_variabler1()





def task_listan():
    #if is_complete == False:
     #   return done_listan

    ''' Kod som kan vara användbart '''

    pass


def done_listan():
    #if is_comple == True:
     #   return hantera_meny()
    ''' Kod som kan vara användbart '''
    pass


def lägga_till():

    pass


def ta_bort_tasklist():
    pass


def max_av_lista():
    pass

def min_av_lista():
    pass


