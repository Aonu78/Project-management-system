from tksheet import Sheet
import sqlite3
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from tksheet import Sheet
import sqlite3


# root.wm_attributes('-fullscreen', 'true')

def data_collector():
    global data_list, i
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute('''SELECT * from External_Evaluation_Class_Table''');
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
    cur.execute("insert into External_Evaluation_Class_Table (Evaluation_Year,Department,Program,"
                "Class,Session,Timing,Total_Student,Total_Evaluation) values (?,?,?,?,"
                "?,?,?,?)",(Evaluation_Class_Entry.get(),Department_entry.get(),Program_entry.get(),
                            Class_entry.get(),Session_entry.get(),Timing_entry.get(),Total_Student_entry.get(),
                            Total_Evaluation_entry.get()),)
    conn.commit()
    # print(Department_entry.get())
    print("Data Submited")

    conn.close()
    testing(temp)


class Supervisor_Classes_Info(Frame):
    def __init__(self, window):
        Frame.__init__(self)
        global temp
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/evaluation.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Student_Zone_Label = Label(self)
        self.Student_Zone_Label.grid(row=2, column=1, sticky='nsew')
        Image_Label = Label(self.Student_Zone_Label, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=10)
        Data_frame = LabelFrame(self.Student_Zone_Label, text="Evaluation Classes Information",
                                font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, columnspan=3, rowspan=2)
        global Evaluation_Class_Entry
        Evaluation_Class_Label = Label(Data_frame, text="Evaluation Class: ", font=('Helvetica', 12, 'bold'))
        Evaluation_Class_Label.grid(row=0, column=0)
        Evaluation_Class_Entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Evaluation_Class_Entry.grid(row=0, column=1, pady=10)
        global Department_entry
        Department_Label = Label(Data_frame, text="Department: ", font=('Helvetica', 12, 'bold'))
        Department_Label.grid(row=1, column=0)
        Department_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Department_entry.grid(row=1, column=1, pady=10)
        global Program_entry
        Program_Label = Label(Data_frame, text="Program: ", font=('Helvetica', 12, 'bold'))
        Program_Label.grid(row=2, column=0)
        Program_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Program_entry.grid(row=2, column=1, pady=10)
        global Class_entry
        Class_Label = Label(Data_frame, text="Class: ", font=('Helvetica', 12, 'bold'))
        Class_Label.grid(row=3, column=0)
        Class_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Class_entry.grid(row=3, column=1, pady=10)
        global Session_entry
        Session_Label = Label(Data_frame, text="Session: ", font=('Helvetica', 12, 'bold'))
        Session_Label.grid(row=4, column=0)
        Session_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Session_entry.grid(row=4, column=1, pady=10)
        global Timing_entry
        Timing_Label = Label(Data_frame, text="Timing", font=('Helvetica', 12, 'bold'))
        Timing_Label.grid(row=5, column=0)
        Timing_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Timing_entry.grid(row=5, column=1, pady=10)
        global Total_Student_entry
        Total_Student_Label = Label(Data_frame, text="Total Student", font=('Helvetica', 12, 'bold'))
        Total_Student_Label.grid(row=6, column=0)
        Total_Student_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Total_Student_entry.grid(row=6, column=1, pady=10)
        global Total_Evaluation_entry
        Total_Evaluation_Label = Label(Data_frame, text="Total Evaluation", font=('Helvetica', 12, 'bold'))
        Total_Evaluation_Label.grid(row=7, column=0)
        Total_Evaluation_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Total_Evaluation_entry.grid(row=7, column=1, pady=10)

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
        # conn.commit()
        # conn.close()


if __name__ == "__main__":
    root = Tk()
    gui = Supervisor_Classes_Info(root)
    gui.grid(row=2, column=1, sticky='nsew')
    mainloop()
