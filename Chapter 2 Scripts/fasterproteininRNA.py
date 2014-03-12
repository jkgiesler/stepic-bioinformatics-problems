"""
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

#iterates through all states two at a time

def passit(possibilities):
    '''
    ugly recursive function which takes two lists and generates all possible
    permutations. spagetti code at it's finest.
    '''
    ans=[]
    for i in range(len(possibilities)-1):
        for x in range(len(possibilities[i])):
            for j in range(len(possibilities[i+1])):
                ans.append(possibilities[i][x]+possibilities[i+1][j])
    return ans

def generatepossibleRNA(proteinseq):
    '''major function which generates all possible rna given a proteinseq'''    
    translatdict=importhandydict()
    possibilities=[]
    for i in proteinseq:
        possibilities.append(translatdict[i])
    possible=translatdict[proteinseq[0]]
    for i in range(len(proteinseq)-1):   
        possible=passit([possible,translatdict[proteinseq[i+1]]])
    final=[]
    for i in possible:
        final.append(i.replace("U","T"))
        final.append(revcomp(i.replace("U","T")))
    return final

def counter(string,search):
    '''this function is an implementation of a overlapping counter which
        ignore the ability of python methods..makes it easer to write in a different
        language. '''
    count = 0
    for x in range(len(string)-len(search)+1):
        if string[x:x+len(search)] == search:
            count+=1
    return count

def importhandydict():
    '''imports the handy translation table'''
    handytable=open("rnatable.txt","rt")
    translatdict={}
    lst=[]
    for line in handytable:
        temp=line.rstrip()
        lst=temp.split(" ")
        if lst[1] in translatdict.keys():
            translatdict[lst[1]].append(lst[0])
        else:
            translatdict[lst[1]] = [lst[0]]
    handytable.close()
    return translatdict

rnaseq=''
genome=open('B_brevis.txt','rt')
rnaseq=''
for line in genome:
    rnaseq+=line.rstrip()
genome.close()

proteinseq='VKLFPWFNQY'
possible=generatepossibleRNA(proteinseq)
total=[]

print("moving on to count")

wholething=len(possible)
tally=0
for i in possible:
    total.append(counter(rnaseq,i))

print(sum(total))




