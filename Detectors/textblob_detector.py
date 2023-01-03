from tkinter import *

from textblob import TextBlob

root = Tk()

root.title("Language Detector using module \"textblob\" By @SmashdFrenzy16")

detector = Entry(root, width=100, borderwidth=5)
detector.pack()
detector.insert(0, "Enter Unknown Language")

def execute():


    detecting = TextBlob(detector.get())
    
    finish_detecting = detecting.detect_language()

    answerlabel = Label(root, text=finish_detecting)
    answerlabel.pack()

enter = Button(root, text="Enter", command=execute)
enter.pack()

root.mainloop()
