from tkinter import *
from tkinter import ttk
import sqlite3

width = 10
root = Tk()
root.option_add("*font", ("Consolas", 10))
value_list = []
# global valuess
valuess = []
# for i in range(1950,2100,1):
#     value_list.append(i)
def getting_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT name from Depart_table")
    for sdf in cmd:
        valuess.append(sdf)
        print(sdf)
    conn.commit()
    conn.close()
    return valuess
monthchoosen = ttk.Combobox(root,values=getting_value())
monthchoosen.grid(column=1, row=5)
Button(root,text="akdaduosgdou",command=lambda :getting_value()).grid()
mainloop()