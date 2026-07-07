from Bio import Entrez, SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import time

mail='test@mail.com'

spezies=open('spezies_namen.txt', 'r')
accessions=[]
species=[]
for line in spezies:
    line=line.strip()
    accession=line[1:line.find(' ')]
    accessions.append(accession)
    if 'PREDICTED: ' in line:
        species.append(line[line.find('PREDICTED: ')+11:line.find('mitochondrial')-1])
    else:
        species.append(line[len(accession)+2:line.find('mitochondrial')-1])
spezies.close()
accessions=accessions[:len(accessions)-1]
species=species[:len(species)-1]

records=[]

Entrez.email=mail

for i in range(len(accessions)):
    
    suche = Entrez.efetch(
        db='nucleotide',
        id=accessions[i],
        idtype='acc',
        rettype='gb', retmode='text'
    )

    ergebnis=SeqIO.read(suche, 'genbank')
    header=species[i]+'_'+accessions[i]
    records.append(
        SeqRecord(Seq(ergebnis.seq), id=header.replace(' ','_'), description='[description='+ergebnis.description+']', name=ergebnis.name)
    )

    print(str(i)+' of '+str(len(accessions)))
    time.sleep(0.35)


print(records[0])
print(ergebnis)
outfile=open('meine_sequenzen.fasta','w')
SeqIO.write(records, outfile, 'fasta')
outfile.close()



# for i in 

# # suche=Entrez.esearch(
# #     db='nucleotide',
# #     id='NM_024864.4',
# #     idtype='acc'
# # )

# # ergebnis=SeqIO.read(suche)
# # print(ergebnis)