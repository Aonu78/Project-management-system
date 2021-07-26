from tkinter import *
from PIL import ImageTk,Image
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
    cmd.execute('''SELECT * from Student_Proposal_Tabel''');
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
    frame.grid(row=2, column=6, columnspan=3,rowspan=3)
    sheet.grid(row = 0, column = 0, sticky = "nswe",pady=30,ipadx=110)
    # data_collector()
#
#
def STUDENT_FORM_SUBMIT():

    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute("insert into Student_Proposal_Tabel (Registration_No,Student_Name,"
                "Project_Name,Introduction,Problem_Statement,Mathdology,Tools,Technique) values (?,?,?,?,?,?,?,?)",
                (Student_Regis_entry.get(),
                                          Student_Name_entry.get(),Student_Project_entry.get(),
                                          Project_Introduction_entry.get(),Project_Problem_sate_entry.get(),
                                          Project_Mathdology_entry.get(),Project_Tools_entry.get(),
                                          Project_Technique_entry.get()),)
    conn.commit()
    # print(Department_entry.get())
    print("Data Submited")

    conn.close()
    testing(temp)


class Project_Proposal(Frame):
    def __init__(self,window):
        global temp
        Frame.__init__(self)
        self.img = ImageTk.PhotoImage(Image.open(r'Images/project for edit.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Proposal_Label=Label(self,borderwidth=0)
        self.Proposal_Label.grid(row=0,column=0)
        self.Image_Label = Label(self.Proposal_Label,image=self.img)
        self.Image_Label.grid(row=0,column=0,sticky="nsew",columnspan=10)
        Data_frame = LabelFrame(self.Proposal_Label, text="PROPOSAL", font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, columnspan=5,rowspan=4)
        global Student_Regis_entry
        Student_Regis_Label = Label(Data_frame, text="Registration No: ", font=('Helvetica', 12, 'bold'))
        Student_Regis_Label.grid(row=0, column=0)
        Student_Regis_entry = ttk.Combobox(Data_frame, value=Registration_value(), width=18, font=('Helvetica', 12, 'bold'))
        Student_Regis_entry.grid(row=0, column=1)
        global Student_Name_entry
        Student_Name_Label = Label(Data_frame, text="Student Name: ", font=('Helvetica', 12, 'bold'))
        Student_Name_Label.grid(row=1, column=0)
        Student_Name_entry = Entry(Data_frame, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Student_Name_entry.grid(row=1, column=1)
        global Student_Project_entry
        Student_Project_Name_Label = Label(Data_frame, text="Project Name: ", font=('Helvetica', 12, 'bold'))
        Student_Project_Name_Label.grid(row=2, column=0)
        Student_Project_entry = Entry(Data_frame, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Student_Project_entry.grid(row=2, column=1,pady=5)
        global Project_Introduction_entry
        Project_Introduction_Label = Label(Data_frame, text="Introduction: ", font=('Helvetica', 12, 'bold'))
        Project_Introduction_Label.grid(row=3, column=0)
        Project_Introduction_entry = Entry(Data_frame, borderwidth=3, font=('Helvetica', 12, 'bold'))
        Project_Introduction_entry.grid(row=3, column=1,ipady=15)
        global Project_Problem_sate_entry
        Project_Problem_state_Label = Label(Data_frame, text="Problum Statement: ", font=('Helvetica', 12, 'bold'))
        Project_Problem_state_Label.grid(row=4, column=0)
        Project_Problem_sate_entry = Entry(Data_frame, borderwidth=3, font=('Helvetica', 12, 'bold'))
        Project_Problem_sate_entry.grid(row=4, column=1,ipady=15)
        global Project_Mathdology_entry
        Project_Mathdology_Label = Label(Data_frame, text="Mathdology: ", font=('Helvetica', 12, 'bold'))
        Project_Mathdology_Label.grid(row=5, column=0)
        Project_Mathdology_entry = Entry(Data_frame, borderwidth=3, font=('Helvetica', 12, 'bold'))
        Project_Mathdology_entry.grid(row=5, column=1,ipady=15)
        global Project_Tools_entry
        Project_Tools_Label = Label(Data_frame, text="Tools: ", font=('Helvetica', 12, 'bold'))
        Project_Tools_Label.grid(row=0, column=2)
        Project_Tools_entry = Entry(Data_frame, borderwidth=3, font=('Helvetica', 12, 'bold'))
        Project_Tools_entry.grid(row=0, column=3,pady=5)
        global Project_Technique_entry
        Project_Technique_Label = Label(Data_frame, text="Technique: ", font=('Helvetica', 12, 'bold'))
        Project_Technique_Label.grid(row=1, column=2)
        Project_Technique_entry = Entry(Data_frame, borderwidth=3, width=15, font=('Helvetica', 12, 'bold'))
        Project_Technique_entry.grid(row=1, column=3,pady=5)
        temp = self.Proposal_Label
        testing(self.Proposal_Label)
        # Grid_frame = LabelFrame(self.Proposal_Label, text="grid", font=('Helvetica', 16, 'bold'))
        # Grid_frame.grid(row=2, column=6, columnspan=3,rowspan=3)
        # data_entry_space = Entry(Grid_frame, borderwidth=10, width=40)
        # data_entry_space.grid(row=0, column=1)

        Save_Data = Button(Data_frame,command=lambda:STUDENT_FORM_SUBMIT(), text="Save Record", image=self.save_ico, compound=LEFT)
        Save_Data.grid(row=3, column=3,sticky='e')
        Delete_Data = Button(Data_frame, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=4, column=3,sticky='e')
        Update_Data = Button(Data_frame, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=5, column=3,sticky='e')

if __name__=="__main__":
    root = Tk()
    lms = Project_Proposal(root)
    lms.grid(row=0, column=0)
    mainloop()