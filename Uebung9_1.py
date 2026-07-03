path=input('Dateipfad')
file=open(path, 'r')
    
fasta_dict={}    
for line in file:
    if '>' in line.strip():
        gene=line.strip()
        fasta_dict.update({gene:''})
    else:
        fasta_dict.update({gene:fasta_dict[gene]+line.strip()})
file.close()

print(fasta_dict)

#Unendliche Geschichte
# success=True    #Solange der Nutzer die Geschichte lesen möchte

# while success==True:
#     geschichte = open('/vol/gbsb/fschneid/MM6/Uebungen_Git/MM6_Uebungen/unendliche_geschichte.txt', 'r')
#     for line in geschichte:
#         wq=str()
#         while wq!='w' and wq != 'q':
#             wq=input()
#         if wq=='w':
#             print(line.strip())
#         elif wq=='q':
#             success=False
#             break
#     geschichte.close()

path=input('Dateipfad')
path='/vol/gbsb/fschneid/MM6/Uebungen_Git/MM6_Uebungen/unendliche_geschichte.txt'
success=True
geschichte = open(path, 'r')
print('''
Es war einmal vor langer Zeit, in einem GBSB-Praktikum gar nicht weit von uns.
Da bildeten alle Studierenden einen Stuhlkreis um Stefan und dieser begann vorzulesen:

      ''')
while success==True:
    for line in geschichte:
        wq=str()
        while wq!='w' and wq != 'q':
            wq=input()
        if wq=='w':
            print(line.strip())
        else:
            success=False
            break
    geschichte.seek(0)
geschichte.close()