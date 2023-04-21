import numpy as np

# fname='test_input.txt'
fname='input.txt'

this_score = 0


with open(fname) as fp:
    for line in fp:
        stripped = str.strip(line)
        if stripped == 'A X':
            this_score+=3+0
        elif stripped == 'A Y':
            this_score+=1+3
        elif stripped == 'A Z':
            this_score+=2+6
        elif stripped == 'B X':
            this_score+=1+0
        elif stripped == 'B Y':
            this_score+=2+3
        elif stripped == 'B Z':
            this_score+=3+6
        elif stripped == 'C X':
            this_score+=2+0
        elif stripped == 'C Y':
            this_score+=3+3
        elif stripped == 'C Z':
            this_score+=1+6
print(this_score)