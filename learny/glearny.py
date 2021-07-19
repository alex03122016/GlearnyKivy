#from sys import version_info

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from learny import clozetest, wordsearch, PresentOrPast, colorsyllables, infinitive, specialwords
#from learny import *

#colorsyllables
"""def colorSyllables ():
    x1 = entry1.get("1.0", "end-1c")
    colorsyllables.color_syllables(x1)
"""
def clozeTest ():
    x1 = entry1.get("1.0", "end-1c")
    clozetest.cloze_test(x1, "Sprache: Deutsch")

#wordsearch
def wordSearch ():
    x1 = entry1.get("1.0", "end-1c")
    words = specialwords.nouns(x1, "Sprache: Deutsch")
    wordsearch.wordsearch(words)

def presentOrPast ():
    x1 = entry1.get("1.0", "end-1c")
    PresentOrPast.present_or_past(x1, "Sprache: Deutsch")

#def infinitive
def infinitiveGet():
    x1 = entry1.get("1.0", "end-1c")
    infinitive.infinitive(x1, "Sprache: Deutsch")

app = tk.Tk()
p1 = PhotoImage(file = '/home/alex/Dokumente/guis/learny.png')

app.iconphoto(False, p1)
app.title("learny")
canvas1 = tk.Canvas(app, width = 400, height = 300)
canvas1.configure(background="lightgreen")


entry1 = tk.Text (app, width= 40, height=5)
canvas1.create_window(200, 140, window=entry1)

#colorsyllables Btn
"""colorsyllables_Btn = tk.Button(text='Silben', command=colorSyllables)
colorsyllables_Btn.configure(background="green", fg='#ffffff', borderwidth=0)
canvas1.create_window(100, 220, window=colorsyllables_Btn)
canvas1.pack()
"""
#cloze Test Btn
Lueckentext_Btn = tk.Button(text='Lückentext', command=clozeTest)
Lueckentext_Btn.configure(background="green", fg='#ffffff', borderwidth=0)
canvas1.create_window(200, 220, window=Lueckentext_Btn)
canvas1.pack()

#wordsearch Btn
wordsearch_Btn = tk.Button(text='Suchsel', command=wordSearch)
wordsearch_Btn.configure(background="green", fg='#ffffff', borderwidth=0)
canvas1.create_window(100, 260, window=wordsearch_Btn)
canvas1.pack()

#presentorpast Btn
presentOrPast_Btn = tk.Button(text='Zeitformen', command=presentOrPast)
presentOrPast_Btn.configure(background="green", fg='#ffffff', borderwidth=0)
canvas1.create_window(300, 220, window=presentOrPast_Btn)

#infinitive Btn
infinitive_Btn = tk.Button(text='Infinitiv', command=infinitiveGet)
infinitive_Btn.configure(background="green", fg='#ffffff', borderwidth=0)
canvas1.create_window(200, 260, window=infinitive_Btn)

app.mainloop()
