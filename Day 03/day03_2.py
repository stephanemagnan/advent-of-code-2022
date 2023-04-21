import numpy as np

fname='test_input.txt'
# fname='input.txt'

this_score = 0
this_row=0
line1=''
line2=''
line3=''
with open(fname) as fp:
    for line in fp:
        stripped = str.strip(line)
        if this_row==0:
            line1=stripped
            this_row+=1
        elif this_row==1:
            line2=stripped
            this_row+=1
        elif this_row==2:
            line3=stripped
            this_row=0
            for charnum in range(65,91):
                if chr(charnum) in line1 and chr(charnum) in line2 and chr(charnum) in line3:
                    this_score+=charnum-38
                    print(chr(charnum),charnum-38)
                    break
            for charnum in range(97,123):
                if chr(charnum) in line1 and chr(charnum) in line2 and chr(charnum) in line3:
                    this_score+=charnum-96
                    print(chr(charnum),charnum-96)
                    break
            

print(this_score)