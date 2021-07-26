from tkinter import *
from PIL import Image,ImageTk
from tksheet import Sheet
import sqlite3
from tkcalendar import DateEntry
from tkinter import ttk


def data_collector():
    global data_list, i
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute('''SELECT * from Session_table''');
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
    frame.grid(row=1, column=3,rowspan=1,columnspan=3)
    sheet.grid(row=0, column=0,ipadx=60, sticky="nswe")

#
#
def STUDENT_FORM_SUBMIT():

    #
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute("insert into Session_table(Session,Start_year, End_year) values (?,?,?)",(Student_entry1.get()+"-"+Student_entry2.get(), Student_Start_Year_entry.get(), Student_End_Year_entry.get()))
    conn.commit()
    print(Student_entry1.get()+"-"+Student_entry2.get())
    print("Data Submited")
    conn.close()
    testing(temp)


class Stu_info_ses(Frame):
    def __init__(self,windows):
        Frame.__init__(self)
        global Student_Start_Year_entry, Student_entry, Student_End_Year_entry,Student_entry1,Student_entry2,temp
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/student_zone1.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Ses_Student_Zone_Label = Label(self,bg="#674856",borderwidth=0)
        self.Ses_Student_Zone_Label.grid(row=0, column=1, sticky='nsew', columnspan=10)
        Image_Label = Label(self.Ses_Student_Zone_Label, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=10)

        Data_frame = LabelFrame(self.Ses_Student_Zone_Label, text="SESSION", font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, pady=64, columnspan=3)

        Student_Session_Label1 = Label(Data_frame, text="Session: ", font=('Helvetica', 12, 'bold'))
        Student_Session_Label1.grid(row=0, column=0)
        year = []
        for i in range(1950, 2100, 1):
            year.append(i)
        Student_entry1 = ttk.Combobox(Data_frame,values=year, font=('Helvetica', 12, 'bold'))
        Student_entry1.grid(row=0, column=1, pady=10)
        Student_Session_Label2 = Label(Data_frame, text="To: ", font=('Helvetica', 12, 'bold'))
        Student_Session_Label2.grid(row=0, column=2)
        Student_entry2 = ttk.Combobox(Data_frame,values=year, font=('Helvetica', 12, 'bold'))
        Student_entry2.grid(row=0, column=3, pady=10,)
        Student_entry = (Student_entry1.get() +"-"+ Student_entry1.get())
        Student_Start_Year_Label = Label(Data_frame, text="Start Year: ", font=('Helvetica', 12, 'bold'))
        Student_Start_Year_Label.grid(row=1, column=0)
        Student_Start_Year_entry = DateEntry(Data_frame, borderwidth=3, width=30, font=('Helvetica', 12, 'bold'))
        Student_Start_Year_entry.grid(row=1, column=1, pady=10, padx=25, columnspan=3)

        Student_End_Year_Label = Label(Data_frame, text="End Year: ", font=('Helvetica', 12, 'bold'))
        Student_End_Year_Label.grid(row=2, column=0)
        Student_End_Year_entry = DateEntry(Data_frame, borderwidth=3, width=30, font=('Helvetica', 12, 'bold'))
        Student_End_Year_entry.grid(row=2, column=1, pady=10, padx=25, columnspan=3)

        Save_Data = Button(self.Ses_Student_Zone_Label, text="Save Record", image=self.save_ico, compound=LEFT,command=lambda :STUDENT_FORM_SUBMIT())
        Save_Data.bind("<Button-1>", testing(self.Ses_Student_Zone_Label))
        Save_Data.grid(row=2, column=0, padx=10)
        Delete_Data = Button(self.Ses_Student_Zone_Label, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=2, column=1, padx=10)
        Update_Data = Button(self.Ses_Student_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=2, column=2, padx=10)


        temp = self.Ses_Student_Zone_Label
        testing(self.Ses_Student_Zone_Label)
        # Gridview = Label(self.Ses_Student_Zone_Label, text="Data GridView: ")
        # Gridview.grid(row=1, column=6, columnspan=3)
        # data_entry_space = Entry(Gridview, borderwidth=10, width=100)
        # data_entry_space.grid(row=0, column=1)
        # data_entry_space.insert(0, "Name: ")



if __name__ == '__main__':
    root = Tk()
    lms = Stu_info_ses(root)
    lms.grid(row=0,column=0)
    mainloop()