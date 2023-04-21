import numpy as np
import re

fname='input.txt'
# fname='input.txt'

this_contained = 0

with open(fname) as fp:
    for line in fp:
        stripped = str.strip(line)
        replaced=stripped.replace(',','-')
        zones=replaced.split('-')
        # print(zones)
        if ((int(zones[0])>=int(zones[2])) and (int(zones[0])<=int(zones[3]))) or ((int(zones[1])>=int(zones[2])) and (int(zones[1])<=int(zones[3]))) or ((int(zones[2])>=int(zones[0])) and (int(zones[2])<=int(zones[1]))) or ((int(zones[3])>=int(zones[0])) and (int(zones[3])<=int(zones[1]))):
            print(zones)
            this_contained+=1

print(this_contained)