from tksheet import Sheet
import sqlite3
import numpy as np
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from tksheet import Sheet
import sqlite3


# root.wm_attributes('-fullscreen', 'true')
D_Value = []
De_Value = []


def Designation_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT designation from Internal_designation")
    for sdf in cmd:
        D_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return D_Value

def Department_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT name from Depart_table")
    for sdf in cmd:
        De_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return De_Value

def data_collector():
    global data_list, i
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute('''SELECT * from External_Supervisor_Table''');
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
    return data_free


def prt():
    print('Button Created')


def testing(asd):
    # data_collector()
    frame = Frame(asd)

    sheet = Sheet(frame, data=data_collector())
    # data = [[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(50)] for r in range(500)])
    sheet.enable_bindings()
    frame.grid(row=1, column=4, columnspan=5)
    sheet.grid(row=0, column=0, sticky="nswe",ipadx=80)
    # data_collector()


#
#
def STUDENT_FORM_SUBMIT():
    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute('insert into External_Supervisor_Table (Supervisor,Organization,Designation,Department,'
                'Phone,Mobile,E_Mail) values (?,?,?,?,?,?,?)', (Supervisor_Name_Entry.get(), Organization_entry.get(),
                                                                Designation_entry.get(), Department_entry.get(),
                                                                Ptcl_No_entry.get(), Mobile_No_entry.get(),
                                                                email_entry.get()))

    conn.commit()
    # print(Department_entry.get())
    print("Data Submited")

    conn.close()
    testing(temp)





class Supervisor_Info(Frame):
    def __init__(self, window):
        Frame.__init__(self)
        global temp
        # super().__init__(**kw)
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/external_header.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Student_Zone_Label = Label(self)
        self.Student_Zone_Label.grid(row=2, column=1, sticky='nsew')
        Image_Label = Label(self.Student_Zone_Label, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=10)
        Data_frame = LabelFrame(self.Student_Zone_Label, text="External Supervisor Information",
                                font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, columnspan=3, rowspan=2)
        global Supervisor_Name_Entry
        Supervisor_Name_Label = Label(Data_frame, text="Supervisor Name: ", font=('Helvetica', 12, 'bold'))
        Supervisor_Name_Label.grid(row=0, column=0)
        Supervisor_Name_Entry = Entry(Data_frame, borderwidth=2, width=40, font=('Helvetica', 12, 'bold'))
        Supervisor_Name_Entry.grid(row=0, column=1, pady=12)
        global Organization_entry
        Organization_Label = Label(Data_frame, text="Organization: ", font=('Helvetica', 12, 'bold'))
        Organization_Label.grid(row=1, column=0)
        Organization_entry = Entry(Data_frame, borderwidth=2, width=40, font=('Helvetica', 12, 'bold'))
        Organization_entry.grid(row=1, column=1, pady=12)
        global Designation_entry
        Designation_Label = Label(Data_frame, text="Designation: ", font=('Helvetica', 12, 'bold'))
        Designation_Label.grid(row=2, column=0)
        Designation_entry = ttk.Combobox(Data_frame, value=Designation_value(), width=38, font=('Helvetica', 12, 'bold'))
        Designation_entry.grid(row=2, column=1, pady=12)
        global Department_entry
        Department_Label = Label(Data_frame, text="Department: ", font=('Helvetica', 12, 'bold'))
        Department_Label.grid(row=3, column=0)
        Department_entry = ttk.Combobox(Data_frame, value=Department_value(), width=38, font=('Helvetica', 12, 'bold'))
        Department_entry.grid(row=3, column=1, pady=12)
        global Ptcl_No_entry
        Ptcl_No_Label = Label(Data_frame, text="PTCL No: ", font=('Helvetica', 12, 'bold'))
        Ptcl_No_Label.grid(row=4, column=0)
        Ptcl_No_entry = Entry(Data_frame, borderwidth=2, width=40, font=('Helvetica', 12, 'bold'))
        Ptcl_No_entry.grid(row=4, column=1, pady=12)
        global Mobile_No_entry
        Mobile_No_Label = Label(Data_frame, text="Mobile No", font=('Helvetica', 12, 'bold'))
        Mobile_No_Label.grid(row=5, column=0)
        Mobile_No_entry = Entry(Data_frame, borderwidth=2, width=40, font=('Helvetica', 12, 'bold'))
        Mobile_No_entry.grid(row=5, column=1, pady=12)
        # Mobile_No_entry.bind('<KeyPress>', self.keybind1)
        # Mobile_No_entry.focus()
        global email_entry
        email_Label = Label(Data_frame, text="E_Mail", font=('Helvetica', 12, 'bold'))
        email_Label.grid(row=6, column=0)
        email_entry = Entry(Data_frame, borderwidth=2, width=40, font=('Helvetica', 12, 'bold'))
        email_entry.grid(row=6, column=1, pady=12)

        temp = self.Student_Zone_Label
        testing(self.Student_Zone_Label)

        ############+=====================
        Save_Data = Button(self.Student_Zone_Label, command=lambda: STUDENT_FORM_SUBMIT(), text="Save Record",
                           image=self.save_ico, compound=LEFT)
        Save_Data.bind("<Button-1>", testing(self.Student_Zone_Label))
        Save_Data.grid(row=2, column=5, padx=10)
        Delete_Data = Button(self.Student_Zone_Label, text="Delete", image=self.delete_ico,
                             compound=LEFT)
        Delete_Data.grid(row=2, column=6, padx=10)
        Update_Data = Button(self.Student_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=2, column=7, padx=10)

    # def keybind1(self, event):
    #     if event.int in np.linspace(0, 9):
    #         print(event.int)

if __name__ == "__main__":
    root = Tk()
    root.wm_attributes("-topmost", True)
    gui = Supervisor_Info(root)
    gui.grid(row=2, column=1, sticky='nsew')
    mainloop()
