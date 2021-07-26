from tkinter import *
from PIL import Image,ImageTk
from tksheet import Sheet
import sqlite3
from tkinter import ttk

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
    cmd.execute('''SELECT * from Internal_Supervisor_Tabel''');
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
    frame.grid(row=1, column=6, columnspan=3)
    sheet.grid(row=0, column=0, sticky="nswe")
    # data_collector()


#
#
def STUDENT_FORM_SUBMIT():
    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute("insert into Internal_Supervisor_Tabel (Supervisor_Name,"
                "Designation,Department,Employment_Code,Phone_No,Mobile_No,E_Mail) values (?,?,?,"
                "?,?,?,?)",(Supervisor_entry.get(),Designation_entry.get(),Department_entry.get(),Employment_entry.get(),
                            Phone_entry.get(),Mobile_entry.get(),E_Mail_entry.get()),)
    conn.commit()
    # print(Department_entry.get())
    print("Data Submited")

    conn.close()
    testing(temp)


class Int_supervisor(Frame):
    def __init__(self,windows):
        global temp
        Frame.__init__(self)
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/super viser.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Project_Zone_Label = Label(self,borderwidth=0)
        self.Project_Zone_Label.grid(row=0, column=1, sticky='nsew', columnspan=10)
        Image_Label = Label(self.Project_Zone_Label, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=10)

        Data_frame = LabelFrame(self.Project_Zone_Label, text="Internal Supervisor Information ", font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, pady=14, columnspan=5,rowspan=5)
        global Supervisor_entry
        Supervisor_Label = Label(Data_frame, text="Supervisor Name: ", font=('Helvetica', 12, 'bold'))
        Supervisor_Label.grid(row=0, column=0)
        Supervisor_entry = Entry(Data_frame, borderwidth=2, width=40, font=('Helvetica', 12, 'bold'))
        Supervisor_entry.grid(row=0, column=1, pady=10, padx=30)
        global Designation_entry
        Designation_Label = Label(Data_frame, text="Designation: ", font=('Helvetica', 12, 'bold'))
        Designation_Label.grid(row=1, column=0)
        Designation_entry = ttk.Combobox(Data_frame, value=Designation_value(), width=38, font=('Helvetica', 12, 'bold'))
        Designation_entry.grid(row=1, column=1, pady=10, padx=30)
        global Department_entry
        Department_Label = Label(Data_frame, text="Department: ", font=('Helvetica', 12, 'bold'))
        Department_Label.grid(row=2, column=0)
        Department_entry = ttk.Combobox(Data_frame, value=Department_value(), width=38, font=('Helvetica', 12, 'bold'))
        Department_entry.grid(row=2, column=1, pady=10, padx=30)
        global Employment_entry
        Employment_Label = Label(Data_frame, text="Employment Code: ", font=('Helvetica', 12, 'bold'))
        Employment_Label.grid(row=3, column=0)
        Employment_entry = Entry(Data_frame, borderwidth=2, width=40, font=('Helvetica', 12, 'bold'))
        Employment_entry.grid(row=3, column=1, pady=10, padx=30)
        global Phone_entry
        Phone_Label = Label(Data_frame, text="Phone No: ", font=('Helvetica', 12, 'bold'))
        Phone_Label.grid(row=4, column=0)
        Phone_entry = Entry(Data_frame, borderwidth=2, width=40, font=('Helvetica', 12, 'bold'))
        Phone_entry.grid(row=4, column=1, pady=10, padx=30)
        global Mobile_entry
        Mobile_Label = Label(Data_frame, text="Mobile No: ", font=('Helvetica', 12, 'bold'))
        Mobile_Label.grid(row=5, column=0)
        Mobile_entry = Entry(Data_frame, borderwidth=2, width=40, font=('Helvetica', 12, 'bold'))
        Mobile_entry.grid(row=5, column=1, pady=10, padx=30)
        global E_Mail_entry
        E_Mail_Label = Label(Data_frame, text="E_Mail: ", font=('Helvetica', 12, 'bold'))
        E_Mail_Label.grid(row=6, column=0)
        E_Mail_entry = Entry(Data_frame, borderwidth=2, width=40, font=('Helvetica', 12, 'bold'))
        E_Mail_entry.grid(row=6, column=1, pady=10, padx=30)

        Save_Data = Button(self.Project_Zone_Label,command=lambda:STUDENT_FORM_SUBMIT(), text="Save Record", image=self.save_ico, compound=LEFT)
        Save_Data.grid(row=5, column=6, padx=10)
        Delete_Data = Button(self.Project_Zone_Label, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=5, column=7, padx=10)
        Update_Data = Button(self.Project_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=5, column=8, padx=10)
        temp = self.Project_Zone_Label
        testing(self.Project_Zone_Label)
        # Gridview = Label(self.Project_Zone_Label, text="Data GridView: ")
        # Gridview.grid(row=1, column=6, columnspan=3)
        # data_entry_space = Entry(Gridview, borderwidth=10, width=100)
        # data_entry_space.grid(row=0, column=1)
        # data_entry_space.insert(0, "Name: ")



if __name__ == '__main__':
    root = Tk()
    lms = Int_supervisor(root)
    lms.grid(row=0,column=0)
    mainloop()