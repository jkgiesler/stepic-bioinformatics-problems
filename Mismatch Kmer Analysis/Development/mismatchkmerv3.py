# -*- coding: utf-8 -*-
"""
Praise bird jesus this worked and got me the assignment...
however sometimes it doesnt work... why is that.

the underlying logic is that the absolute max will be d mutations from
one of the sequences which already appears in the string. Is this always
the case? Who knows.

Further testing is required.

"""

#def generateallkmer(k):
    #'''returns every possible kmer given a length k'''
    #seq = itertools.product("ATGC",repeat=k)

    #lst=[]
    
    #for i in seq:
        #lst.append(("".join(i)))
        
    #return lst
def scoring(testseq,kmer,d):
    '''this function is used as a logical test to see whether
    or not the test seq is within an acceptable distance of
    kmer'''
    count=0
    acceptable=len(testseq)-d
    for i in range(len(testseq)):
        if kmer[i]==testseq[i]:
            count+=1
    if count >= acceptable:
        return True
    else:
        return False
        
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

def counter(string,search,d):
    '''this function is an implementation of a overlapping counter which
        ignore the ability of python methods..makes it easer to write in a different
        language'''
    count = 0
    for x in range(len(string)-len(search)+1):
        if scoring(string[x:x+len(search)],search,d):#calls score for mismatch
            count+=1
    return count
   
def mutatebase(bp):
    mutant=[]
    for x in range(len(bp)):
        for i in range(3):
            if bp[x]=="A":
                z=["C","G","T"]
                mutantstr=(z[i])
            if bp[x]=="C":
                z=["G","T","A"]
                mutantstr=(z[i])
            if bp[x]=="G":
                z=["C","A","T"]
                mutantstr=(z[i])
            if bp[x]=="T":
                z=["G","C","A"]
                mutantstr=(z[i])
            start=bp[:x]
            stop=bp[x+1:]
            mutantstr=start+mutantstr+stop
            mutant.append(mutantstr)

    return mutant

def massmutate(base,d):
    z=mutatebase(base)    
    for i in range(d-1): 
        z=[mutatebase(i) for i in z]
        z= list(itertools.chain.from_iterable(z))
    return z

def printmax(seq,k,d):	
	#init time
	start=time.time()
	#init dict and grab all kmers in seq
	kmers=getkmers(seq,k)
	dictr={}
	#mutate all kmers
	for i in kmers:
		mutants=massmutate(i,d)
		for mut in mutants:
			dictr[mut]=0

	counterlst=[]
	allkmer=list(dictr.keys())

	tot =len(allkmer)
	cnt=0
	#count occurance of all kmers
	for i in allkmer:
		counterlst.append(counter(seq,i,d))                
		cnt += 1
		print(counter(seq,i,d))

	#whats the max?
	maximum=max(counterlst)

	#generate answer
	maxlst=[]
	for i in range (len(counterlst)):
		if counterlst[i]==maximum:
			maxlst.append(allkmer[i])
	print(time.time()-start)
	return maxlst




####stuff for accuracy testing######
import itertools
import time
k=4
d=1

print(printmax("ACGTTGCATGTCGCATGATGCATGAGAGCT",k,d))


##print(printmax(seq,k,d))
#filein=open("testcases.txt","rt")
#answers=[]
#sequences=[]
#for line in filein:
	#line=line.rstrip()
	#sequences.append(line)
	#answers.append(printmax(line,k,d))
	
#filein.close()

#fileout=open("newgensol.txt","wt")

#for i in answers:
	#print(i,file=fileout)

#fileout.close()
