from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tksheet import Sheet
import sqlite3

# value_list = []
# global valuess
#
# for i in range(1950,2100,1):
#     value_list.append(i)
def getting_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    valuess = []
    cmd.execute(f"SELECT name from Depart_table")
    for sdf in cmd:
        valuess.append(sdf)
        print(sdf)
    conn.commit()
    conn.close()
    return valuess

def data_collector():
    global data_list, i
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute('SELECT * from Program_table');
    data_list = []
    data_free = []
    lok = 65
    i = 1
    for student in cmd:
        for j in range(len(student)):
            data_list.append(student[j])
        data_free.append(data_list)
        data_list = []
        i = i + 1
    conn.close()
    print(data_free)
    return data_free


def values():
    print('Button Created')
def testing(asd):
    # data_collector()
    frame = Frame(asd)

    sheet = Sheet(frame,data=data_collector())
                           # data = [[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(50)] for r in range(500)])
    sheet.enable_bindings()
    frame.grid(row=1, column=4, columnspan=6,rowspan=1)
    sheet.grid(row = 0, column = 0,pady=30)
    # data_collector()
#
#
def STUDENT_FORM_SUBMIT():

    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute("insert into Program_table(Name,Department) values (?,?)",(Program_entry.get(),Department_entry.get(),))
    conn.commit()
    # print(Campus_entry.get())
    print("Data Submited")
    conn.close()
    testing(temp)


class Stu_info_Program(Frame):
    def __init__(self,windows):
        global Program_entry, Department_entry,temp
        Frame.__init__(self)
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/student_zone1.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Pro_Student_Zone_Label = Label(self,borderwidth=0)
        self.Pro_Student_Zone_Label.grid(row=0, column=1, sticky='nsew', columnspan=10)
        Image_Label = Label(self.Pro_Student_Zone_Label, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=10)

        Data_frame = LabelFrame(self.Pro_Student_Zone_Label, text="PROGRAM", font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, pady=34, columnspan=5,ipady=40)

        Student_Session_Label = Label(Data_frame, text="Program Name: ", font=('Helvetica', 12, 'bold'))
        Student_Session_Label.grid(row=0, column=0, pady=60)
        Program_entry = Entry(Data_frame, borderwidth=3, width=32, font=('Helvetica', 12, 'bold'))
        Program_entry.grid(row=0, column=1, padx=30)

        Student_Program_Label = Label(Data_frame, text="Department: ", font=('Helvetica', 12, 'bold'))
        Student_Program_Label.grid(row=1, column=0)
        Department_entry = ttk.Combobox(Data_frame,value = getting_value(), width=30, font=('Helvetica', 12, 'bold'))
        Department_entry.grid(row=1, column=1, padx=30)

        Save_Data = Button(self.Pro_Student_Zone_Label, text="Save Record", image=self.save_ico, compound=LEFT,command=lambda : STUDENT_FORM_SUBMIT())
        Save_Data.grid(row=2, column=0, padx=10)
        Delete_Data = Button(self.Pro_Student_Zone_Label, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=2, column=1, padx=10)
        Update_Data = Button(self.Pro_Student_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=2, column=2, padx=10)

        temp = self.Pro_Student_Zone_Label
        testing(self.Pro_Student_Zone_Label)
        # Gridview = Label(self.Pro_Student_Zone_Label, text="Data GridView: ")
        # Gridview.grid(row=1, column=6, columnspan=3)
        # data_entry_space = Entry(Gridview, borderwidth=10, width=100)
        # data_entry_space.grid(row=0, column=1)
        # data_entry_space.insert(0, "Name: ")



if __name__ == '__main__':
    root = Tk()
    lms = Stu_info_Program(root)
    lms.grid(row=0,column=0)
    mainloop()