# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:57:51 2014

@author: jgiesler
mismatchtest holy shit it works... really slow
God this needs to be cleaned up though
"""

#given a sequence
seq="CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC"
d=2
k=10
import itertools

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

def counter(string,search,d):
    '''this function is an implementation of a overlapping counter which
        ignore the ability of python methods..makes it easer to write in a different
        language'''
    count = 0
    for x in range(len(string)-len(search)+1):
        if scoring(string[x:x+len(search)],search,d):#calls score for mismatch
            count+=1
    return count
    


def printmax(seq,k,d):
    '''this function makes sure to print only the highest scoring kmers'''
    allkmer=generateallkmer(k)
    counterlst=[]
    
    percentdone=0
    tot=len(allkmer)
    cnt=0
    for i in allkmer:
        counterlst.append(counter(seq,i,d))
        cnt = cnt + 1
        print(cnt/tot)
    maximum=max(counterlst) #get most common kmer
    #now look for all kmers which have the maximum name
    maxlst=[]
    for i in range (len(counterlst)):
        if counterlst[i]==maximum:
            maxlst.append(allkmer[i])
    return maxlst

print(printmax(seq,k,d))