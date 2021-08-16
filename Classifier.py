import pandas as pd
import numpy as np
from os.path import exists
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import Frame
import re

text = "i am an english speaker and i live in america"


def getdata(word):
    text_file = open("train_data.csv", 'r')
    lines = text_file.readlines()
    dataset = [[], [], []]
    dataset.clear()
    for line in lines:
        data = str(line).split(',')
        dataset.append(data)
    if (str(dataset[5]).__contains__(word)):
        string = ""
        i = 0
        for col in dataset[5]:
            if i == 1:
                string = col
                break
            i += 1
        string = string.replace('[', '')
        string = string.replace(']', '')
        string = string.replace('\'', '')
        string = string.replace('\"', '')
        result = word + string
        return result
    return word
