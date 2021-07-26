from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tksheet import Sheet
import sqlite3
from tkcalendar import DateEntry

R_Value = []
C_Value = []


def Category_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT Category_Name from Project_Category_Table")
    for sdf in cmd:
        C_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return C_Value


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
    cmd.execute('''SELECT * from Student_Project_Tabel''');
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
    frame.grid(row=1, column=6, columnspan=3)
    sheet.grid(row = 0, column = 0, sticky = "nswe",pady=30,ipadx=110)
    # data_collector()
#
#
def STUDENT_FORM_SUBMIT():

    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute("insert into Student_Project_Tabel (Project,Category,Registration_No,"
                "Student_Name,Class_Name,Date_Created,Date_Modified,"
                " Confirmed) values (?,?,?,?,?,?,?,?)",(Student_Project_Entry.get(),
                                          Student_Category_Entry.get(),Student_Regis_No_Entry.get(),
                                          Student_Stu_Name_Entry.get(),Student_Class_Name_Entry.get(),
                                          Student_Date_Create_Entry.get(),Student_Date_Modi_Entry.get(),
                                          Student_Project_Comfirmed_Entry.get()),)
    conn.commit()
    # print(Department_entry.get())
    print("Data Submited")

    conn.close()
    testing(temp)



class Pro_Project(Frame):
    def __init__(self,windows):
        global temp
        Frame.__init__(self)
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/project for edit.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Student_Project_Zone = Label(self, borderwidth=0)
        self.Student_Project_Zone.grid(row=0, column=1, sticky='nsew', columnspan=10)
        Image_Label = Label(self.Student_Project_Zone, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=10)

        Data_frame = LabelFrame(self.Student_Project_Zone, text="PROJECT", font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, pady=14, columnspan=5)
        global Student_Project_Entry
        Student_Project_Label = Label(Data_frame, text="Project: ", font=('Helvetica', 12, 'bold'))
        Student_Project_Label.grid(row=0, column=0)
        Student_Project_Entry = Entry(Data_frame, borderwidth=2, width=37, font=('Helvetica', 12, 'bold'))
        Student_Project_Entry.grid(row=0, column=1, pady=5, padx=30)
        global Student_Category_Entry
        Student_Category_Label = Label(Data_frame, text="Category: ", font=('Helvetica', 12, 'bold'))
        Student_Category_Label.grid(row=1, column=0)
        Student_Category_Entry = ttk.Combobox(Data_frame, value=Category_value(), width=35, font=('Helvetica', 12, 'bold'))
        Student_Category_Entry.grid(row=1, column=1, pady=5, padx=30)
        global Student_Regis_No_Entry
        Student_Regis_No_Label = Label(Data_frame, text="Registration No: ", font=('Helvetica', 12, 'bold'))
        Student_Regis_No_Label.grid(row=2, column=0)
        Student_Regis_No_Entry = ttk.Combobox(Data_frame, value=Registration_value(), width=35, font=('Helvetica', 12, 'bold'))
        Student_Regis_No_Entry.grid(row=2, column=1, pady=5, padx=30)
        global Student_Stu_Name_Entry
        Student_Stu_Name_Label = Label(Data_frame, text="Student Name: ", font=('Helvetica', 12, 'bold'))
        Student_Stu_Name_Label.grid(row=3, column=0)
        Student_Stu_Name_Entry = Entry(Data_frame, borderwidth=2, width=37, font=('Helvetica', 12, 'bold'))
        Student_Stu_Name_Entry.grid(row=3, column=1, pady=5, padx=30)
        global Student_Class_Name_Entry
        Student_Class_Name_Label = Label(Data_frame, text="Class Name: ", font=('Helvetica', 12, 'bold'))
        Student_Class_Name_Label.grid(row=4, column=0)
        Student_Class_Name_Entry = Entry(Data_frame, borderwidth=2, width=37, font=('Helvetica', 12, 'bold'))
        Student_Class_Name_Entry.grid(row=4, column=1, pady=5, padx=30)
        global Student_Date_Create_Entry
        Student_Date_Create_Label = Label(Data_frame, text="Date Created: ", font=('Helvetica', 12, 'bold'))
        Student_Date_Create_Label.grid(row=5, column=0)
        Student_Date_Create_Entry = DateEntry(Data_frame, borderwidth=2, width=35, font=('Helvetica', 12, 'bold'))
        Student_Date_Create_Entry.grid(row=5, column=1, pady=5, padx=30)
        global Student_Date_Modi_Entry
        Student_Date_Modi_Label = Label(Data_frame, text="Date Modified: ", font=('Helvetica', 12, 'bold'))
        Student_Date_Modi_Label.grid(row=6, column=0)
        Student_Date_Modi_Entry = DateEntry(Data_frame, borderwidth=2, width=35, font=('Helvetica', 12, 'bold'))
        Student_Date_Modi_Entry.grid(row=6, column=1, pady=5, padx=30)
        global Student_Project_Comfirmed_Entry
        Student_Project_Comfirmed_Label = Label(Data_frame, text="Confirmed: ", font=('Helvetica', 12, 'bold'))
        Student_Project_Comfirmed_Label.grid(row=7, column=0)
        Student_Project_Comfirmed_Entry = DateEntry(Data_frame, borderwidth=2, width=35, font=('Helvetica', 12, 'bold'))
        Student_Project_Comfirmed_Entry.grid(row=7, column=1, pady=5, padx=30)

        Save_Data = Button(self.Student_Project_Zone,command=lambda : STUDENT_FORM_SUBMIT(), text="Save Record", image=self.save_ico, compound=LEFT)
        Save_Data.grid(row=2, column=0, padx=10)
        Delete_Data = Button(self.Student_Project_Zone, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=2, column=1, padx=10)
        Update_Data = Button(self.Student_Project_Zone, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=2, column=2, padx=10)

        temp = self.Student_Project_Zone
        testing(self.Student_Project_Zone)
        # Gridview = Label(self.Student_Project_Zone, text="Data GridView: ")
        # Gridview.grid(row=1, column=6, columnspan=3)
        # data_entry_space = Entry(Gridview, borderwidth=10, width=100)
        # data_entry_space.grid(row=0, column=1)
        # data_entry_space.insert(0, "Name: ")



if __name__ == '__main__':
    root = Tk()
    lms = Pro_Project(root)
    lms.grid(row=0,column=0)
    mainloop()