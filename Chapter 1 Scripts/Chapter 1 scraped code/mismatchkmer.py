"""
Written by Jason Giesler 
Stepic.org/Bioinformatics Chapter 1:
Kmer Mismatch
Started on 1/26/14
Will implement in C++ for practice
"""
#given a sequence
seq="AACAAGCTGATAAACATTTAAAGAG"
#given a kmer
kmer="AAAAA"
#given a d
d=2
k=5



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
        
def mismatchlocator(seq,kmer,d,k):
    answers=[]
    for x in range(len(seq)-k+1):
        testseq=seq[x:x+k]
        if scoring(testseq,kmer,d):
            answers.append(x)
    return (len(answers))

answers=mismatchlocator(seq,kmer,d,k)
