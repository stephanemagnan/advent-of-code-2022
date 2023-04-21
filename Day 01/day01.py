import numpy as np

fname='test_input.txt'
# fname='input.txt'

this_count = 0
max_count = 0

this_elf = 1
max_elf = 0

excl_1 = 127
excl_2 = 127

with open(fname) as fp:
    for line in fp:
        stripped = str.strip(line)
        if stripped == '':
            if this_count>max_count:
                max_count=this_count
                max_elf=this_elf
            this_elf+=1
            this_elf+=1
            this_count=0
        else:
            this_count+=int(stripped)
print(max_elf, max_count)