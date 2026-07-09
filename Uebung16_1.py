import subprocess
from Bio.Seq import Seq

infile='unknown.fas'    #Fasta-Datei mit Sequenz
outfile='16_1.gff'      #gff-Datei, die von Prodega ausgegeben wird

subprocess.run(['prodigal','-i',infile,'-f','gff','-o',outfile])    #führe prodigal aus

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
        start=int(cols[3])
        stop=int(cols[4])
        dna_seq=Seq(sequence[start-1:stop]) #-1, da in die Positions-Zählweise in der Sequenz bei 1 beginnt, Python aber ab 0 zählt.
    elif strand=='-':   #Wenn wir auf dem RV-Strand sind, entsprcht die DNA-Sequenz dem Reverse-Complement
        start=int(cols[4])
        stop=int(cols[3])
        dna_seq=Seq(sequence[stop-1:start]).reverse_complement()
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


    l+=1    #l wird für die fortlaufende Nummer bei der Gen-Benennung hochgezählt

gff.close()   #dateien werden geschlossen
fasta.close()

#hier sieht man jetzt beispielhaft den Eintrag für das erste potentielle gen:
print(dic['gene1'])


