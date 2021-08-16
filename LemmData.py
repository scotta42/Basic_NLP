# Using readlines()
file1 = open('./Datasets/Lemmatization.txt', 'r')
lines = file1.readlines()
wordList = []
for line in lines:
    wordList += line.split( )

# Using above second method to create a
# 2D array
rows, cols = (41758, 2)
current_col = -1
current_row = 0
count = 0
arr = [["wordA"], ["wordB"]]
array = [[], []]
arrayA = []
arrayB = []
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
    arrayA.append(wordA)
    arrayB.append(wordB)
    array.append(words)


def check_matching(word_in):
    i = 0
    for word in arrayA:
        if word == word_in:
            return arrayB[i]
        i += 1
    i = 0
    for word in arrayB:
        if word == word_in:
            return arrayA[i]
        i += 1
    return word_in


def lemmatizer(word_list):
    wordslist = []
    for word in word_list:
        new_word = check_matching(word)
        if word != new_word:
            wordslist.append(new_word)
    return wordslist
# for i in range(rows):
#    col = []
#    for j in range(cols):
#        col.append(wordList[count])
#        count += 1

