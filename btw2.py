# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 17:02:50 2014

@author: jgiesler
"""
import BWTimport as bwt
import urllib.request
import itertools
from time import time

def generateallkmer(k):
    '''returns every possible kmer given a length k'''
    seq = itertools.product("ATGC",repeat=k)

    lst=[]
    
    for i in seq:
        lst.append(("".join(i)))
        
    return lst


allkmer=generateallkmer(9)
seq= 'TAGGACGGTAGGTCCTCCACGGACGGCGCTTAGGACGGTCCCCATAGGCCATCCCGCTCGCTCGCTCGCTCCACGCTCCACGCTTCCTAGGCGCTTCCCGCTCCATCCCCATCCTAGGCCATAGGACGGACGGACGGACGGACGGTAGGTCCCGCTCGCTCCAACGGCGCTTAGGCCATAGGCGCTCGCTTAGGTAGGCCACGCTCGCTCCATCCTAGGTAGGACGGCGCTTAGGTCCTCCTCCTCCCGCTTCCACGGTAGGACGGCGCTTAGGCCACGCTTAGGACGGCGCTCCAACGGCCAACGGCCACCATCCCGCTCCATCCTAGGTAGGACGGCCACGCTTCCCCA'

print('searching')
# pre-compute data structures
bwt_data = bwt.make_all(seq)
print('size: ',len(allkmer))
for i in allkmer:
    bwt.find(i, seq, mismatches=3, bwt_data=bwt_data)