import numpy as np

# fname='test_input.txt'
fname='input.txt'

this_score = 0

with open(fname) as fp:
    for line in fp:
        stripped = str.strip(line)
        halflen=len(stripped)//2
        comp1=stripped[0:halflen]
        comp2=stripped[halflen:]
        
        for charnum in range(65,91):
            if chr(charnum) in comp1 and chr(charnum) in comp2:
                this_score+=charnum-38
                print(chr(charnum),charnum-38)
                break
        for charnum in range(97,123):
            if chr(charnum) in comp1 and chr(charnum) in comp2:
                this_score+=charnum-96
                print(chr(charnum),charnum-96)
                break
print(this_score)