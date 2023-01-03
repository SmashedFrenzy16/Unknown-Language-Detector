from tkinter import *

from langcodes import *

import langid

root = Tk()

root.title("Language Detector using module \"langid\" By @SmashdFrenzy16")

detector = Entry(root, width=100, borderwidth=5)
detector.pack()
detector.insert(0, "Enter Unknown Language")

def execute():


    detecting = langid.classify(detector.get())
    
    final = Language.make(language = detecting).display_name()

    answerlabel = Label(root, text=final)
    answerlabel.pack()

enter = Button(root, text="Enter", command=execute)
enter.pack()

root.mainloop()
