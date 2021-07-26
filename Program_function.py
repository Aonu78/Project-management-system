from tkinter import *
import random
import setup
from PIL import Image,ImageTk
screen = Tk()
lpc = globals()[setup.ima]
result = Label(screen,text='cksdckjs')
result.grid(row=0,column=0)
def generate():
        random_number = random.randint(1, 1000)
        result['text'] = "Number: " + str(random_number)
        # result = Label(screen,text='kfsufgouygfouewf',image = globals()[setup.ima]).grid(row=0,column=0)

text = Label(screen, text="Click to generate a random number:")
text.grid(row=1,column=0)

button = Button(screen, text="GENERATE!", command=generate, fg="yellow",                 
bg="purple")
button.grid(row=2,column=0)

screen.mainloop()