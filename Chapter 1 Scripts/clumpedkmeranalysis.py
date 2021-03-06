"""
Written by Jason Giesler 
Stepic.org/Bioinformatics Chapter 1:
Clumped Kmer Finder
Started on 1/26/14
Will implement in C++ for practice
"""
seq= ""
K=12
L=597
t=20

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

def counter(string,search):
    '''this function is an implementation of a overlapping counter which
        ignore the ability of python methods..makes it easer to write in a different
        language'''
    count = 0
    for x in range(len(string)-len(search)+1):
        if string[x:x+len(search)]==search:
            count+=1
    return count

def findclumps(seq,L,t,K):
    '''this function searches the sequence for kmers length K which appear t times within a region lenght of L.
    It works quickly but has one assumption that was made to lower the amount of possible kmers returned.
    It's made to look for only kmers which appear more than once'''
    
    dictr={}#used to remove duplicates
    count=0
    for x in range (len(seq)-L+1):
        lseq=seq[x:x+L]#gets the first L sized string
        possible=getkmers(lseq,K)
        for kmer in possible:
           test=counter(lseq,kmer)
           if (test>=t):
              dictr[kmer]=1 
        count+=1
        print(round((count/(len(seq)-L+1))*100))
    return list(dictr.keys())

z=findclumps(importgenome("E-coli.txt"),500,3,9)
print(len(z))