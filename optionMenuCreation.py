import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import Frame
from TXTtoArray import textArray as ta
from SplitString import splitSentences
from SplitString import splitString
import numpy as np

# from program import update_selected as update_selected

global selected
global clicked
global clicked1
global clicked2
global clicked3
global clicked4
global clicked5
global clicked6
global clicked7
global clicked8
global clicked9
global clicked10
global clicked11
global clicked12
global clicked13
global clicked14
global clicked15
global clicked16
global clicked17
global clicked18
global clicked19
global clicked20
global clicked21
global clicked22
global clicked23
global clicked24


def clear_selection():
    global selected
    global clicked
    global clicked1
    global clicked2
    global clicked3
    global clicked4
    global clicked5
    global clicked6
    global clicked7
    global clicked8
    global clicked9
    global clicked10
    global clicked11
    global clicked12
    global clicked13
    global clicked14
    global clicked15
    global clicked16
    global clicked17
    global clicked18
    global clicked19
    global clicked20
    global clicked21
    global clicked22
    global clicked23
    global clicked24
    clicked = " "
    clicked1 = " "
    clicked2 = " "
    clicked3 = " "
    clicked4 = " "
    clicked5 = " "
    clicked6 = " "
    clicked7 = " "
    clicked8 = " "
    clicked9 = " "
    clicked10 = " "
    clicked11 = " "
    clicked12 = " "
    clicked13 = " "
    clicked14 = " "
    clicked15 = " "
    clicked16 = " "
    clicked17 = " "
    clicked18 = " "
    clicked19 = " "
    clicked20 = " "
    clicked21 = " "
    clicked22 = " "
    clicked23 = " "


def getall():
    global clicked
    global clicked1
    global clicked2
    global clicked3
    global clicked4
    global clicked5
    global clicked6
    global clicked7
    global clicked8
    global clicked9
    global clicked10
    global clicked11
    global clicked12
    global clicked13
    global clicked14
    global clicked15
    global clicked16
    global clicked17
    global clicked18
    global clicked19
    global clicked20
    global clicked21
    global clicked22
    global clicked23
    selections = [clicked, clicked1, clicked2, clicked3, clicked4, clicked5, clicked6, clicked7, clicked8, clicked9,
                  clicked10, clicked11, clicked12, clicked13, clicked14, clicked15, clicked16, clicked17, clicked18,
                  clicked19, clicked20, clicked21, clicked22, clicked23]
    return selections


def update_selected(string):
    global clicked
    clicked = string
    print(string)


def update_selected1(string):
    global clicked1
    clicked1 = string
    print(string)


def update_selected2(string):
    global clicked2
    clicked2 = string
    print(string)


def update_selected3(string):
    global clicked3
    clicked3 = string
    print(string)


def update_selected4(string):
    global clicked4
    clicked4 = string
    print(string)


def update_selected5(string):
    global clicked5
    clicked5 = string
    print(string)


def update_selected6(string):
    global clicked6
    clicked6 = string
    print(string)


def update_selected7(string):
    global clicked7
    clicked7 = string
    print(string)


def update_selected8(string):
    global clicked8
    clicked8 = string
    print(string)


def update_selected9(string):
    global clicked9
    clicked9 = string
    print(string)


def update_selected10(string):
    global clicked10
    clicked10 = string
    print(string)


def update_selected11(string):
    global clicked11
    clicked11 = string
    print(string)


def update_selected12(string):
    global clicked12
    clicked12 = string
    print(string)


def update_selected13(string):
    global clicked13
    clicked13 = string
    print(string)


def update_selected14(string):
    global clicked14
    clicked14 = string
    print(string)


def update_selected15(string):
    global clicked15
    clicked15 = string
    print(string)


def update_selected16(string):
    global clicked16
    clicked16 = string
    print(string)


def update_selected17(string):
    global clicked17
    clicked17 = string
    print(string)


def update_selected18(string):
    global clicked18
    clicked18 = string
    print(string)


def update_selected19(string):
    global clicked19
    clicked19 = string
    print(string)


def update_selected20(string):
    global clicked20
    clicked20 = string
    print(string)


def update_selected21(string):
    global clicked21
    clicked21 = string
    print(string)


def update_selected22(string):
    global clicked22
    clicked22 = string
    print(string)


def update_selected23(string):
    global clicked23
    clicked23 = string
    print(string)


class OptionMenuCreation:
    selected = []

    def create_buttons(word_list, train_frame1, train_frame2, train_frame3):
        global clicked
        global clicked1
        global clicked2
        global clicked3
        global clicked4
        global clicked5
        global clicked6
        global clicked7
        global clicked8
        global clicked9
        global clicked10
        global clicked11
        global clicked12
        global clicked13
        global clicked14
        global clicked15
        global clicked16
        global clicked17
        global clicked18
        global clicked19
        global clicked20
        global clicked21
        global clicked22
        global clicked23
        global clicked24
        # Create Dropdown menus
        # these are the hidden optionmenus
        # datatype of menu text
        clicked = StringVar()
        clicked.set(" ")
        clicked1 = StringVar()
        clicked1.set(" ")
        clicked2 = StringVar()
        clicked2.set(" ")
        clicked3 = StringVar()
        clicked3.set(" ")
        clicked4 = StringVar()
        clicked4.set(" ")
        clicked5 = StringVar()
        clicked5.set(" ")
        clicked6 = StringVar()
        clicked6.set(" ")
        clicked7 = StringVar()
        clicked7.set(" ")
        clicked8 = StringVar()
        clicked8.set(" ")
        clicked9 = StringVar()
        clicked9.set(" ")
        clicked10 = StringVar()
        clicked10.set(" ")
        clicked11 = StringVar()
        clicked11.set(" ")
        clicked12 = StringVar()
        clicked12.set(" ")
        clicked13 = StringVar()
        clicked13.set(" ")
        clicked14 = StringVar()
        clicked14.set(" ")
        clicked15 = StringVar()
        clicked15.set(" ")
        clicked16 = StringVar()
        clicked16.set(" ")
        clicked17 = StringVar()
        clicked17.set(" ")
        clicked18 = StringVar()
        clicked18.set(" ")
        clicked19 = StringVar()
        clicked19.set(" ")
        clicked20 = StringVar()
        clicked20.set(" ")
        clicked21 = StringVar()
        clicked21.set(" ")
        clicked22 = StringVar()
        clicked22.set(" ")
        clicked23 = StringVar()
        clicked23.set(" ")
        # Dropdown menu options
        options = [
            " ",
            "adjective",
            "adverb",
            "article",
            "conjunction",
            "preposition",
            "pronoun",
            "noun",
            "verb"
        ]
        max = len(word_list)
        count = 0
        while count < max:
            try:
                word_1 = Label(train_frame1, text=word_list[0])
                word_1.pack(side=LEFT)
                opMenu_1 = OptionMenu(train_frame1, clicked, *options, command=update_selected)
                opMenu_1.pack(side=LEFT)
            except():
                print("Error handling data")
            count += 1
            if count < max:
                try:
                    word_2 = Label(train_frame1, text=word_list[1])
                    word_2.pack(side=LEFT)
                    opMenu_2 = OptionMenu(train_frame1, clicked1, *options, command=update_selected1)
                    opMenu_2.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_3 = Label(train_frame1, text=word_list[2])
                    word_3.pack(side=LEFT)
                    opMenu_3 = OptionMenu(train_frame1, clicked2, *options, command=update_selected2)
                    opMenu_3.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_4 = Label(train_frame1, text=word_list[3])
                    word_4.pack(side=LEFT)
                    opMenu_4 = OptionMenu(train_frame1, clicked3, *options, command=update_selected3)
                    opMenu_4.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_5 = Label(train_frame1, text=word_list[4])
                    word_5.pack(side=LEFT)
                    opMenu_5 = OptionMenu(train_frame1, clicked4, *options, command=update_selected4)
                    opMenu_5.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_6 = Label(train_frame1, text=word_list[5])
                    word_6.pack(side=LEFT)
                    opMenu_6 = OptionMenu(train_frame1, clicked5, *options, command=update_selected5)
                    opMenu_6.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_7 = Label(train_frame1, text=word_list[6])
                    word_7.pack(side=LEFT)
                    opMenu_8 = OptionMenu(train_frame1, clicked6, *options, command=update_selected6)
                    opMenu_8.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_8 = Label(train_frame1, text=word_list[7])
                    word_8.pack(side=LEFT)
                    opMenu_8 = OptionMenu(train_frame1, clicked7, *options, command=update_selected7)
                    opMenu_8.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_9 = Label(train_frame2, text=word_list[8])
                    word_9.pack(side=LEFT)
                    opMenu_9 = OptionMenu(train_frame2, clicked8, *options, command=update_selected8)
                    opMenu_9.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_10 = Label(train_frame2, text=word_list[9])
                    word_10.pack(side=LEFT)
                    opMenu_10 = OptionMenu(train_frame2, clicked9, *options, command=update_selected9)
                    opMenu_10.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_11 = Label(train_frame2, text=word_list[10])
                    word_11.pack(side=LEFT)
                    opMenu_11 = OptionMenu(train_frame2, clicked10, *options, command=update_selected10)
                    opMenu_11.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_12 = Label(train_frame2, text=word_list[11])
                    word_12.pack(side=LEFT)
                    opMenu_12 = OptionMenu(train_frame2, clicked11, *options, command=update_selected11)
                    opMenu_12.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_13 = Label(train_frame2, text=word_list[12])
                    word_13.pack(side=LEFT)
                    opMenu_13 = OptionMenu(train_frame2, clicked12, *options, command=update_selected12)
                    opMenu_13.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_14 = Label(train_frame2, text=word_list[13])
                    word_14.pack(side=LEFT)
                    opMenu_14 = OptionMenu(train_frame2, clicked13, *options, command=update_selected13)
                    opMenu_14.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_15 = Label(train_frame2, text=word_list[14])
                    word_15.pack(side=LEFT)
                    opMenu_15 = OptionMenu(train_frame2, clicked14, *options, command=update_selected14)
                    opMenu_15.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_16 = Label(train_frame2, text=word_list[15])
                    word_16.pack(side=LEFT)
                    opMenu_16 = OptionMenu(train_frame2, clicked15, *options, command=update_selected15)
                    opMenu_16.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_17 = Label(train_frame2, text=word_list[16])
                    word_17.pack(side=LEFT)
                    opMenu_17 = OptionMenu(train_frame3, clicked16, *options, command=update_selected16)
                    opMenu_17.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_18 = Label(train_frame2, text=word_list[17])
                    word_18.pack(side=LEFT)
                    opMenu_18 = OptionMenu(train_frame3, clicked17, *options, command=update_selected17)
                    opMenu_18.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_19 = Label(train_frame3, text=word_list[18])
                    word_19.pack(side=LEFT)
                    opMenu_19 = OptionMenu(train_frame3, clicked18, *options, command=update_selected18)
                    opMenu_19.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_20 = Label(train_frame3, text=word_list[19])
                    word_20.pack(side=LEFT)
                    opMenu_20 = OptionMenu(train_frame3, clicked19, *options, command=update_selected19)
                    opMenu_20.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_21 = Label(train_frame3, text=word_list[20])
                    word_21.pack(side=LEFT)
                    opMenu_21 = OptionMenu(train_frame3, clicked20, *options)
                    opMenu_21.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_22 = Label(train_frame3, text=word_list[21])
                    word_22.pack(side=LEFT)
                    opMenu_22 = OptionMenu(train_frame3, clicked21, *options, command=update_selected20)
                    opMenu_22.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_23 = Label(train_frame3, text=word_list[22])
                    word_23.pack(side=LEFT)
                    opMenu_23 = OptionMenu(train_frame3, clicked22, *options, command=update_selected21)
                    opMenu_23.pack(side=LEFT)
                except():
                    print()
            count += 1
            if count < max:
                try:
                    word_24 = Label(train_frame3, text=item)
                    word_24.pack(side=LEFT)
                    opMenu_24 = OptionMenu(train_frame3, clicked23, *options, command=update_selected22)
                    opMenu_24.pack(side=LEFT)
                except():
                    print()

    # option menus
