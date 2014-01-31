"""
Written by Jason Giesler 
Stepic.org/Bioinformatics Chapter 1:
Finding a Simple Kmer(Exact)
Started on 1/26/14
Will implement in C++ for practice
"""
seq= "GTGAAGGACCTCTTGGGGGTGAAGGACCTCTTGGGGTAGCGTCATGGTGAAGGATCCTGGCATCCTGGCATCCTGGCATAGCGTCATGTCCTGGCACCTCTTGGGGTCCTGGCATAGCGTCATGCCTCTTGGGGCGATACTGTCGTGAAGGACCTCTTGGGGTAGCGTCATGCCTCTTGGGGGTGAAGGATAGCGTCATGTAGCGTCATGCCTCTTGGGGGTGAAGGATAGCGTCATGGTGAAGGACCTCTTGGGGCGATACTGTCTCCTGGCATAGCGTCATGGTGAAGGATAGCGTCATGTCCTGGCAGTGAAGGACGATACTGTCTCCTGGCACGATACTGTCCCTCTTGGGGCCTCTTGGGGGTGAAGGATCCTGGCAGTGAAGGACCTCTTGGGGTAGCGTCATGGTGAAGGATCCTGGCACCTCTTGGGGCGATACTGTCTCCTGGCAGTGAAGGACCTCTTGGGGTCCTGGCATAGCGTCATGTCCTGGCAGTGAAGGATCCTGGCAGTGAAGGACCTCTTGGGGCGATACTGTCCCTCTTGGGGCGATACTGTCTCCTGGCAGTGAAGGACCTCTTGGGGGTGAAGGATCCTGGCATAGCGTCATGTAGCGTCATGCCTCTTGGGGTAGCGTCATGCGATACTGTCTAGCGTCATGTCCTGGCATCCTGGCATCCTGGCACGATACTGTCCCTCTTGGGGTCCTGGCAGTGAAGGATCCTGGCACGATACTGTCTCCTGGCAGTGAAGGACCTCTTGGGGTAGCGTCATGTCCTGGCACCTCTTGGGGTCCTGGCACGATACTGTCTCCTGGCATAGCGTCATGCCTCTTGGGGTCCTGGCATCCTGGCACGATACTGTCTCCTGGCAGTGAAGGACCTCTTGGGGCCTCTTGGGGTAGCGTCATGTAGCGTCATGGTGAAGGATCCTGGCAGTGAAGGATAGCGTCATG"
k=14 # kmer length

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

def printmax(seq,k):
    allkmer=getkmers(seq,k)
    counterlst=[]
    for i in allkmer:
        counterlst.append(counter(seq,i))
    maximum=max(counterlst) #get most common kmer
    #now look for all kmers which have the maximum name
    maxlst=[]
    for i in range (len(counterlst)):
        if counterlst[i]==maximum:
            maxlst.append(allkmer[i])
    return maxlst
        

    
    