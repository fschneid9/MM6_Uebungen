from Bio import SeqIO

gb=SeqIO.parse('sequence.gb', 'genbank')
for seq_record in gb:
    print(seq_record)
