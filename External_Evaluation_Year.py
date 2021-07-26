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
    cmd.execute('''SELECT * from External_Evaluation_Year_Table''');
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
    cur.execute("insert into External_Evaluation_Year_Table (Evaluation_Year,Document_Submission,"
                "Thesis_Submission) values (?,?,?)",(Evaluation_Year_Entry.get(),Documentation_entry.get(),Thesis_entry.get()),)
    conn.commit()
    # print(Department_entry.get())
    print("Data Submited")

    conn.close()
    testing(temp)


class Evaluation_Year(Frame):
    def __init__(self,window):
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
        Data_frame = LabelFrame(self.Student_Zone_Label, text="Evaluation Year Information", font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0,columnspan=3,ipady=30)
        global Evaluation_Year_Entry
        Evaluation_Year_Label = Label(Data_frame, text="Evaluation Year:", font=('Helvetica', 12, 'bold'))
        Evaluation_Year_Label.grid(row=0, column=0)
        Evaluation_Year_Entry = Entry(Data_frame, borderwidth=3, width=30, font=('Helvetica', 12, 'bold'))
        Evaluation_Year_Entry.grid(row=0, column=1, pady=20)
        global Documentation_entry
        Documentation_Label = Label(Data_frame, text="Documentation Submission:", font=('Helvetica', 12, 'bold'))
        Documentation_Label.grid(row=1, column=0)
        Documentation_entry = Entry(Data_frame, borderwidth=3, width=30, font=('Helvetica', 12, 'bold'))
        Documentation_entry.grid(row=1, column=1, pady=20)
        global Thesis_entry
        Thesis_Label = Label(Data_frame, text="Thesis Submission:", font=('Helvetica', 12, 'bold'))
        Thesis_Label.grid(row=2, column=0)
        Thesis_entry = Entry(Data_frame, borderwidth=3, width=30, font=('Helvetica', 12, 'bold'))
        Thesis_entry.grid(row=2, column=1, pady=20)

        temp = self.Student_Zone_Label
        testing(self.Student_Zone_Label)

############+=====================
        Save_Data = Button(self.Student_Zone_Label,command=lambda: STUDENT_FORM_SUBMIT(), text="Save Record",
                           image=self.save_ico, compound=LEFT)
        Save_Data.bind("<Button-1>",testing(self.Student_Zone_Label))
        Save_Data.grid(row=2, column=0, padx=10)
        Delete_Data = Button(self.Student_Zone_Label, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=2, column=1, padx=10)
        Update_Data = Button(self.Student_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=2, column=2, padx=10)
        # conn.commit()
        # conn.close()
if __name__ == "__main__":
    root = Tk()
    gui = Evaluation_Year(root)
    gui.grid(row=2, column=1, sticky='nsew')
    mainloop()

