import subprocess
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import time
import json

infile='unknown.fas'    #Fasta-Datei mit Sequenz
outfile='16_1.gff'      #gff-Datei, die von Prodega ausgegeben wird
subprocess.run(['prodigal','-i',infile,'-f','gff','-o',outfile])

gff=open(outfile, 'r')    #generierte gff-Datei öffnen
fasta=open(infile, 'r')     #Fasta-Datei mit der gesamt-DNA-Sequenz wird geöffnet
sequence=fasta.readlines()[1]   #als Sequenz wird die zweite Zeile der Datei ausgewählt. Die erste enthält ja den Header.

dic={}  #leeres Ziel-Dictionary
l=0

for line in gff:
    if line.startswith('#'):    #Header-Zeilen ignorieren
        continue

    cols=line.strip().split('\t')   #Tabelle anhand der Tabulatoren in Spalten teilen
    if cols[0]!='unknown':  #wenn kein Genname bekannt ist, wird das Gen als geneX (X=fortlaufende Zahl) bezeichnet
        id=cols[0]
    else:
        id=f'gene{l}'
    
    #Jetzt werden die einzelnen Informationen aus den Spalten gezogen
    strand=cols[6]
    start=int(cols[3])
    stop=int(cols[4])
    seq_len=stop-start+1    #+1, das auch die start-position schon ein nucleotid hat
    score=float(cols[5])

    #Sequenzen
    if strand=='+':     #Wenn wir auf dem FW-Strand sind, entspricht die DNA-Sequenz dem Bereich zwischen Start und Stopp
        dna_seq=Seq(sequence[start-1:stop]) #-1, da in die Positions-Zählweise in der Sequenz bei 1 beginnt, Python aber ab 0 zählt.
    elif strand=='-':   #Wenn wir auf dem RV-Strand sind, entsprcht die DNA-Sequenz dem Reverse-Complement
        dna_seq=Seq(sequence[start-1:stop]).reverse_complement()
    aa_seq=dna_seq.translate()

    dic.update({id:{    #Im Ziel-Dictionary wird zu jedem Gen ein eigenes Dictionary mit den Informationen erstellt
        'start':start,
        'stop':stop,
        'length':seq_len,
        'strand':strand,
        'score':score,
        'dna_sequence':dna_seq,
        'protein_sequence':aa_seq
    }
    })

    print('Starte BLAST...')
    result_handle = NCBIWWW.qblast(
        "blastp",
        "swissprot",
        aa_seq
    )
    blast_record = NCBIXML.read(result_handle)

    if blast_record.alignments:
        hit = blast_record.alignments[0]
        print(hit.hit_id)
        print(hit.hit_def)
        beschreibung = hit.hit_def

        if "[" in beschreibung and "]" in beschreibung:
            organismus = beschreibung.split("[")[-1].rstrip("]")
        else:
            organismus = "unknown"
        print(organismus)

        dic[id].update(
            {'BLAST_id':hit.hit_id,
             'description':hit.hit_def,
             'organism':organismus}
        )
    
    else:
        dic[id].update(
            {'BLAST_id':None,
             'description':None,
             'organism':None}
        )

    print('BLAST beendet.')
    

    time.sleep(1)
    print('Finished: '+str(l))

    l+=1    #l wird für die fortlaufende Nummer bei der Gen-Benennung hochgezählt

gff.close()   #dateien werden geschlossen
fasta.close()

with open('dic16_1.json', 'w') as f:
    json.dump(dic, f)
    f.close()

print(dic['gene0'])

#hier sieht man jetzt beispielhaft den Eintrag für das erste potentielle gen:
#print(dic['gene1'])


