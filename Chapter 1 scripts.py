"""
Written by Jason Giesler 
Stepic.org/Bioinformatics Chapter 1:
Reverse Complement and Finding start of substring
Started on 1/26/14
Will implement in C++ for practice
"""

genome=""
patter="CTTGATCAT"

def revcomp(seq):
    """this takes a given sequence and returns the reverse complement"""
    seq=seq.upper()
    seq=seq[::-1]
    intab="ACTG"
    outtab="TGAC"
    trantab=str.maketrans(intab,outtab)
    seq=seq.translate(trantab)
    return seq
    
def searcher(string,search):
    '''this function looks awefully similar to the counter function from kmer analysis but returns
    instead the location of every start of the search string'''
    strtlst=[]
    for x in range(len(string)-len(search)+1):
        if string[x:x+len(search)]==search:
            strtlst.append(x)
    return strtlst

def binarystat():
    '''this function retuns the solution of Pr(25,2,"01",1) from the 
    "Detour: Probabilities of patterns in string" section of stepic 
    note this is only good for a t of 1 as it does not look for overlaps'''
    
    binstr=[]
    for i in range(0,(2**25)):
        binnum=bin(i)[2:]#gets rid of the 0b
        if (len(binnum)<25):
            binnum="0"*(25-len(binnum))+binnum #makes sure every string is 25 long
        binstr.append(binnum)
    
    yes=0
    for x in binstr:
        temp=x.count("01")
        if temp>=1:
            yes+=1
    result= yes/len(binstr)
    return result


#z=searcher(genome,patter)
#z=[str(i) for i in z]
#print(" ".join(z))

