import re


def splitSentences(string_in):
    print(string_in)
    str_in = [""]
    str_in = string_in
    sentences = ['', '']
    str_whole = ""
    i = 0
    j = 1
    print(len(str_in))
    str_in = list(map(lambda x: x.strip(),str_in))

    for line in str_in:
        str_a = ""
        str_b = ""
        if j <= len(str_in) - 1:
            str_a = str_in[i]
            str_b = str_in[j]
            str_whole = str_whole+str_a+str_b
            i = j+1
            j = j+2
        else:
            break
    print(i)
    print(j)
    print("showing result")
    print(str_whole)
    print("complete")
    sentences.clear()
    sentences = str_whole.split('.')
    count = 0
    return sentences


def splitString(self, string_in):
    x = string_in
    y = x.replace(',', ' ')
    y = y.replace('.', ' ')
    y = y.replace('!', ' ')
    words = y.split(' ')
    return words
