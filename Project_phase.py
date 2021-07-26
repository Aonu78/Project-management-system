from tkinter import *
from PIL import Image, ImageTk
from tksheet import Sheet
import sqlite3
from tkinter import ttk


# root.wm_attributes('-fullscreen', 'true')
R_Value = []


def Registration_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT registration_no from student_info")
    for sdf in cmd:
        R_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return R_Value

def data_collector():
    global data_list, i
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute('''SELECT * from Student_Phase_Table''');
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
    frame.grid(row=2, column=0, columnspan=3, rowspan=3)
    sheet.grid(row=0, column=0, sticky="nswe")
    # data_collector()


#
#
def STUDENT_FORM_SUBMIT():
    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute("insert into Student_Phase_Table (Registration_No,Project_Name,Phase,Discription) values (?,?,?,?)",
                (Student_Regis_entry.get(),
                 Student_Name_entry.get(), Student_Phase_entry.get(),
                 Student_Discription_entry.get()), )
    conn.commit()
    # print(Department_entry.get())
    print("Data Submited")

    conn.close()
    testing(temp)


def data_collector1():
    global data_list1, i
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute('''SELECT * from Student_Phase2_Table''');
    data_list1 = []
    data_free = []
    lok = 65
    i = 1
    for student in cmd:
        for j in range(len(student)):
            data_list1.append(student[j])
        data_free.append(data_list1)
        data_list1 = []
        i = i + 1
    conn.close()
    return data_free


def prt1():
    print('Button Created')


def testing1(asd):
    # data_collector()
    frame = Frame(asd)

    sheet = Sheet(frame, data=data_collector1())
    # data = [[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(50)] for r in range(500)])
    sheet.enable_bindings()
    frame.grid(row=2, column=6, columnspan=4,rowspan=3)
    sheet.grid(row=0, column=0, sticky="nswe")
    # data_collector()


#
#
def STUDENT_FORM_SUBMIT1():
    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute("insert into Student_Phase2_Table (Registration_No,Project_Name,Phase,Discription) values (?,?,?,?)",
                (Student_Regis_entry1.get(), Student_Project_name_entry1.get(), Student_Session_entry1.get(),
                 Student_Department_entry1.get()), )
    conn.commit()
    # print(Department_entry.get())
    print("Data Submited")

    conn.close()
    testing1(temp)


class project_phases_class(Frame):
    def __init__(self, windows):
        global temp
        Frame.__init__(self)
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/student_zone1.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Class_Student_Zone_Label = Label(self, borderwidth=0)
        self.Class_Student_Zone_Label.grid(row=0, column=1, sticky='nsew', columnspan=10)
        Image_Label = Label(self.Class_Student_Zone_Label, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=11)

        Data_frame = LabelFrame(self.Class_Student_Zone_Label, text="Project Documentation Phases",
                                font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, columnspan=5)
        global Student_Regis_entry
        Student_Regis_Label = Label(Data_frame, text="Registration No: ", font=('Helvetica', 12, 'bold'))
        Student_Regis_Label.grid(row=0, column=0)
        Student_Regis_entry = ttk.Combobox(Data_frame, value=Registration_value(), width=18, font=('Helvetica', 12, 'bold'))
        Student_Regis_entry.grid(row=0, column=1, pady=5)
        global Student_Name_entry
        Student_Name_Label = Label(Data_frame, text="Project Name: ", font=('Helvetica', 12, 'bold'))
        Student_Name_Label.grid(row=1, column=0)
        Student_Name_entry = Entry(Data_frame, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Student_Name_entry.grid(row=1, column=1, pady=5)
        global Student_Phase_entry
        Student_Phase_Label = Label(Data_frame, text="Phase: ", font=('Helvetica', 12, 'bold'))
        Student_Phase_Label.grid(row=2, column=0)
        Student_Phase_entry = ttk.Combobox(Data_frame, value=['Documentation','Implementation'], width=18, font=('Helvetica', 12, 'bold'))
        Student_Phase_entry.grid(row=2, column=1, pady=5, padx=5)
        global Student_Discription_entry
        Student_Discription_Label = Label(Data_frame, text="Description: ", font=('Helvetica', 12, 'bold'))
        Student_Discription_Label.grid(row=0, column=2)
        Student_Discription_entry = Entry(Data_frame, borderwidth=3, width=25, font=('Helvetica', 12, 'bold'))
        Student_Discription_entry.grid(row=1, column=2, rowspan=3,ipady=20)

        # Grid_frame = LabelFrame(self.Class_Student_Zone_Label, text="grid", font=('Helvetica', 16, 'bold'))
        # Grid_frame.grid(row=2, column=0, columnspan=3,rowspan=3)
        # data_entry_space = Entry(Grid_frame, borderwidth=10, width=40)
        # data_entry_space.grid(row=0, column=1)

        Save_Data = Button(self.Class_Student_Zone_Label, command=lambda: STUDENT_FORM_SUBMIT(), text="Save",
                           image=self.save_ico, compound=LEFT)
        Save_Data.grid(row=2, column=4, sticky='e', ipadx=7)
        Delete_Data = Button(self.Class_Student_Zone_Label, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=3, column=4, sticky='e', ipadx=2)
        Update_Data = Button(self.Class_Student_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=4, column=4, sticky='e')

        Label(self.Class_Student_Zone_Label, bg='#064759').grid(row=1, rowspan=4, column=5, ipady=200)

        Data_frame1 = LabelFrame(self.Class_Student_Zone_Label, text="Project Implementation Phases",
                                 font=('Helvetica', 16, 'bold'))
        Data_frame1.grid(row=1, column=6, columnspan=5, ipadx=10)

        global Student_Regis_entry1
        Student_Regis_Label1 = Label(Data_frame1, text="Registration No: ", font=('Helvetica', 12, 'bold'))
        Student_Regis_Label1.grid(row=0, column=0)
        Student_Regis_entry1 = ttk.Combobox(Data_frame1, value = Registration_value(), width=18, font=('Helvetica', 12, 'bold'))
        Student_Regis_entry1.grid(row=0, column=1, pady=10)
        global Student_Project_name_entry1
        Student_Project_Name_Label1 = Label(Data_frame1, text="Project Name: ", font=('Helvetica', 12, 'bold'))
        Student_Project_Name_Label1.grid(row=1, column=0)
        Student_Project_name_entry1 = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Student_Project_name_entry1.grid(row=1, column=1, pady=10)
        global Student_Session_entry1
        Student_Session_Label1 = Label(Data_frame1, text="Phase: ", font=('Helvetica', 12, 'bold'))
        Student_Session_Label1.grid(row=2, column=0)
        Student_Session_entry1 = ttk.Combobox(Data_frame1, value=['Documentation','Implementation'], width=18, font=('Helvetica', 12, 'bold'))
        Student_Session_entry1.grid(row=2, column=1, padx=5, pady=10)
        global Student_Department_entry1
        Student_Department_Name_Label1 = Label(Data_frame1, text="Description: ", font=('Helvetica', 12, 'bold'))
        Student_Department_Name_Label1.grid(row=0, column=2)
        Student_Department_entry1 = Entry(Data_frame1, borderwidth=3, width=25, font=('Helvetica', 12, 'bold'))
        Student_Department_entry1.grid(row=1, column=2, rowspan=3,ipady=20)

        # Gridview = LabelFrame(self.Class_Student_Zone_Label, text="Data GridView: ")
        # Gridview.grid(row=2, column=6, columnspan=4,rowspan=3)
        # data_entry_space = Entry(Gridview, borderwidth=10, width=40)
        # data_entry_space.grid(row=0, column=1, pady=10)
        # data_entry_space.insert(0, "Name: ")

        Save_Data_Assin = Button(self.Class_Student_Zone_Label, command=lambda: STUDENT_FORM_SUBMIT1(), text="Save",
                                 font=('Helvetica', 12, 'bold'), image=self.save_ico, compound=LEFT)
        Save_Data_Assin.grid(row=2, column=10, sticky='e')
        Delete_Data_Assin = Button(self.Class_Student_Zone_Label, text="Delete", font=('Helvetica', 12, 'bold'),
                                   image=self.delete_ico, compound=LEFT)
        Delete_Data_Assin.grid(row=3, column=10, sticky='e')
        Update_Data_Assin = Button(self.Class_Student_Zone_Label, text="Update", font=('Helvetica', 12, 'bold'),
                                   image=self.update_ico, compound=LEFT)
        Update_Data_Assin.grid(row=4, column=10, sticky='e')

        temp = self.Class_Student_Zone_Label
        testing(self.Class_Student_Zone_Label)
        testing1(self.Class_Student_Zone_Label)


if __name__ == '__main__':
    root = Tk()
    lms = project_phases_class(root)
    lms.grid(row=0, column=0)
    mainloop()
