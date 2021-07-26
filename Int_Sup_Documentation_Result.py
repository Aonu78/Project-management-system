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
    cmd.execute('''SELECT * from Internal_Supervisor_Docum_Result_Tabel''');
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
    frame.grid(row=1, column=6, columnspan=4)
    sheet.grid(row=0, column=0, sticky="nswe", ipadx=60)
    # data_collector()


#
#
def STUDENT_FORM_SUBMIT():
    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute('insert into Internal_Supervisor_Docum_Result_Tabel (Department_Name,Program,'
                'Evaluation_Year,Session,Timing,Registration_No,Phase,Student_Name,'
                'Enrollment,Internal_Name,Project_Name,Marks,GPA,Grade) values (?,?,?,?,?,?,?,?,?,'
                '?,?,?,?,?)', (Registration_Entry.get(), Program_entry.get(), Evaluation_Year_entry.get(),
                                     Session_entry.get(), Timing_entry.get(), Department_entry.get(), Phase_entry.get(),
                                     Student_Name_Entry.get(),Enrollment_entry.get(),Internal_Name_entry.get(),
                                     Project_Name_entry.get(),Marks_entry.get(),GPA_entry.get(),Grade_entry.get()), )
    conn.commit()
    # print(Department_entry.get())
    print("Data Submited")

    conn.close()
    testing(temp)


class Result_Info(Frame):
    def __init__(self, window):
        Frame.__init__(self)
        global temp
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/result_zone.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Student_Zone_Label = Label(self)
        self.Student_Zone_Label.grid(row=2, column=1, sticky='nsew')
        Image_Label = Label(self.Student_Zone_Label, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=10)
        Data_frame = LabelFrame(self.Student_Zone_Label, text="Evaluation Classes Record",
                                font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, columnspan=3, rowspan=2, ipady=20)
        global Registration_Entry
        Registration_Label = Label(Data_frame, text="Department", font=('Helvetica', 12, 'bold'))
        Registration_Label.grid(row=0, column=0)
        Registration_Entry = Entry(Data_frame, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Registration_Entry.grid(row=0, column=1, pady=10)
        global Program_entry
        Program_Label = Label(Data_frame, text="Program", font=('Helvetica', 12, 'bold'))
        Program_Label.grid(row=1, column=0)
        Program_entry = Entry(Data_frame, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Program_entry.grid(row=1, column=1, pady=10)
        global Evaluation_Year_entry
        Evaluation_Year_Label = Label(Data_frame, text="Year Evaluation Year", font=('Helvetica', 10, 'bold'))
        Evaluation_Year_Label.grid(row=2, column=0)
        Evaluation_Year_entry = Entry(Data_frame, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Evaluation_Year_entry.grid(row=2, column=1, pady=10)
        global Session_entry
        Session_Label = Label(Data_frame, text="Session", font=('Helvetica', 12, 'bold'))
        Session_Label.grid(row=3, column=0)
        Session_entry = Entry(Data_frame, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Session_entry.grid(row=3, column=1, pady=10)
        global Timing_entry
        Timing_Label = Label(Data_frame, text="Timing", font=('Helvetica', 12, 'bold'))
        Timing_Label.grid(row=4, column=0)
        Timing_entry = Entry(Data_frame, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Timing_entry.grid(row=4, column=1, pady=10)
        global Department_entry
        Department_Label = Label(Data_frame, text="Registration No", font=('Helvetica', 12, 'bold'))
        Department_Label.grid(row=5, column=0)
        Department_entry = Entry(Data_frame, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Department_entry.grid(row=5, column=1, pady=10)
        global Phase_entry
        Phase_Label = Label(Data_frame, text="Phases", font=('Helvetica', 12, 'bold'))
        Phase_Label.grid(row=6, column=0)
        Phase_entry = Entry(Data_frame, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Phase_entry.grid(row=6, column=1, pady=10)
        # frame 2

        Data_frame1 = LabelFrame(self.Student_Zone_Label, text="Internal Supervisor Result",
                                 font=('Helvetica', 16, 'bold'))
        Data_frame1.grid(row=1, column=3, columnspan=3, rowspan=2, ipady=20)
        global Student_Name_Entry
        Student_Name_Label = Label(Data_frame1, text="Student Name", font=('Helvetica', 12, 'bold'))
        Student_Name_Label.grid(row=0, column=0)
        Student_Name_Entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Student_Name_Entry.grid(row=0, column=1, pady=10)
        global Enrollment_entry
        Enrollment_Label = Label(Data_frame1, text="Enrollment", font=('Helvetica', 12, 'bold'))
        Enrollment_Label.grid(row=1, column=0)
        Enrollment_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Enrollment_entry.grid(row=1, column=1, pady=10)
        global Internal_Name_entry
        Internal_Name_Label = Label(Data_frame1, text="Internal Name", font=('Helvetica', 12, 'bold'))
        Internal_Name_Label.grid(row=2, column=0)
        Internal_Name_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Internal_Name_entry.grid(row=2, column=1, pady=10)
        global Project_Name_entry
        Project_Name_Label = Label(Data_frame1, text="Project Name", font=('Helvetica', 12, 'bold'))
        Project_Name_Label.grid(row=3, column=0)
        Project_Name_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Project_Name_entry.grid(row=3, column=1, pady=10)
        global Marks_entry
        Marks_Label = Label(Data_frame1, text="Marks", font=('Helvetica', 12, 'bold'))
        Marks_Label.grid(row=4, column=0)
        Marks_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Marks_entry.grid(row=4, column=1, pady=10)
        global GPA_entry
        GPA_Label = Label(Data_frame1, text="GPA", font=('Helvetica', 12, 'bold'))
        GPA_Label.grid(row=5, column=0)
        GPA_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        GPA_entry.grid(row=5, column=1, pady=10)
        global Grade_entry
        Grade_Label = Label(Data_frame1, text="Grade", font=('Helvetica', 12, 'bold'))
        Grade_Label.grid(row=6, column=0)
        Grade_entry = Entry(Data_frame1, borderwidth=3, width=20, font=('Helvetica', 12, 'bold'))
        Grade_entry.grid(row=6, column=1, pady=10)

        temp = self.Student_Zone_Label
        testing(self.Student_Zone_Label)
        ############+=====================
        Save_Data = Button(self.Student_Zone_Label, command=lambda: STUDENT_FORM_SUBMIT(), text="Save Record",
                           image=self.save_ico, compound=LEFT)
        Save_Data.bind("<Button-1>", testing(self.Student_Zone_Label))
        Save_Data.grid(row=2, column=6, padx=10)
        Delete_Data = Button(self.Student_Zone_Label, text="Delete", image=self.delete_ico,
                             compound=LEFT)
        Delete_Data.grid(row=2, column=7, padx=10)
        Update_Data = Button(self.Student_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=2, column=8, padx=10)


if __name__ == "__main__":
    root = Tk()
    gui = Result_Info(root)
    gui.grid(row=2, column=1, sticky='nsew')
    mainloop()
