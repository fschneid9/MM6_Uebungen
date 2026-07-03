### DNA-FASTA einlesen
path=input('Input Path')
AA_out = input('AA out path')
rvComp_out = input('rvComp out path')

def read_fasta(input_path):
    file=open(input_path, 'r')
    fasta_dict={}    
    for line in file:
        if '>' in line.strip():
            gene=line.strip()
            fasta_dict.update({gene:''})
        else:
            fasta_dict.update({gene:fasta_dict[gene]+line.strip()})
    file.close()
    return(fasta_dict)

### Transcription
def transcription(sequence):
    sequence=sequence.upper()   #Alle buchstaben groß machen
    return(sequence.replace('T','U'))   #thymin wird durch uracil ersetzt

### Translation
codontab = {
    'UCA': 'S',    # Serine
    'UCC': 'S',    # Serine
    'UCG': 'S',    # Serine
    'UCU': 'S',    # Serine
    'UUC': 'F',    # Phenylalanine
    'UUU': 'F',    # Phenylalanine
    'UUA': 'L',    # Leucine
    'UUG': 'L',    # Leucine
    'UAC': 'Y',    # Tyrosine
    'UAU': 'Y',    # Tyrosine
    'UAA': '*',    # Stop
    'UAG': '*',    # Stop
    'UGC': 'C',    # Cysteine
    'UGU': 'C',    # Cysteine
    'UGA': '*',    # Stop
    'UGG': 'W',    # Tryptophan
    'CUA': 'L',    # Leucine
    'CUC': 'L',    # Leucine
    'CUG': 'L',    # Leucine
    'CUU': 'L',    # Leucine
    'CCA': 'P',    # Proline
    'CCC': 'P',    # Proline
    'CCG': 'P',    # Proline
    'CCU': 'P',    # Proline
    'CAC': 'H',    # Histidine
    'CAU': 'H',    # Histidine
    'CAA': 'Q',    # Glutamine
    'CAG': 'Q',    # Glutamine
    'CGA': 'R',    # Arginine
    'CGC': 'R',    # Arginine
    'CGG': 'R',    # Arginine
    'CGU': 'R',    # Arginine
    'AUA': 'I',    # Isoleucine
    'AUC': 'I',    # Isoleucine
    'AUU': 'I',    # Isoleucine
    'AUG': 'M',    # Methionine
    'ACA': 'T',    # Threonine
    'ACC': 'T',    # Threonine
    'ACG': 'T',    # Threonine
    'ACU': 'T',    # Threonine
    'AAC': 'N',    # Asparagine
    'AAU': 'N',    # Asparagine
    'AAA': 'K',    # Lysine
    'AAG': 'K',    # Lysine
    'AGC': 'S',    # Serine
    'AGU': 'S',    # Serine
    'AGA': 'R',    # Arginine
    'AGG': 'R',    # Arginine
    'GUA': 'V',    # Valine
    'GUC': 'V',    # Valine
    'GUG': 'V',    # Valine
    'GUU': 'V',    # Valine
    'GCA': 'A',    # Alanine
    'GCC': 'A',    # Alanine
    'GCG': 'A',    # Alanine
    'GCU': 'A',    # Alanine
    'GAC': 'D',    # Aspartic acid
    'GAU': 'D',    # Aspartic acid
    'GAA': 'E',    # Glutamic acid
    'GAG': 'E',    # Glutamic acid
    'GGA': 'G',    # Glycine
    'GGC': 'G',    # Glycine
    'GGG': 'G',    # Glycine
    'GGU': 'G'     # Glycine
}

def translation(RNA):
    start=RNA.find('AUG') #Start-Codon finden
    CDS=RNA[start:]   #Zu-Translatierende RNA beginnt mit dem Start-Codon
    AA=str()    #Leerer String, in dem die AA-Sequenz aufgebaut wird
    while len(CDS)>=3:  #Solange noch mindestens ein ganzes Codon noch nicht translatiert wurde:
        codon=CDS[:3]   #Codon sind die ersten drei Basen
        if codontab[codon]=='*':    #Kontrolle: Ist es ein Stop-Codon?
            #print('STOP: '+codon)
            return(AA)  #Wenn ja: Bisherige AA-Sequenz zurückgeben
        else:
            AA=AA+codontab[codon]   #Die zum Codon-gehörende AA wird an die AA-Sequenz angehangen
            CDS=CDS[3:]     #Das aktuelle Codon wird aus der CDS entfernt, damit es mit dem nächsten Codon weitergeht
    return(AA)

def get_AA_Fasta(FASTA_IN_PATH):
    DNA_FASTA = read_fasta(FASTA_IN_PATH)   #FASTA-Dictionary laden

    AA_fasta = ''   #Leerer Ziel-String für die AA-Fasta
    for i in DNA_FASTA.keys():
        AA_fasta += i+'\n'  #Header
        AA_fasta += translation(transcription(DNA_FASTA[i]))+'\n'   #Transkript
    AA_fasta=AA_fasta[:len(AA_fasta)-1] #letztes '\n' wieder entfernen
    return(AA_fasta)

def get_rvComp_Fasta(FASTA_IN_PATH):
    DNA_FASTA = read_fasta(FASTA_IN_PATH)
    rvComp_fasta = ''
    for i in DNA_FASTA.keys():
        seq=DNA_FASTA[i]
        seq=seq.replace('A','t')   #komplementär-Nucleotide; zunächst in Klein-Buchstaben, um Case-Sensetive die Original-basen zu ändern
        seq=seq.replace('T','a')
        seq=seq.replace('G','c')
        seq=seq.replace('C','g')
        seq=seq.upper()    #Anschließend werden die Buchstaben wieder groß gemacht
        rvComp_fasta += i+'\n'  #Header
        rvComp_fasta += seq[::-1]+'\n'  #Reverse Complement
    rvComp_fasta=rvComp_fasta[:len(rvComp_fasta)-1] #letztes '\n' wieder entfernen
    return(rvComp_fasta)

def write_AA_fasta(FASTA_IN_PATH, FASTA_OUT_PATH):
    AA = get_AA_Fasta(FASTA_IN_PATH)
    file = open(FASTA_OUT_PATH, 'w')
    file.write(AA)
    file.close

def write_rvComp_fasta(FASTA_IN_PATH, FASTA_OUT_PATH):
    RV = get_rvComp_Fasta(FASTA_IN_PATH)
    file = open(FASTA_OUT_PATH, 'w')
    file.write(RV)
    file.close

print(read_fasta(path))
write_AA_fasta(path, AA_out)
write_rvComp_fasta(path, rvComp_out)