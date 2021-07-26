from tkinter import *
from PIL import Image,ImageTk
import sqlite3
from tksheet import Sheet
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
    cmd.execute('''SELECT * from Project_Phase_Member''');
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
    sheet.grid(row = 0, column = 0,pady=30,ipadx=130)
    # data_collector()
#
#
def STUDENT_FORM_SUBMIT():

    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute("insert into Project_Phase_Member(Registration_NO,Project_Name,participation) values (?,?,?)",
                (Registration_entry.get(),Project_entry.get(),Participation_entry.get()))
    conn.commit()
    # print(Campus_entry.get())
    print("Data Submited")
    conn.close()
    testing(temp)
 # def func2():
 #    text2.delete(0.0,'end')
 #    text2.insert('insert', spb2.get())
class Project_phase_member(Frame):
    def __init__(self,windows):
        Frame.__init__(self)
        global temp
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/project for edit.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Project_Zone_Label = Label(self,borderwidth=0)
        self.Project_Zone_Label.grid(row=0, column=1, sticky='nsew', columnspan=10)
        Image_Label = Label(self.Project_Zone_Label, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=10)

        Data_frame = LabelFrame(self.Project_Zone_Label, text="Member's ", font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, pady=65, columnspan=3)
        global Registration_entry
        Student_Time_Label = Label(Data_frame, text="Registration No: ", font=('Helvetica', 12, 'bold'))
        Student_Time_Label.grid(row=0, column=0, pady=10)
        Registration_entry = ttk.Combobox(Data_frame, value=Registration_value(), width=38, font=('Helvetica', 12, 'bold'))
        Registration_entry.grid(row=0, column=1, pady=10, padx=30)
        global Project_entry
        Student_Time_Label = Label(Data_frame, text="Project Name: ", font=('Helvetica', 12, 'bold'))
        Student_Time_Label.grid(row=1, column=0, pady=10)
        Project_entry = Entry(Data_frame, borderwidth=2, width=40, font=('Helvetica', 12, 'bold'))
        Project_entry.grid(row=1, column=1, pady=10, padx=30)
        global Participation_entry
        Student_Time_Label = Label(Data_frame, text="Participation: ", font=('Helvetica', 12, 'bold'))
        Student_Time_Label.grid(row=2, column=0, pady=10)
        Participation_entry = Spinbox(Data_frame,width=39, values=[1,2,3,4,5,6], increment=1, font=('Helvetica', 12, 'bold'))
        Participation_entry.grid(row=2, column=1, pady=10, padx=30)

        Save_Data = Button(self.Project_Zone_Label,command=lambda : STUDENT_FORM_SUBMIT(), text="Save Record", image=self.save_ico, compound=LEFT)
        Save_Data.grid(row=2, column=0, padx=30)
        Delete_Data = Button(self.Project_Zone_Label, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=2, column=1, padx=30)
        Update_Data = Button(self.Project_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=2, column=2, padx=30)

        temp = self.Project_Zone_Label
        testing(self.Project_Zone_Label)
        # Gridview = Label(self.Project_Zone_Label, text="Data GridView: ")
        # Gridview.grid(row=1, column=6, columnspan=3)
        # data_entry_space = Entry(Gridview, borderwidth=10, width=100)
        # data_entry_space.grid(row=0, column=1)
        # data_entry_space.insert(0, "Name: ")



if __name__ == '__main__':
    root = Tk()
    lms = Project_phase_member(root)
    lms.grid(row=0,column=0)
    mainloop()