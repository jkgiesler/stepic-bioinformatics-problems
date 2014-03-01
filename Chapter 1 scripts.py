"""
Written by Jason Giesler 
Stepic.org/Bioinformatics Chapter 1:
Small Scripts from Chapter 1
Started on 1/26/14
Will implement in C++ for practice
"""
#########################
###Reverse Complement####
#########################

def revcomp(seq):
    """this takes a given sequence and returns the reverse complement"""
    seq=seq.upper()
    seq=seq[::-1]
    intab="ACTG"
    outtab="TGAC"
    trantab=str.maketrans(intab,outtab)
    seq=seq.translate(trantab)
    return seq

#########################
########Statistics#######
#########################
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


def generateallkmer(k):
    '''returns every possible kmer given a length k'''
    kmers=[]
    answers=[]
    for i in range(0,2**(2*k)):
        binnum=bin(i)[2:]
        if (len(binnum)<2*k):
            binnum="0"*((2*k)-len(binnum))+binnum
        kmers.append(binnum)
    
    for string in kmers:
        totalstr=""
        for i in range(int(len(string)/2)):
            case=string[i]+string[i+k]
            if case=="00":
                totalstr+="A"
            if case=="01":
                totalstr+="C"
            if case=="10":
                totalstr+="G"
            if case=="11":
                totalstr+="T"
        answers.append(totalstr)
    return answers

#########################
####kmer searching#######
#########################
def importgenome(filename):
    '''this function just lets me import the ecoli genome because I'm too lazy to
    try copying and pasting it into the text editor'''
    genome=open(filename,"rt")
    bases=""
    for line in genome:
        bases+=line.rstrip()
    return bases
    
def getkmers(seq,k):
    '''takes a given sequence and returns all possible kmers
        does something kind of ugly with the creation of a dictionary to get rid
        of duplicates'''
    possiblekmers={}
    for i in range(len(seq)-k+1):
        if seq[i:i+k] in possiblekmers.keys():
            possiblekmers[seq[i:i+k]]+=1
        else:
            possiblekmers[seq[i:i+k]]=0
    
    lst=[] #optimization here hopefully will work
    for i in possiblekmers.keys():
        if possiblekmers[i]>1:
            lst.append(i)
    return lst



###################
####Skew Problems##
###################

def skew(seq):
    '''calculates skew distance for every base in an attempt to find the oriC'''
    seqstr=[]
    running=0
    seqstr.append(running)
    for i in range(len(seq)):
        
        if seq[i]=="C":
            running-=1
        if seq[i]=="G":
            running+=1
        else:
            pass
        seqstr.append(running)
    return seqstr

def findmin(skewdat):
    '''finds the location of the lowest skew scores'''    
    mini=[]
    minimum=min(skewdat)
    for i in range(len(skewdat)):
        if int(skewdat[i])==minimum:
            mini.append(i)
    return mini
