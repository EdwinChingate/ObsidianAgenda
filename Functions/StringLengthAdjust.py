import numpy as np
def StringLengthAdjust(string,max_word_length=50,join=' '):
    Lstring=len(string)
    Divide=int(np.ceil(Lstring/max_word_length))
    if Divide==1:
        return string
    DistributionVec=np.linspace(0,Lstring+1,Divide,dtype='int')
    startChar=0
    FragmentS=[]
    for loc in DistributionVec[1:]:
        endChar=loc
        FragmentString=string[startChar:endChar]
        FragmentS.append(FragmentString)
        startChar=endChar
    string=join.join(FragmentS)
    return string
