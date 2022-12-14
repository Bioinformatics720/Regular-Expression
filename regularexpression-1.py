import re
seq="AATGCAGCAGTGCAGTGCGGTCCTACGATGCAGTG"
seq2=re.search('GG(A|T)CC',seq)
if seq2:
    print('pattern found')
else:
    print('pattern not found')
