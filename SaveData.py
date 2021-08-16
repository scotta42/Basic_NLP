import pandas as pd
import numpy as np
from os.path import exists
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import Frame


def save_training_data():
    array = np.arange(1,25).reshape(6,3)
    dataframe = pd.DataFrame(array)
    dataframe.to_csv(r"./Datasets/train_data.csv")


def save_data(data):
    file_exists = exists("./Datasets/train_data.csv")
    if file_exists == TRUE:
        text_file = open("./Datasets/train_data.csv", 'r')
        lines = text_file.readlines()
        if len(lines) < 1:
            array = np.array(data)
            np.savetxt("train_data.csv", array, delimiter=",", fmt="%s")
        else:
            save_add(data, lines)
    else:
        array = np.array(data)
        np.savetxt("train_data.csv", array, delimiter=",", fmt="%s")


def save_add(data, lines):
    # needs finishing
    array = np.array(data)
