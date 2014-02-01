"""
Written by Jason Giesler 
Stepic.org/Bioinformatics Chapter 1:
Clumped Kmer Finder
Started on 1/26/14
Will implement in C++ for practice
"""
seq= ""
K=11
L=566
t=18

def getkmers(seq,k):
    '''takes a given sequence and returns all possible kmers
        does something kind of ugly with the creation of a dictionary to get rid
        of duplicates'''
    possiblekmers=[seq[i:i+k] for i in range(len(seq)-k+1)]
    dictr={}
    for kmer in possiblekmers:
        dictr[kmer]=0 #nukes all extras
    possiblekmers=list(dictr.keys())
    return possiblekmers

def counter(string,search):
    '''this function is an implementation of a overlapping counter which
        ignore the ability of python methods..makes it easer to write in a different
        language'''
    count = 0
    for x in range(len(string)-len(search)+1):
        if string[x:x+len(search)]==search:
            count+=1
    return count


#this works but it takes for FUCKING EVER 298 seconds 
import time

dictr={}

count=0
for x in range (len(seq)-L+1):
    lseq=seq[x:x+L]#gets the first L sized string
    possible=getkmers(lseq,K)
    counts=[]
    for kmer in possible:
       test=counter(lseq,kmer)
       if (test>=t):
          dictr[kmer]=1 
    count+=1
    print((count/(len(seq)-L+1))*100)

print(list(dictr.keys()))
print(time.time()-start)
    