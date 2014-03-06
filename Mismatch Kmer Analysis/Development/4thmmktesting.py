# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 09:09:49 2014

@author: jgiesler
"""
import itertools

def generateallkmer(k,d):
    '''returns every possible kmer given a length k'''
    seq = itertools.product("ATGCN",repeat=k)
    lst=[]
    dictr={}
    for i in seq:
       test=("".join(i))
       if test.count("N")<=d:
           dictr[test]=0
    return dictr


def scoring(testseq,kmer,d):
    '''this function is used as a logical test to see whether
    or not the test seq is within an acceptable distance of
    kmer'''
    count=0
    acceptable=k-d
    for i in range(len(testseq)):
        if (kmer[i]==testseq[i]) or (testseq[i]=="N"):
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

d=1
k=4
z = generateallkmer(4,1)
seq = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
z = list(z)
count=[]
for i in z:
    count.append(counter(seq,i,d))
maximum=max(count)
winner=[]
for i in range(len(count)):
    if i == maximum:
        winner.append(z[i])