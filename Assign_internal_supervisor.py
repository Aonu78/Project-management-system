from tkinter import *
from PIL import Image,ImageTk
from tksheet import Sheet
import sqlite3
from tkinter import ttk

# root.wm_attributes('-fullscreen', 'true')
D_Value = []
P_Value = []
S_Value = []
T_Value = []
C_Value = []
# ws['bg']='#fb0


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
    cmd.execute('''SELECT * from Assign_Internal_Supervisor_Tabel''');
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
    frame.grid(row=1, column=6,rowspan=4,columnspan=3)
    sheet.grid(row=0, column=0,ipadx=60, sticky="nswe")
    # data_collector()


#
#
def STUDENT_FORM_SUBMIT():
    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute("insert into Assign_Internal_Supervisor_Tabel (Registration_No,Student_Name,"
                "Class_Name,Session,Timing,Department_Name,Program, Roll_No,"
                "Employment_Code,Internal_Name,Designation,Department,Mobile_No,"
                "E_Mail) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(Registration_entry.get(),Student_Name_entry.get(),Student_Class_entry.get(),
                                Student_Session_entry.get(),Student_Time_entry.get(),Student_Department_entry.get(),
                                Student_Program_entry.get(),Student_ROLL_entry.get(),Employee_entry.get(),Internal_entry.get(),
                                Designation_entry.get(),Department_entry.get(),Mobile_entry.get(),E_Mail_entry.get()),)
    conn.commit()
    # print(Department_entry.get())
    print("Data Submited")

    conn.close()
    testing(temp)


class Int_supervisor(Frame):
    def __init__(self,windows):
        global temp
        Frame.__init__(self)
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/assign internal.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Project_Zone_Label = Label(self,borderwidth=0)
        self.Project_Zone_Label.grid(row=0, column=1, sticky='nsew', columnspan=10)
        Image_Label = Label(self.Project_Zone_Label, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=10)

        Data_frame = LabelFrame(self.Project_Zone_Label, text="Select Department, Class & Session", font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, columnspan=2,ipadx=20)

        Student_Time_Label = Label(Data_frame, text="Department: ", font=('Helvetica', 12, 'bold'))
        Student_Time_Label.grid(row=0, column=0)
        Student_entry = ttk.Combobox(Data_frame, value=Department_value(), width=20, font=('Helvetica', 12, 'bold'))
        Student_entry.grid(row=0, column=1, pady=10)

        Student_Time_Label = Label(Data_frame, text="Session: ", font=('Helvetica', 12, 'bold'))
        Student_Time_Label.grid(row=0, column=2)
        Student_entry = ttk.Combobox(Data_frame, value=Session_value(), width=20, font=('Helvetica', 12, 'bold'))
        Student_entry.grid(row=0, column=3, pady=10)

        Student_Time_Label = Label(Data_frame, text="Class Name: ", font=('Helvetica', 12, 'bold'))
        Student_Time_Label.grid(row=1, column=0)
        Student_entry = ttk.Combobox(Data_frame, value=Class_Name_value(), width=20, font=('Helvetica', 12, 'bold'))
        Student_entry.grid(row=1, column=1, pady=10)

        Student_Time_Label = Label(Data_frame, text="Timing: ", font=('Helvetica', 12, 'bold'))
        Student_Time_Label.grid(row=1, column=2)
        Student_entry = ttk.Combobox(Data_frame, value=Timing_value(), width=20, font=('Helvetica', 12, 'bold'))
        Student_entry.grid(row=1, column=3, pady=10)

        # frame2
        Data_frame1 = LabelFrame(self.Project_Zone_Label, text="Student Information",
                                font=('Helvetica', 12, 'bold'))
        Data_frame1.grid(row=2, column=0,rowspan=5)
        global Registration_entry
        Registration_Label = Label(Data_frame1, text="Registration No: ", font=('Helvetica', 12))
        Registration_Label.grid(row=0, column=0)
        Registration_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12))
        Registration_entry.grid(row=0, column=1, pady=2)
        global Student_Name_entry
        Student_Name_Label = Label(Data_frame1, text="Student Name: ", font=('Helvetica', 12))
        Student_Name_Label.grid(row=1, column=0)
        Student_Name_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12))
        Student_Name_entry.grid(row=1, column=1, pady=2)
        global Student_Class_entry
        Student_Class_Label = Label(Data_frame1, text="Class Name: ", font=('Helvetica', 12))
        Student_Class_Label.grid(row=2, column=0)
        Student_Class_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12))
        Student_Class_entry.grid(row=2, column=1, pady=2)
        global Student_Session_entry
        Student_Session_Label = Label(Data_frame1, text="Session: ", font=('Helvetica', 12))
        Student_Session_Label.grid(row=3, column=0)
        Student_Session_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12))
        Student_Session_entry.grid(row=3, column=1, pady=2)
        global Student_Time_entry
        Student_Time_Label = Label(Data_frame1, text="Timing: ", font=('Helvetica', 12))
        Student_Time_Label.grid(row=4, column=0)
        Student_Time_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12))
        Student_Time_entry.grid(row=4, column=1, pady=2)
        global Student_Department_entry
        Student_Department_Label = Label(Data_frame1, text="Department: ", font=('Helvetica', 12))
        Student_Department_Label.grid(row=5, column=0)
        Student_Department_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12))
        Student_Department_entry.grid(row=5, column=1, pady=2)
        global Student_Program_entry
        Student_Program_Label = Label(Data_frame1, text="Program: ", font=('Helvetica', 12))
        Student_Program_Label.grid(row=6, column=0)
        Student_Program_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12))
        Student_Program_entry.grid(row=6, column=1, pady=2)
        global Student_ROLL_entry
        Student_ROLL_Label = Label(Data_frame1, text="Roll No: ", font=('Helvetica', 12))
        Student_ROLL_Label.grid(row=7, column=0)
        Student_ROLL_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12))
        Student_ROLL_entry.grid(row=7, column=1, pady=2)
        #

        Data_frame2 = LabelFrame(self.Project_Zone_Label, text="Internal Supervisor",font=('Helvetica', 12, 'bold'))
        Data_frame2.grid(row=2, column=1)
        global Employee_entry
        Employee_Label = Label(Data_frame2, text="Employee Code: ", font=('Helvetica', 12))
        Employee_Label.grid(row=0, column=0)
        Employee_entry = Entry(Data_frame2, borderwidth=3, width=20, font=('Helvetica', 12))
        Employee_entry.grid(row=0, column=1, pady=2,columnspan=2)
        global Internal_entry
        Internal_Label = Label(Data_frame2, text="Internal Name: ", font=('Helvetica'))
        Internal_Label.grid(row=1, column=0)
        Internal_entry = Entry(Data_frame2, borderwidth=3, width=20, font=('Helvetica', 12))
        Internal_entry.grid(row=1, column=1, pady=2,columnspan=2)
        global Designation_entry
        Designation_Label = Label(Data_frame2, text="Designation: ", font=('Helvetica', 12))
        Designation_Label.grid(row=2, column=0)
        Designation_entry = Entry(Data_frame2, borderwidth=3, width=20, font=('Helvetica', 12))
        Designation_entry.grid(row=2, column=1, pady=2,columnspan=2)
        global Department_entry
        Department_Label = Label(Data_frame2, text="Department: ", font=('Helvetica', 12))
        Department_Label.grid(row=3, column=0)
        Department_entry = Entry(Data_frame2, borderwidth=3, width=20, font=('Helvetica', 12))
        Department_entry.grid(row=3, column=1, pady=2,columnspan=2)
        global Mobile_entry
        Mobile_Label = Label(Data_frame2, text="Mobile No: ", font=('Helvetica', 12))
        Mobile_Label.grid(row=4, column=0)
        Mobile_entry = Entry(Data_frame2, borderwidth=3, width=20, font=('Helvetica', 12))
        Mobile_entry.grid(row=4, column=1, pady=2,columnspan=2)
        global E_Mail_entry
        E_Mail_Label = Label(Data_frame2, text="E_Mail: ", font=('Helvetica', 12))
        E_Mail_Label.grid(row=5, column=0)
        E_Mail_entry = Entry(Data_frame2, borderwidth=3, width=20, font=('Helvetica', 12))
        E_Mail_entry.grid(row=5, column=1, pady=2,columnspan=2)

        # button
        Save_Data = Button(self.Project_Zone_Label,command=lambda:STUDENT_FORM_SUBMIT(), text="Save", image=self.save_ico, compound=LEFT)
        Save_Data.grid(row=6, column=6)
        Delete_Data = Button(self.Project_Zone_Label, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=6, column=7)
        Update_Data = Button(self.Project_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=6, column=8)

        # Gridview = LabelFrame(self.Project_Zone_Label, text="Data GridView: ")
        # Gridview.grid(row=1, column=7,rowspan=5,columnspan=3)
        # data_entry_space = Text(Gridview, borderwidth=5,height=20, width=65)
        # data_entry_space.grid(row=0, column=1)
        # data_entry_space.insert(0, "Name: ")
        temp = self.Project_Zone_Label
        testing(self.Project_Zone_Label)


if __name__ == '__main__':
    root = Tk()
    lms = Int_supervisor(root)
    lms.grid(row=0,column=0)
    mainloop()