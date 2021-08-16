def textArray(stringinput):
    # Using above second method to create a
    # 2D array
    text = stringinput
    rows, cols = (41758, 2)
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
                wordA = text[count]
                current_col += 1
                count += 1
            else:
                wordB = wordList[count]
                current_col = 0
                count += 1
        words = [[wordA], [wordB]]

        array.append(words)
    print(array)

# for i in range(rows):
#    col = []
#    for j in range(cols):
#        col.append(wordList[count])
#        count += 1

