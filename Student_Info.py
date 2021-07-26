from tksheet import Sheet
import sqlite3
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

# global Student_entry
# global Father_entry
# global Registration_entry
# global DOB_entry
# global Mobile_No_entry
# global Student_cnic_entry
# global Gridview
# #
# conn = sqlite3.connect('Whole_Database.db')
# creating the cursur to send the data to the data base
# cmd = conn.cursor()
# cmd.execute('''SELECT * from student_info''');
# data_list =[]
# data_free = []
# lok = 65
# i = 1  # row value inside the loop


def SDF():

    print(Student_entry.get(), Father_entry.get(),Registration_entry.get(),DOB_entry.get(), Mobile_No_entry.get(),Student_cnic_entry.get())
    print(data_list)



def data_collector():
    global data_list, i
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute('''SELECT * from student_info''');
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
    frame.grid(row=1, column=6,rowspan=1,columnspan=3)
    sheet.grid(row=0, column=0,ipadx=60, sticky="nswe")
#
def STUDENT_FORM_SUBMIT():
    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    r_set = cur.execute('insert into student_info(student_name,student_father_name,registration_no,date_of_birth,mobile_no,'
                'c_n_i_c) VALUES (?,?,?,?,?,?)',(Student_entry.get(), Father_entry.get(),Registration_entry.get(),
                                                 DOB_entry.get(), Mobile_No_entry.get(),Student_cnic_entry.get()))
    conn.commit()
    # print(Department_entry.get())
    print("Data Submited")

    conn.close()
    testing(temp)


class StudentInfo(Frame):
    def __init__(self,window):
        global Student_entry,Gridview
        global Father_entry, Registration_entry, DOB_entry
        global Mobile_No_entry, Student_cnic_entry,temp
        # creating the database
        # conn = sqlite3.connect('Whole_Database.db')
        # creating the cursur to send the data to the data base
        # cur = conn.cursor()
        Frame.__init__(self)
        # super().__init__(**kw)
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/student_zone1.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Student_Zone_Label = Label(self)
        self.Student_Zone_Label.grid(row=2, column=1, sticky='nsew')
        Image_Label = Label(self.Student_Zone_Label, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=10)
        Data_frame = LabelFrame(self.Student_Zone_Label, text="Student Information", font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0,columnspan=3)

        Student_Name_Label = Label(Data_frame, text="Student Name: ", font=('Helvetica', 12, 'bold'))
        Student_Name_Label.grid(row=0, column=0)
        Student_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Student_entry.grid(row=0, column=1, pady=10)
        # Student_entry.insert(0, "Student Name: ")

        Father_Name_Label = Label(Data_frame, text="Father Name: ", font=('Helvetica', 12, 'bold'))
        Father_Name_Label.grid(row=1, column=0)
        Father_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Father_entry.grid(row=1, column=1, pady=10)
        # Father_entry.insert(0, "Father Name: ")

        Registration_No_Label = Label(Data_frame, text="Registration No: ", font=('Helvetica', 12, 'bold'))
        Registration_No_Label.grid(row=2, column=0)
        Registration_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Registration_entry.grid(row=2, column=1, pady=10)
        # Registration_entry.insert(0, "Reg_No: ")

        Date_Of_Birth_Label = Label(Data_frame, text="Date_Of_Birth: ", font=('Helvetica', 12, 'bold'))
        Date_Of_Birth_Label.grid(row=3, column=0)
        DOB_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        DOB_entry.grid(row=3, column=1, pady=10)
        # DOB_entry.insert(0, "D_O_B: ")

        Mobile_No_Label = Label(Data_frame, text="Mobile_No: ", font=('Helvetica', 12, 'bold'))
        Mobile_No_Label.grid(row=4, column=0)
        Mobile_No_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Mobile_No_entry.grid(row=4, column=1, pady=10)


        CNIC_Label = Label(Data_frame, text="C.N.I.C: ", font=('Helvetica', 12, 'bold'))
        CNIC_Label.grid(row=5, column=0)
        Student_cnic_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Student_cnic_entry.grid(row=5, column=1, pady=10)

        temp = self.Student_Zone_Label
        # data_collector()
        testing(self.Student_Zone_Label)


############+=====================
        Save_Data = Button(self.Student_Zone_Label,command=lambda: STUDENT_FORM_SUBMIT(), text="Save Record",
                           image=self.save_ico, compound=LEFT)
        Save_Data.bind("<Button-1>",testing(self.Student_Zone_Label))
        Save_Data.grid(row=2, column=0, padx=10)
        Delete_Data = Button(self.Student_Zone_Label,command=lambda : SDF(), text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=2, column=1, padx=10)
        Update_Data = Button(self.Student_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=2, column=2, padx=10)
        # conn.commit()
        # conn.close()
if __name__ == "__main__":
    root = Tk()
    gui = StudentInfo(root)
    gui.grid(row=2, column=1, sticky='nsew')
    mainloop()

