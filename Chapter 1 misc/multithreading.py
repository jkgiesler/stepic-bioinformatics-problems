# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:57:51 2014

@author: jgiesler
mismatchtest holy shit it works... really slow
God this needs to be cleaned up though
"""

#given a sequence
seq="ACGTTGCATGTCGCATGATGCATGAGAGCT"
d=1
k=4
import itertools
from multiprocessing import Pool

def generateallkmer(k):
    '''returns every possible kmer given a length k'''
    seq = itertools.product("ATGC",repeat=k)

    lst=[]
    
    for i in seq:
        lst.append(("".join(i)))
        
    return lst

def scoring(testseq,kmer,d):
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

def counter(search):
    '''this function is an implementation of a overlapping counter which
        ignore the ability of python methods..makes it easer to write in a different
        language'''
    count = 0
    string = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    d = 1
    for x in range(len(string)-len(search)+1):
        if scoring(string[x:x+len(search)],search,d):#calls score for mismatch
            count+=1
    return count



allkmer=generateallkmer(k)   
if __name__=="__main__":
    pool = Pool(processes=4)
    result = pool.map(counter, allkmer)

print(result)







#maximum=max(counterlst) #get most common kmer
##now look for all kmers which have the maximum name
#maxlst=[]
#for i in range (len(counterlst)):
#    if counterlst[i]==maximum:
#        maxlst.append(allkmer[i])
#maxlst

