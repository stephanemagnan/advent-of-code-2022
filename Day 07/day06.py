import numpy as np
import re

# fname='Day 06/test_input.txt'
fname='Day 06/input.txt'



with open(fname) as fp:
    for line in fp:
        stripped = str.strip(line)
        words = len(stripped)-1

        for word_ind in range(4,words):
            this_word = stripped[word_ind-4:word_ind]
            if len(set(this_word))==4:
                print(this_word, word_ind)
                break


