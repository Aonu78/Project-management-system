from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
from tksheet import Sheet

R_Value = []
T_Value = []


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
    cmd.execute('''SELECT * from student_enroll''');
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
    frame.grid(row=1, column=3, columnspan=6)
    sheet.grid(row = 0, column = 0,pady=30,ipadx=110)
    # data_collector()
#
#
def STUDENT_FORM_SUBMIT():

    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute("insert into student_enroll (Registration_No,Student_Name,Class_Name,Session,Timing,Department_Name,"
                "Program, Roll_No) values (?,?,?,?,?,?,?,?)",(Student_Regis_entry.get(),Student_Stu_Name_entry.get(),
                                                              Student_Class_Name_entry.get(),Student_Session_entry.get(),
                                                              Student_Timing_entry.get(),Student_Depart_Name_entry.get(),
                                                              Student_Program_entry.get(),Student_Roll_No_entry.get()))
    conn.commit()
    # print(Campus_entry.get())
    print("Data Submited")
    conn.close()
    testing(temp)


class Stu_info_Enroll(Frame):
    def __init__(self,windows):
        global temp
        Frame.__init__(self)
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/student_zone1.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Enroll_Student_Zone_Label = Label(self,borderwidth=0)
        self.Enroll_Student_Zone_Label.grid(row=0, column=1, sticky='nsew', columnspan=10)
        Image_Label = Label(self.Enroll_Student_Zone_Label, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=10)

        Data_frame = LabelFrame(self.Enroll_Student_Zone_Label, text="Student Enrollment", font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, pady=14, columnspan=3)
        global Student_Regis_entry
        Student_Regis_Label = Label(Data_frame, text="Registration No: ", font=('Helvetica', 12, 'bold'))
        Student_Regis_Label.grid(row=0, column=0)
        Student_Regis_entry = ttk.Combobox(Data_frame, value = Registration_value(), width=33, font=('Helvetica', 12, 'bold'))
        Student_Regis_entry.grid(row=0, column=1, pady=5, padx=30)
        global Student_Stu_Name_entry
        Student_Stu_Name_Label = Label(Data_frame, text="Student Name: ", font=('Helvetica', 12, 'bold'))
        Student_Stu_Name_Label.grid(row=1, column=0)
        Student_Stu_Name_entry = Entry(Data_frame, borderwidth=2, width=35, font=('Helvetica', 12, 'bold'))
        Student_Stu_Name_entry.grid(row=1, column=1, pady=5, padx=30)
        global Student_Class_Name_entry
        Student_Class_Name_Label = Label(Data_frame, text="Class Name: ", font=('Helvetica', 12, 'bold'))
        Student_Class_Name_Label.grid(row=2, column=0)
        Student_Class_Name_entry = Entry(Data_frame, borderwidth=2, width=35, font=('Helvetica', 12, 'bold'))
        Student_Class_Name_entry.grid(row=2, column=1, pady=5, padx=30)
        global Student_Session_entry
        Student_Session_Label = Label(Data_frame, text="Session: ", font=('Helvetica', 12, 'bold'))
        Student_Session_Label.grid(row=3, column=0)
        Student_Session_entry = Entry(Data_frame, borderwidth=2, width=35, font=('Helvetica', 12, 'bold'))
        Student_Session_entry.grid(row=3, column=1, pady=5, padx=30)
        global Student_Timing_entry
        Student_Timing_Label = Label(Data_frame, text="Timing: ", font=('Helvetica', 12, 'bold'))
        Student_Timing_Label.grid(row=4, column=0)
        Student_Timing_entry = ttk.Combobox(Data_frame, value=Timing_value(), width=33, font=('Helvetica', 12, 'bold'))
        Student_Timing_entry.grid(row=4, column=1, pady=5, padx=30)
        global Student_Depart_Name_entry
        Student_Depart_Name_Label = Label(Data_frame, text="Department Name: ", font=('Helvetica', 12, 'bold'))
        Student_Depart_Name_Label.grid(row=5, column=0)
        Student_Depart_Name_entry = Entry(Data_frame, borderwidth=2, width=35, font=('Helvetica', 12, 'bold'))
        Student_Depart_Name_entry.grid(row=5, column=1, pady=5, padx=30)
        global Student_Program_entry
        Student_Program_Label = Label(Data_frame, text="Program: ", font=('Helvetica', 12, 'bold'))
        Student_Program_Label.grid(row=6, column=0)
        Student_Program_entry = Entry(Data_frame, borderwidth=2, width=35, font=('Helvetica', 12, 'bold'))
        Student_Program_entry.grid(row=6, column=1, pady=5, padx=30)
        global Student_Roll_No_entry
        Student_Roll_No_Label = Label(Data_frame, text="Roll No: ", font=('Helvetica', 12, 'bold'))
        Student_Roll_No_Label.grid(row=7, column=0)
        Student_Roll_No_entry = Entry(Data_frame, borderwidth=2, width=35, font=('Helvetica', 12, 'bold'))
        Student_Roll_No_entry.grid(row=7, column=1, pady=5, padx=30)

        temp = self.Enroll_Student_Zone_Label
        testing(self.Enroll_Student_Zone_Label)

        Save_Data = Button(self.Enroll_Student_Zone_Label,command=lambda : STUDENT_FORM_SUBMIT(), text="Save Record", image=self.save_ico, compound=LEFT)
        Save_Data.grid(row=2, column=0, padx=10)
        Delete_Data = Button(self.Enroll_Student_Zone_Label, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=2, column=1, padx=10)
        Update_Data = Button(self.Enroll_Student_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=2, column=2, padx=10)

        # Gridview = Label(self.Enroll_Student_Zone_Label, text="Data GridView: ")
        # Gridview.grid(row=1, column=6, columnspan=4)
        # data_entry_space = Entry(Gridview, borderwidth=10, width=100)
        # data_entry_space.grid(row=0, column=1)
        # data_entry_space.insert(0, "Name: ")



if __name__ == '__main__':
    root = Tk()
    lms = Stu_info_Enroll(root)
    lms.grid(row=0,column=0)
    mainloop()