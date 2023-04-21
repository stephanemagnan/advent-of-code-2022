import numpy as np
import re

# fname='Day 08/test_input.txt'
fname='Day 08/input.txt'


forest = []
with open(fname) as fp:
    for line in fp:
        stripped = str.strip(line)
        forest.append(list([int(tree) for tree in stripped]))

forest_array=np.array(forest)
print(forest_array)

visible = np.zeros_like(forest_array)

#need to check all four sides. Perform analysis four times, rotating after each time.
for i in range(0,4):
    for row_ind, this_row in enumerate(forest_array):
        this_row_max=-1
        for col_ind, this_tree in enumerate(this_row):
            if this_tree>this_row_max:
                this_row_max=this_tree
                visible[row_ind,col_ind]=1
                if this_tree==9:
                    break
    print(visible)
    forest_array=np.rot90(forest_array)
    visible=np.rot90(visible)

forest_array=np.rot90(forest_array)
visible=np.rot90(visible)
print(forest_array)
print(visible)

print(np.sum(visible[:]))