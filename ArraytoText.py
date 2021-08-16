import numpy as np
a = [['i', 'am', 'an', 'american'], ['pronoun', 'verb', 'article', 'pronoun'], ['i am an american', 'i am an american', 'i am an american', 'i am an american']]

# Using above second method to create a
# 2D array
rows, cols = (4, 3)
current_col = -1
current_row = 0
count = 0
arr = [["wordA"], ["wordB"]]
array = [[], []]
wordA = ""
wordB = ""
array.clear()
for i in range(rows):
    current_row += 1
    for j in range(cols):
        if current_col == 0:
            wordA = wordList[count]
            current_col += 1
            count += 1
        else:
            wordB = wordList[count]
            current_col = 0
            count += 1
    words = [[wordA], [wordB]]

    array.append(words)
print(array[1])


# with open('./Datasets/tokenlist.txt', 'w') as outfile:
#    for slice_2d in a:
#        np.savetxt(outfile, x)
