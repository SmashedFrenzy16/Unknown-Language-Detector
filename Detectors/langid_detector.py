from tkinter import *

import langid

root = Tk()

root.title("Language Detector using module \"langid\" By @SmashdFrenzy16")

detector = Entry(root, width=100, borderwidth=5)
detector.pack()
detector.insert(0, "Enter Unknown Language")

def execute():


    detecting = langid.classify(detector.get())

    answerlabel = Label(root, text=detecting)
    answerlabel.pack()

enter = Button(root, text="Enter", command=execute)
enter.pack()

root.mainloop()
