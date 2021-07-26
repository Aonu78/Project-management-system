from tkinter import *
import GUI1
import GUI2

# the first gui owns the root window
root = Tk()
gui1 = GUI1.GUI(root)
gui1.pack(fill="both", expand=True)

# the second GUI is in a Toplevel
win2 = Toplevel(root)
gui2 = GUI2.GUI(win2)
gui2.pack(fill="both", expand=True)

mainloop()