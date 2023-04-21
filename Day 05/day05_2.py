import numpy as np
import re

# fname='Day 05/test_input.txt'
fname='Day 05/input.txt'

this_contained = 0

multlist=[[],[],[],[],[],[],[],[],[]]

with open(fname) as fp:
    for line in fp:
        # stripped = str.strip(line)
        if '[' in line:
            stripped = "{:<35}".format(line)
            # print(stripped)
            if stripped[1]!=' ':
                multlist[0].append(stripped[1])    
            if stripped[5]!=' ':
                multlist[1].append(stripped[5])    
            if stripped[9]!=' ':
                multlist[2].append(stripped[9])    
            if stripped[13]!=' ':
                multlist[3].append(stripped[13])    
            if stripped[17]!=' ':
                multlist[4].append(stripped[17])    
            if stripped[21]!=' ':
                multlist[5].append(stripped[21])    
            if stripped[25]!=' ':
                multlist[6].append(stripped[25])    
            if stripped[29]!=' ':
                multlist[7].append(stripped[29])    
            if stripped[33]!=' ':
                multlist[8].append(stripped[33])    
            
            print(multlist)
        else:
            words=str.split(line,' ')
            if len(words)==6:
                print(line)
                repeats=int(words[1])
                fromind=int(words[3])-1
                toind=int(words[5])-1


                buffer = multlist[fromind][0:repeats]
                print(buffer)
                buffer.reverse()
                for i in range(0,repeats):
                    del multlist[fromind][0]
                # multlist[toind].insert(0,buffer[:][:])
                
                for i in range(0,repeats):
                    # buffer = multlist[fromind][0]
                    # del multlist[fromind][0]
                    multlist[toind].insert(0,buffer[i])

                print(multlist)
print(multlist)
print(multlist[0][0],multlist[1][0],multlist[2][0],multlist[3][0],multlist[4][0],multlist[5][0],multlist[6][0],multlist[7][0],multlist[8][0])
# print(multlist[0][0],multlist[1][0],multlist[2][0])