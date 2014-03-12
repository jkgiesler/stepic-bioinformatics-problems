"""
Chapter 2 Finally!

(requires RNAtoProtein and revcomp) This function takes a DNA sequence and a
protein sequence and returns all of the possible DNA sequence which
appear in the given sequence that code the protein sequence supplied.

In other words it searches for the protein sequence given using only
the codons which are availible in rnaseq. 

It also will return every instance in all reading frames.
"""

###################################################################################
######Find All possible sequences in string which could equal a given prot string##
###################################################################################

def RNAtoProtein(rna):
    """This function takes rna, searches for the first AUG in any RF 
    and prints out all of the amino acids before a stop codon is reached"""
    
    protein=""
    handytable=open("rnatable.txt","rt")
    translatdict={}
    lst=[]
    for line in handytable:
        temp=line.rstrip()
        lst=temp.split(" ")
        translatdict[lst[0]]=lst[1] 
    start=[]
    var=0
    while(var<len(rna)):
        protein = protein + translatdict[rna[var:var+3]]
        var += 3
    return protein


def revcomp(seq):
    """this takes a given sequence and returns the reverse complement"""
    seq=seq.upper()
    intab="ACTG"
    outtab="TGAC"
    trantab=str.maketrans(intab,outtab)
    seq=seq[::-1]
    seq=seq.translate(trantab)
    return seq

def findprotseqinrna(rnaseq,proteinseq):
    k=len(proteinseq)*3
    
    possiblekmers=[rnaseq[i:i+k].replace("T","U") for i in range(len(rnaseq)-k+1)]
    stor=[]
    answers=[]
    totalcalc=len(possiblekmers)
    prog=0
    for dnaseq in possiblekmers:
        prot=""
        prot2=""
        
        var=0
        while var<len(dnaseq):
            prot+=RNAtoProtein(dnaseq[var:var+3])
            var+=3
            
        revdnaseq=revcomp(dnaseq.replace("U","T"))
        
        var=0
        while var<len(dnaseq):
            prot2+=RNAtoProtein(revdnaseq[var:var+3].replace("T","U"))
            var+=3
    
        if prot == proteinseq or prot2 == proteinseq:
            answers.append(dnaseq)
        prog += 1
        print(prog/totalcalc)
    answers=[i.replace("U","T") for i in answers]
    return answers

proteinseq='VKLFPWFNQY'

genome=open('B_brevis.txt','rt')
rnaseq=''
for line in genome:
    rnaseq+=line.rstrip()
genome.close()
print(len(findprotseqinrna(rnaseq,proteinseq)))
