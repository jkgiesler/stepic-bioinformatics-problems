'''
Chapter 1: DIY Genetic
Jason Giesler
2/6/14
'''
from random import *
seq="ACGTTGCATGTCGCATGATGCATGAGAGCT"
d=1
k=4

def mutatebase(bp):
    x=choice(range(len(bp)))
    
    if bp[x]=="A":
        z=["C","G","T"]
        mutant=(choice(z))
    if bp[x]=="C":
        z=["G","T","A"]
        mutant=(choice(z))
    if bp[x]=="G":
        z=["C","A","T"]
        mutant=(choice(z))
    if bp[x]=="T":
        z=["G","C","A"]
        mutant=(choice(z))
    
    start=bp[:x]
    stop=bp[x+1:]
    mutant=start+mutant+stop
    return mutant

def distancetest(testseq,kmer,d):
    '''this function is used as a logical test to see whether
    or not the test seq is within an acceptable distance of
    kmer'''
    count=0
    acceptable=k-d
    for i in range(len(testseq)):
        if kmer[i]==testseq[i]:
            count+=1
    if count >= acceptable:
        return True
    else:
        return False

def counter(string,search,d):
    '''this function is an implementation of a overlapping counter which
        ignore the ability of python methods..makes it easer to write in a different
        language'''
    count = 0
    for x in range(len(string)-len(search)+1):
        if distancetest(string[x:x+len(search)],search,d):#calls score for mismatch
            count+=1
    return count

initseq=k*"A"
maxcount=0
maxcountstr=[]
stop=0
while stop<20:
    count=counter(seq,initseq,d)
    
    if count>maxcount:
        maxcountstr=[]
        maxcountstr.append(initseq)
        maxcount=count
    if count==maxcount:
        maxcountstr.append(initseq)
    z=0
    if count<maxcount:
        while z<=count:
            newseq=mutatebase(initseq)
            z=counter(seq,newseq,d)
        initseq=newseq
    initseq=mutatebase(initseq)
    stop+=1
    
print(maxcount)
print(maxcountstr)
    
    
    #return count
    
#starttherandom(seq,k,d)
    