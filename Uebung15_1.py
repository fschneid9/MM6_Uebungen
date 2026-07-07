from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# def read_fasta(input_path):
#     file=open(input_path, 'r')
#     genes=[]    
#     for line in file:
#         if '>' in line.strip():
#             gene=line.strip()
#             fasta_dict.update({gene:''})
#         else:
#             fasta_dict.update({gene:fasta_dict[gene]+line.strip()})
#     file.close()
#     return(fasta_dict)

def read_fasta(input_path):
    file=open(input_path, 'r')
    genes=[]  
    seq=''
    id=''
    description=''
    for line in file:
        line=line.strip()
        if '>' in line:     #Header?
            if seq!='':
                genes.append(SeqRecord(
                    Seq(seq),
                    id=id,
                    description=description,
                    name=name
                ))
                seq=''
            id=line[1:line.find(' ')]
            description=line[line.find('['):]
            name=line[line.find('protein=')+8:]
            name=name[:name.find(']')]
            print(name)
        else:
            seq=seq+line
    genes.append(SeqRecord(
        Seq(seq),
        id=id
    ))
    return(genes)

print(read_fasta('sequences.fas')[0])