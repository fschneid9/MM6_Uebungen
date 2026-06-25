a = int(input("Zahl1 eingeben\n"))
b = int(input("Zahl2 eingeben\n"))

liste1 = [a]
liste2 = []

while a > 1:
    a = int(a/2)
    liste1.append(a)
#Variable 'a' wird verändert
#Voraussetzung ist, dass 'a' größer als 1 ist
#'a' bekommt den int von 'a/2' zugeteilt. Dadurch wird 'a' bei jedem Durchlauf kleiner. Das neue 'a' wird jeweils an liste1 angehängt. Sobald 'a' kleiner/gleich 1 ist, wird die schleife beendet und 'a' wird nicht mehr kleiner.

print(liste1)

for i in range(0, len(liste1)):
    neu = b * pow(2, i)
    liste2.append(neu)
#liste2 wird verändert, indem eine neue zahl 'neu' angehangen wird
#neu entspricht Zahl 'b' mal 2**i, wobei die schleife über die anzahl an elementen in liste1 iteriert. Am Ende haben also liste1 und liste2 die gleiche length

print(liste2)

for i in range(0, len(liste1)):
    if (liste1[i] % 2) == 0:
        liste2[i] = 0
#die schleife iteriert über die elemente der liste1
#wenn die zahl gerade ist, wird das korrespondierende element in liste2 =0 gesetzt

print(liste2)

summe = 0

for zahl in liste2:
    summe += zahl
#alle elemente aus liste2 werden aufsummiert

print("Das Ergebnis ist: ", summe)
print(sum(liste2))


#Das Programm multipliziert Zahl1 mit Zahl2
