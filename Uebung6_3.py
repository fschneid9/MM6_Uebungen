def summieren(bis):
    if type(bis)==int:
        summe=0
        for i in range(1,bis+1):
            summe+=i
        return(summe)
    else:
        print("Bitte geben Sie eine Ganze Zahl (Int) ein.")
print(summieren(4))

def runden(zahl, up):
    if (type(zahl)!=int and type(zahl)!=float) or type(up)!=bool:
        print("Bitte geben Sie eine Zahl (Int oder Float) und einen Bool (True/False) ein!")
        return()
    if up==True:
        return(int(zahl)+1)
    else:
        return(int(zahl))
print(runden(4.7,True))

def sort_list(liste):
    if type(liste)!=list:   #Überprüfen, ob das eingegebene Arbugemtn tatsächlich eine Liste ist
        print("Bitte geben Sie eine Liste ein.")
        return()    #Wenn nicht: Abbruch
    new_list=[]     #leere ziel-Liste erstellen
    new_list.append(liste[0])   #Und schon einmal das erste Element als Start-Wert zum vergleichen überführen
    for i in range(1,len(liste)):   #Ab dem zweiten Element werden jetzt alle Elemente der Eingabe-Liste durchgegangen
        success=False   #Success bleibt solange negativ, bis das entsprechende Element einsortiert wurde
        for j in range(0,len(new_list)):    #Jetzt wird die Zielliste nach und nach durchgegangen
            if liste[i]<new_list[j]:    #Das Element der Eingabe liste wird mit jedem Element, das schon in der Zielliste ist verglichen um zu schauen, ob es kleiner ist.
                new_list.insert(j,liste[i]) #Wenn es kleiner ist, wird es davor eingeschoben
                success=True
                break   #Mit diesem Element sind wir fertig, daher brechen wir die innere for-loop ab und gehen zum nächsten Element über.
        if success==False:
            new_list.append(liste[i])   #Falls kein Element in der Zielliste gefunden wurde, das größer ist, wird das Eingabe-Element am Ende an die Zielliste angehangen.
    return(new_list)    #Die sortierte Liste wird zurück gegeben
def differenzen(liste):
    if type(liste)!=list:   #Überprüfen, ob das eingegebene Arbugemtn tatsächlich eine Liste ist
        print("Bitte geben Sie eine Liste ein.")
        return()    #Wenn nicht: Abbruch
    liste=sort_list(liste)  #Die eingegebene Liste wird mit der vorhin erstellten Sortier-Funktion sortiert.
    differences=[]  #Eine leere Ziel-Liste wird erstellt.
    for i in range(0,len(liste)-1): #Es gibt am Ende genau eine direkte Differenz weniger, als zu vergleichende Elemente, daher -1
        differences.append(liste[i+1]-liste[i]) #Die differenz der größeren zahl [i+1] und der kleineren Zahl [i] wird zur ziel-Liste hinzugefügt
    return(differences)
#print(differenzen([4,3,7,6,1,5,2,8,10,13,11,12]))
print(differenzen(7))