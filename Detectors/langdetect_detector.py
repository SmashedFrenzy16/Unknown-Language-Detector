from tkinter import *

from langcodes import *

from langdetect import detect

root = Tk()

root.title("Language Detector using module \"langdetect\" By @SmashdFrenzy16")

detector = Entry(root, width=100, borderwidth=5)
detector.pack()
detector.insert(0, "Enter Unknown Language")

def execute():


    detecting = detect(detector.get())
    
    final = Language.make(language = detecting).display_name()

    answerlabel = Label(root, text=final)
    answerlabel.pack()

enter = Button(root, text="Enter", command=execute)
enter.pack()

root.mainloop()
