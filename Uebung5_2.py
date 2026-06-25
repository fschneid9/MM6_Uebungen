def einmaleins(zahl):
    print("Alles klar, lass uns das kleine Einmaleins der Zahl "+str(zahl)+" üben! Du kannst die Übung jederzeit durch die Eingabe von 'q' beenden.")
    try:
        zahl=int(zahl)
    except:
        print("Bitte nutzen Sie ganze zahlen!")
        return()
    for i in range(1,11):
        success = False
        while not success:
            inpt = input("Was ergibt "+str(i)+" mal "+str(zahl)+"?")
            if inpt == 'q':
                print("Die Übung wurde frühzeitig beendet.")
                return()
            elif int(inpt)==i*zahl:
                print("Das ist richtig! "+str(i)+" mal "+str(zahl)+" ergeibt "+str(i*zahl)+".")
                success=True
            else:
                print("Das war noch nicht ganz richtig. Probiere es noch einmal!")
    print("Du hast das toll gemacht und beherrschst jetzt das kleine Einmaleins der Zahl "+str(zahl)+"!")

einmaleins(2)
