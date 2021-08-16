import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import Frame
import LemmData as ld
import SaveData as sd
from TXTtoArray import textArray as ta
from SplitString import splitSentences
from SplitString import splitString
import numpy as np
import optionMenuCreation as omenu
from optionMenuCreation import OptionMenuCreation as omc
import self
import Classifier as classify

global main_root
global bottom_frame
main_root = Tk()
main_root.title("Edit, Summarize, and Tokenize Text with SpaCy")
main_root.geometry("850x450")
main_root.rowconfigure(0, weight=1)
main_root.columnconfigure(0, weight=1)
main_text = "apple"
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
top_frame = Frame(main_root)
top_frame.pack(side=TOP)
train_frame1 = Frame(main_root)
train_frame1.pack(side=TOP)
train_frame2 = Frame(main_root)
train_frame2.pack(side=TOP)
train_frame3 = Frame(main_root)
train_frame3.pack(side=TOP)
button_frame = Frame(main_root)
button_frame.pack(side=TOP)
bottom_frame = Frame(main_root)
bottom_frame.pack(side=BOTTOM)
# globals
global train_data
global sentence_list
global focus_words
global curr_sentence
global count_max
global counter
global wordcounter
global set_num
global drop_menus
global word_selection
train_data = ["Word", "Form", "Sentence"]
sentence_list = ["", ""]
focus_words = [""]
curr_sentence = ""
count_max = 0
counter = 0
wordcounter = 0
word_selection = [24]
set_num = 1



text = ''
title = 'Trainer'
desc = 'Enter text into the text box or load a text file \nthen use the lemmatization tool to prepare your data.' \
       'Then select the type for each of the 6 displayed words. \nThere is a maximum of 120 words per document.'
wordcount = 0


def get_root():
    root = Tk()
    root.title("Edit, Summarize, and Tokenize Text with SpaCy")
    root.geometry("850x450")
    return root

# Read only 'r'
# Read and Write 'r+' (beginning of file)
# Write Only 'w' (over-written)
# Write and Read 'w+' (over written)
# Append Only 'a' (end of file)
# Append and Read 'a+' (end of file)


def sample_txt():
    text_file = open("london.txt", 'r')
    text = text_file.read()
    my_text.insert(END, text)
    text_file.close()


def open_txt():
    text_file = filedialog.askopenfilename(initialdir="C:/Users/")
    text_file = open(text_file, 'r')
    file_location = text_file
    readtext = text_file.read()
    # messagebox.showerror(title="ReadFileError", message="File Type not Accepted")
    self.my_text.insert(END, readtext)
    global text
    text = readtext
    text_file.close()


def save_txt():
    # text_file = open("NewSavedTxt.txt", 'w')
    text_file = filedialog.asksaveasfilename(initialdir="C:/Users/", filetypes=(
                ("Text files", "*.txt"),
                ("Prolog files", "*.pl *.pro"),
                ("All files", "*.*"),
            ))

    text_file = open(text_file, 'w')
    text_file.write(self.my_text.get(1.0, END))
    text_file.close()


def save_file_as(file_path=None):
    # If there is no file path specified, prompt the user with a dialog which
    # allows him/her to select where they want to save the file
    if file_path is None:
        file_path = filedialog.asksaveasfilename(
            filetypes=(
                ("Text files", "*.txt"),
                ("Prolog files", "*.pl *.pro"),
                ("All files", "*.*"),
            )
        )

    try:
        # Write the Prolog rule editor contents to the file location
        self.text = open(file_path, "w")
        text.write(self.my_text.get(1.0, END))
        # text.file_path = file_path
        return "saved"

    except FileNotFoundError:
        return "cancelled"


def save_sentences():
    text_file = open("./SampleText/londonSample.txt", 'r')
    lines = text_file.readlines()
    lines_arr = []
    lines_arr = splitSentences(lines)
    print(lines_arr)
#    text_file = open("./SampleText/sentences.txt", 'w')
#    text_file.writelines("")
#    text_file.writelines(lines_arr)


def open_sample():
    text_file = open("./SampleText/londonSample.txt", 'r')
    global sentence_list
    global focus_words
    global count_max
    global counter
    sentence_list.clear()
    lines = text_file.readlines()
    lines_arr = ["", ""]
    lines_arr = splitSentences(lines)
    # print(lines_arr)
    sentence_list = lines_arr
    count_max = len(lines_arr)-1
    sentence = lines_arr[0].replace(",", "")
    sentence = sentence.replace("\'", "")
    sentence = sentence.replace("\"", "")
    sentence = sentence.replace("!", "")
    focus_words = lines_arr[0].split(" ")
    word_list = focus_words
    show_widget(train_button)
    omc.create_buttons(word_list, train_frame1, train_frame2, train_frame3)


def update_selected():
    global focus_words
    global word_selection
    selection = []
    selection = omenu.getall()
    isReady = TRUE
    result = ""
    for item in selection:
        result += str(item)
        if item == "adjective":
            if item == "adverb":
                if item == "article":
                    if item == "conjunction":
                        if item == "preposition":
                            if item == "pronoun":
                                if item == "noun":
                                    if item == "verb":
                                        isReady = TRUE
                                    else:
                                        isReady = FALSE
    if isReady == TRUE:
        i = 0
        print(focus_words)
        for word in focus_words:
            # print(word+": "+selection[i])
            i += 1
        word_selection = selection
        add_training(selection)
    else:
        Tk.messagebox.showwarning(title="assignments", message="not all data is filled", **options)
        print("not all data is filled")


def extract_data():
    print("hello")


def start_train():
    import optionMenuCreation


def add_training(selection):
    global train_data
    global focus_words
    global wordcounter
    trainer = [[], [], []]
    countb = wordcounter
    word_num = -1
    # for sentence in sentence_list:
    for word in focus_words:
        wordcounter += 1
        word_num += 1
        # train_data.append()
        data = [[word], [word_selection[word_num]], [sentence_list[set_num]]]
        print(data)
        trainer.append(data)
    word_num = -1
    wordlist = ld.lemmatizer(focus_words)
    # for sentence in sentence_list:
    for word in wordlist:
        # train_data.append()
        countb += 1
        word_num += 1
        data = [[word], [word_selection[word_num]], [sentence_list[set_num]]]
        print(data)
        trainer.append(data)
    sd.save_data(trainer)


def hide_widget(widget):
    widget.pack_forget()


def show_widget(widget):
    widget.pack()


# Change the label text
def show(label):
    label.config(text=clicked.get())


def test_text():
    new_sentence = ""
    textbox = my_text.get("1.0",END)
    sentence = textbox.replace(",", "")
    sentence = sentence.replace("\'", "")
    sentence = sentence.replace("\"", "")
    sentence = sentence.replace("!", "")
    words = sentence.split(" ")
    new_words = []
    for word in words:
        varx = classify.getdata(word)
        new_sentence += varx
        new_words.append(varx)
    print(new_words)
    i = 0
    for item in words:
        textbox.replace(item, new_words[i])
        print(textbox)
        i += 1
    my_text.replace("1.0", END, new_words)


fact_label = Label(top_frame, text=title)
fact_label.pack(side=TOP, pady=0)
my_text = Text(top_frame, width=65, height=10, font=("Helvetica", 16))
my_text.pack(side=TOP, pady=10)
open_button = Button(button_frame, text="Open Text File", command=open_txt)
open_button.pack(side=RIGHT, pady=0)
save_button = Button(button_frame, text="Save Text File", command=save_sentences)
save_button.pack(side=RIGHT, pady=0)
redact_button = Button(button_frame, text="start", command=open_sample)
redact_button.pack(side=RIGHT, pady=0)
train_button = Button(button_frame, text="train", command=update_selected)
train_button.pack(side=RIGHT, pady=0)
hide_widget(train_button)
test_button = Button(button_frame, text="test", command=test_text)
test_button.pack(side=RIGHT, pady=0)
detail_label = Label(bottom_frame, text=desc)
detail_label.pack(side=BOTTOM, padx=20, pady=20)

# these are the hidden optionmenus

# datatype of menu text
clicked = StringVar()
# initial menu text
clicked.set(" ")

main_root.mainloop()


def getMyText():
    self.text = self.my_text.get(all)



