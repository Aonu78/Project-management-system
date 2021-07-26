from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
from tksheet import Sheet


D_Value = []
P_Value = []
S_Value = []
T_Value = []
C_Value = []
R_Value = []
# Data Class


def Department_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT name from Depart_table")
    for sdf in cmd:
        D_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return D_Value


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


def Class_Name_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT class_name from student_class")
    for sdf in cmd:
        C_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return C_Value


def Timing_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT Timing_Name from Timetable")
    for sdf in cmd:
        T_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return T_Value


def Program_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT Name from Program_table")
    for sdf in cmd:
        P_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return P_Value


def Session_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT Session from Session_table")
    for sdf in cmd:
        S_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return S_Value


def data_collector():
    global data_list, i
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute('''SELECT * from student_class''');
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

    sheet = Sheet(frame,data=data_collector())
                           # data = [[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(50)] for r in range(500)])
    sheet.enable_bindings()
    frame.grid(row=2, column=0, columnspan=3,rowspan=3)
    sheet.grid(row = 0, column = 0,pady=30)
    # data_collector()


def STUDENT_FORM_SUBMIT():

    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute("insert into student_class (class_name,student_department_name,session,program,"
                "timing) values (?,?,?,?,?)",(Student_Class_entry.get(),Student_Department_entry.get(),Student_Session_entry1.get(),Student_Program_entry.get(),Student_Timing_entry.get(),))
    conn.commit()
    # print(Campus_entry.get())
    print("Data Submited")
    conn.close()
    testing(temp)

# Assign Class


def data_collector1():
    global data_list1, i
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute('''SELECT * from student_class_assign''');
    data_list1 = []
    data_free = []
    lok = 65
    i = 1
    for student in cmd:
        print(student)
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

    sheet = Sheet(frame,data=data_collector1())
                           # data = [[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(50)] for r in range(500)])
    sheet.enable_bindings()
    frame.grid(row=2, column=6, columnspan=4,rowspan=3)
    sheet.grid(row = 0, column = 0,pady=30)
    # data_collector()
#
#
def STUDENT_FORM_SUBMIT1():

    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute("insert into student_class_assign (Registration_No,Session,Class_Name) values (?,?,?)",(Student_Regis_entry.get(),Student_Session_entry.get(),Student_Class_name_entry.get(),))
    conn.commit()
    # print(Campus_entry.get())
    print("Data Submited")
    conn.close()
    testing1(temp)


class Stu_info_Class(Frame):
    def __init__(self,windows):
        global Student_Session_entry,Student_Class_name_entry,Student_Regis_entry
        global Student_Timing_entry, Student_Program_entry, Student_Session_entry1, Student_Department_entry, Student_Class_entry, temp
        Frame.__init__(self)
        # self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/student_zone1.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Class_Student_Zone_Label = Label(self,borderwidth=0)
        self.Class_Student_Zone_Label.grid(row=0, column=1, sticky='nsew', columnspan=10)
        # Image_Label = Label(self.Class_Student_Zone_Label, image=self.img_stu)
        # Image_Label.grid(row=0, column=0, columnspan=11)

        Data_frame = LabelFrame(self.Class_Student_Zone_Label, text="CLASS", font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, columnspan=5,ipadx=30)

        Student_Class_Label = Label(Data_frame, text="Class Name: ", font=('Helvetica', 12, 'bold'))
        Student_Class_Label.grid(row=0, column=0)
        Student_Class_entry = Entry(Data_frame, borderwidth=3, width=15, font=('Helvetica', 12, 'bold'))
        Student_Class_entry.grid(row=0, column=1)

        Student_Session_Label = Label(Data_frame, text="Session: ", font=('Helvetica', 12, 'bold'))
        Student_Session_Label.grid(row=1, column=0)
        Student_Session_entry1 = ttk.Combobox(Data_frame,value=Session_value(), width=15, font=('Helvetica', 12, 'bold'))
        Student_Session_entry1.grid(row=1, column=1)

        Student_Department_Name_Label = Label(Data_frame, text="Department Name: ", font=('Helvetica', 12, 'bold'))
        Student_Department_Name_Label.grid(row=0, column=2)
        Student_Department_entry = ttk.Combobox(Data_frame, value=Department_value(), width=15, font=('Helvetica', 12, 'bold'))
        Student_Department_entry.grid(row=0, column=3, pady=10)

        Student_Program_Label = Label(Data_frame, text="Program: ", font=('Helvetica', 12, 'bold'))
        Student_Program_Label.grid(row=1, column=2)
        Student_Program_entry = ttk.Combobox(Data_frame, value=Program_value(), width=15, font=('Helvetica', 12, 'bold'))
        Student_Program_entry.grid(row=1, column=3, pady=10)

        Student_Timing_Label = Label(Data_frame, text="Timing: ", font=('Helvetica', 12, 'bold'))
        Student_Timing_Label.grid(row=2, column=2)
        Student_Timing_entry = ttk.Combobox(Data_frame, value=Timing_value(), width=15, font=('Helvetica', 12, 'bold'))
        Student_Timing_entry.grid(row=2, column=3, pady=10)
        temp = self.Class_Student_Zone_Label
        testing(self.Class_Student_Zone_Label)

        # Grid_frame = LabelFrame(self.Class_Student_Zone_Label, text="grid", font=('Helvetica', 16, 'bold'))
        # Grid_frame.grid(row=2, column=0, columnspan=3,rowspan=3)
        # data_entry_space = Entry(Grid_frame, borderwidth=10, width=40)
        # data_entry_space.grid(row=0, column=1)

        Save_Data = Button(self.Class_Student_Zone_Label,command=lambda: STUDENT_FORM_SUBMIT(), text="Save Record", image=self.save_ico, compound=LEFT)
        Save_Data.grid(row=2, column=4,sticky='e')
        Delete_Data = Button(self.Class_Student_Zone_Label, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=3, column=4,sticky='e')
        Update_Data = Button(self.Class_Student_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=4, column=4,sticky='e')

        Label(self.Class_Student_Zone_Label,bg='#064759').grid(row=1,rowspan=4,column=5,ipady=200)

        Data_frame1 = LabelFrame(self.Class_Student_Zone_Label, text="Assign Class", font=('Helvetica', 16, 'bold'))
        Data_frame1.grid(row=1, column=6, columnspan=5,ipadx=30,ipady=23)

        Student_Regis_Label = Label(Data_frame1, text="Registration No: ", font=('Helvetica', 12, 'bold'))
        Student_Regis_Label.grid(row=0, column=0)
        Student_Regis_entry = ttk.Combobox(Data_frame1, value=Registration_value(), width=15, font=('Helvetica', 12, 'bold'))
        Student_Regis_entry.grid(row=0, column=1, pady=10)

        Student_Class_Name_Label = Label(Data_frame1, text="Class Name: ", font=('Helvetica', 12, 'bold'))
        Student_Class_Name_Label.grid(row=1, column=0)
        Student_Class_name_entry = ttk.Combobox(Data_frame1, value=Class_Name_value(), width=15, font=('Helvetica', 12, 'bold'))
        Student_Class_name_entry.grid(row=1, column=1, pady=10)

        Student_Session_Label = Label(Data_frame1, text="Session: ", font=('Helvetica', 12, 'bold'))
        Student_Session_Label.grid(row=0, column=2)
        Student_Session_entry = ttk.Combobox(Data_frame1, value=Session_value(), width=15, font=('Helvetica', 12, 'bold'))
        Student_Session_entry.grid(row=0, column=3, pady=10)

        testing1(self.Class_Student_Zone_Label)
        # Gridview = LabelFrame(self.Class_Student_Zone_Label, text="Data GridView: ")
        # Gridview.grid(row=2, column=6, columnspan=4,rowspan=3)
        # data_entry_space = Entry(Gridview, borderwidth=10, width=40)
        # data_entry_space.grid(row=0, column=1, pady=10)
        # data_entry_space.insert(0, "Name: ")

        Save_Data_Assin = Button(self.Class_Student_Zone_Label,command=lambda: STUDENT_FORM_SUBMIT1(), text="Save Record", image=self.save_ico, compound=LEFT)
        Save_Data_Assin.grid(row=2, column=10,sticky='e')
        Delete_Data_Assin = Button(self.Class_Student_Zone_Label, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data_Assin.grid(row=3, column=10,sticky='e')
        Update_Data_Assin = Button(self.Class_Student_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data_Assin.grid(row=4, column=10,sticky='e')


if __name__ == '__main__':
    root = Tk()
    lms = Stu_info_Class(root)
    lms.grid(row=0,column=0)
    mainloop()