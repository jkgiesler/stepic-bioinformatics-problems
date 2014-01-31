seq= "CGGAAGCGAGATTCGCGTGGCGTGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGGCGTGATTCGAGCGGCGGATTCGAGATTCCGGGCGTGCGGGCGTGAAGCGCGTGGAGGAGGCGTGGCGTGCGGGAGGAGAAGCGAGAAGCCGGATTCAAGCAAGCATTCCGGCGGGAGATTCGCGTGGAGGCGTGGAGGCGTGGAGGCGTGCGGCGGGAGATTCAAGCCGGATTCGCGTGGAGAAGCGAGAAGCGCGTGCGGAAGCGAGGAGGAGAAGCATTCGCGTGATTCCGGGAGATTCAAGCATTCGCGTGCGGCGGGAGATTCAAGCGAGGAGGCGTGAAGCAAGCAAGCAAGCGCGTGGCGTGCGGCGGGAGAAGCAAGCGCGTGATTCGAGCGGGCGTGCGGAAGCGAGCGG"
k=12 # kmer length
tol=0 #acceptable errors


##calculate all possible kmers in the DNA set


def simplekmer(seq,k):
    count =0
    dict={}
    totallenseq=len(seq)
    
    while count<(totallenseq-k):
        for i in range(len(seq)-k):
            kmer=seq[i:i+k]
    		
            if kmer in dict:
                dict[kmer]+=1
            else:
                dict[kmer]= 1		
        seq=seq[1:]
        count+=1
    
    kmerlst=list(dict.keys())
    
    kmerlst.sort()
    return dict

def revcomp(seq):
    seq=seq[::-1]
    intab="ACTG"
    outtab="TGAC"
    trantab=str.maketrans(intab,outtab)
    seq=seq.translate(trantab)
    return seq


print(simplekmer(seq,k))







#score=0
#matches=0
#highmatches=0
#winner=""
#
#
#for sample in kmerlst: 
#    #compare each kmer against all of the others..
#    #if it is acceptably close to matching with another it will count as a match.
#    #the one with the most matches will the most common.
#    for j in range(len(kmerlst)):
#        
#        for i in range(len(sample)):
#            
#            if ( sample[i]==kmerlst[j][i] ):
#                score+=1
#    
#        if (score >= (k-tol) ):
#            matches+=1
#
#    if (matches>highmatches):
#        winner=sample
#        highmatches=matches
#            
#    score=0
#    matches=0

#print(winner)