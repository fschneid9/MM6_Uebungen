def summieren(bis):
    if type(bis)==int:  #Überprüfen, dass die Eingabe tatsächlich ein integer ist
        summe=0 #Hier drauf wird aufgerechnet
        for i in range(1,bis+1):    #1 bis zur festgelegten 'bis'-zahl. +1 aufgrund der Zählweise von Python, da die 'bis'-Zahl sonst ausgelassen würde
            summe+=i    #wird immer zur Summe hinzugefügt
        return(summe)
    else:
        print("Bitte geben Sie eine Ganze Zahl (Int) ein.")
def halbsumme(bis):
    return(summieren(bis)/2)
print(summieren(4))
print(halbsumme(4))

def absolute(number):
    if number<0:
        number=number*(-1)
    return(number)
print(absolute(-4))

def anytrue(it):
    #Überprüfen, dass die Eingabe tatsächlich ein iterierbares Objekt ist
    try:
        iter(it)
    except:
        print("The argument must be iterable!")
        return
    #for-loop geht durch alle Elemente des iterierbaren objekts und prüft einzelnen, ob sie True sind
    for element in it:
        if element==True:
            #Wenn ja, wird die Funktion mit dem Output 'True' beendet
            return(True)
    #Falls nicht, endet sie mit dem Output 'False'
    return(False)
print(anytrue([False,True,False,False]))

def binary(integer):
    if type(integer)!=int:
        print("The argument must be Integer.")
        return()
    b=str()
    while integer!=0:
        if integer%2!=0:
            integer=(integer-1)/2
            b='1'+b
        else:
            integer=integer/2
            b='0'+b
    return(b)
print(binary(47))

#Als Dictionary
def enum(list):
    enum={}
    for i in range(len(list)):
        enum.update({i:list[i]})
    return(enum)
print(enum(['apfel','birne','banane']))
#Als Liste mit Tuples
def enum(list):
    enum=[]
    for i in range(len(list)):
        enum.append((i, list[i]))
    return(enum)
print(enum(['apfel','birne','banane']))