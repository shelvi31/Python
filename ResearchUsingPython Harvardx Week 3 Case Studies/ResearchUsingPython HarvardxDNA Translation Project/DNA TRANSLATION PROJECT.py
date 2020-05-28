# DNA TRANSLATION
#reference from files : dna.txt , protein.txt

def translate(sequence):
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }

    protein = ""
    if len(sequence)%3 == 0 :
        for i in range(0,len(sequence),3):
            codon = sequence[i:i+3]      #extracting the codon sequence
            protein += table[codon]      #The next step is to look up the codon and store it.We can store the protein in a string and concatenate amino acids to it one at a time.
    return (protein)                #lookup the codon matching result and store the result

def read_sequence(inputfile):
    """Reads and return the input string with special characters removed"""
    with open(inputfile, "r") as f:
        sequence = f.read()
    sequence = sequence.replace("\n", "")
    sequence = sequence.replace("\r", "")
    return sequence

prt = read_sequence("protein.txt")
dna = read_sequence("dna.txt")

print(len(dna)%3)     #gives 2 , hence lets translate with sliced

print(translate(dna[20:938]))    #the cds translation we have from ncbi is from location 21 - 937 hence slicing
print(prt)
print(prt == (translate(dna[20:938])))  #we get backspace here because the translation when completed is shown by _

print(prt == (translate(dna[20:938])[:-1]))    #removing backspace and comparing

print (translate(dna[20:938])[:-1] == translate(dna[20:935]))

# TASK ACCOMPLISHED
# 1) Manually downloading DNA and Protein Sequence data from NCBI
# 2) Imported the data into Python
# 3) Created an algoritham to translate DNA Data
# 4)Check if translation matches downloaded Protein sequennce





