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
    for i in allkmer:
        counterlst.append(counter(seq,i,d))
    maximum=max(counterlst) #get most common kmer
    #now look for all kmers which have the maximum name
    maxlst=[]
    for i in range (len(counterlst)):
        if counterlst[i]==maximum:
            maxlst.append(allkmer[i])
    return maxlst

print(printmax(seq,k,d))