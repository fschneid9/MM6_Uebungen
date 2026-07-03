path=input('Dateipfad der Eingabe')
outpath=input('Dateipfad der Ausgabe')

file=open(path, 'r')
story=''

for line in file:
    story=story+line

file.close()

l = len(story)-2
rev=''
while l >= 0:
    rev=rev+story[l]
    l-=1
print(rev)

file=open(outpath,'w')
file.write(rev)
file.close()