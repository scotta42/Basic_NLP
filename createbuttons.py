
def create_buttons(str_list):
    global curr_sentence
    global wordcounter
    global drop_menus
    arr = ["cheese", "banana", "anchovi"]
    arr.clear()
    arr = str_list
    curr_sentence = str_list
    global counter
    i = 0
    j = 1
    count = 0
    # Create a 6x7 array of zeros as the one you used

    for item in arr:
        if i == 0:
            label = Label(train_frame1, text=item)
            label.pack(side=LEFT)
            # datatype of menu text
            clicked = StringVar()
            # initial menu text
            clicked.set(" ")
            # Create Dropdown menu
            drop = OptionMenu(train_frame1, clicked, *options, command=update_selected)
            drop.pack(side=LEFT)

            # Create Label
            j += 1
            counter += 1
            count += 1
        if i == 1:
            label = Label(train_frame2, text=item)
            label.pack(side=LEFT)
            # datatype of menu text
            clicked = StringVar()
            # initial menu text
            clicked.set(" ")
            # Create Dropdown menu
            drop = OptionMenu(train_frame2, clicked, *options)
            drop.pack(side=LEFT)
            # Create Label
            j += 1
            counter += 1
        if i == 2:
            label = Label(train_frame3, text=item)
            label.pack(side=LEFT)
            # datatype of menu text
            clicked = StringVar()
            # initial menu text
            clicked.set(" ")
            # Create Dropdown menu
            drop = OptionMenu(train_frame3, clicked, *options)
            drop.pack(side=LEFT)
            # Create Label
            j += 1
            counter += 1
        if j > 8:
            i += 1
            j = 1
