# -*- coding: utf-8 -*-
"""
Chapter 2 Finally!
Created on Thu Mar  6 21:43:39 2014

@author: jgiesler
"""

##########################
###Translation Script#####
##########################
def RNAtoProtein(rna):
    """This function takes rna, searches for the first AUG in any RF 
    and prints out all of the amino acids before a stop codon is reached"""
    
    protein=""
    handytable=open("rnatable.txt","rt")
    translatdict={}
    lst=[]
    for line in handytable:
        temp=line.rstrip()
        lst=temp.split(" ")
        translatdict[lst[0]]=lst[1]
    print(translatdict.keys())
    
    start=[]
    for i in range(len(rna)-2):
        #print(rna[i:i+3])
        if rna[i:i+3] == "AUG":
            start.append(i)

    var=start[0]
    while(var<len(rna)):
        print(rna[var:var+3])
        protein = protein + translatdict[rna[var:var+3]]
        var += 3
        
    
    
    return protein

def identifysubstring(rnaseq,proteinseq):
    seq=[]
    prot=[]
    for line in handytable:
        temp=line.rstrip()
        lst=temp.split(" ")
        seq.append(lst[0])
        prot.append(lst[1])
    
    starts=[]
    
    for case in prot:
        if prot = proteinseq[0]:
            starts.append()
    
    
    return output
    
identifysubstring('ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA','MA')
    