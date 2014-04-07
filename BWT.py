#Implementation of BW transform for searching for identical sequences

from collections import deque
from time import time
def seqimport(filename):
    seqfile=open(filename,'rt')
    seq=''
    for line in seqfile:
        line=line.rstrip()
        seq += line
    return seq
    seqfile.close()


def bwtransform(seq):
    seq= seq + '$'    
    #Burrows-Wheeler Transform
    n=len(seq)
    dq=deque(seq)
    outfile=open('tmpfile.txt','wt')
    for i in range(n):
        print(''.join(list(dq)),file=outfile)
        dq.rotate(1)
    outfile.close()
    return

def transform2():
    tmmpfile=open('tempfile.txt','rt')
    lst=[]
    for line in tmmpfile:
        line=line.rstrip()
        lst.append(line)
    tmmpfile.close()
    lst=[].sort()
    tmpfile2=open('tempfile2.txt','rt')
    for i in lst:
        print(i,file=tmpfile2)
    tmpfile2.close()


def printtofile(filename,seq):
    outfile=open(filename,'rt')
    print(seq,file=outfile)
    outfile.close()

start=time()
seq=seqimport('Vibrio_cholerae.txt')
bwt=bwtransform(seq)
printtofile('outfile1.txt',seq)
print(time()-start)
