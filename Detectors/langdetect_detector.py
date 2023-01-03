from tkinter import *

from langdetect import detect

root = Tk()

root.title("Language Detector using module \"langdetect\" By @SmashdFrenzy16")

detector = Entry(root, width=100, borderwidth=5)
detector.pack()
detector.insert(0, "Enter Unknown Language")

def execute():


    detecting = detect(detector.get())

    answerlabel = Label(root, text=detecting)
    answerlabel.pack()

enter = Button(root, text="Enter", command=execute)
enter.pack()

root.mainloop()
