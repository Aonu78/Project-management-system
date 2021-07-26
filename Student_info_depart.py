from tkinter import *
from tksheet import Sheet
from PIL import Image, ImageTk
import sqlite3
global Department_entry

# root.wm_attributes('-fullscreen', 'true')

def data_collector():
    global data_list, i
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute('''SELECT * from Depart_table''');
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
    frame.grid(row=1, column=6, columnspan=6, sticky='nesw',rowspan=1)
    sheet.grid(row = 0, column = 0, sticky = "nswe",pady=30,padx=40,ipadx=40)
    # data_collector()
#
#
def STUDENT_FORM_SUBMIT():

    # data_collector()
    conn = sqlite3.connect('Whole_Database.db')
    # creating the cursur to send the data to the data base
    cur = conn.cursor()
    cur.execute("insert into Depart_table(name) values (?)",(Department_entry.get(),))
    conn.commit()
    print(Department_entry.get())
    print("Data Submited")

    conn.close()
    testing(temp)


class Stu_depart(Frame):
    def __init__(self,window):
        Frame.__init__(self)
        global Department_entry, temp
        # super().__init__(**kw)
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/student_zone1.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Cam_Student_Zone_Label = Label(self)
        self.Cam_Student_Zone_Label.grid(row=0, column=1, sticky='nsew',columnspan=10)
        Image_Label = Label(self.Cam_Student_Zone_Label, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=10)

        Data_frame = LabelFrame(self.Cam_Student_Zone_Label, text="DEPARTMENT", font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0,pady=14,columnspan=5)

        Student_Name_Label = Label(Data_frame, text="Department: ", font=('Helvetica', 12, 'bold'))
        Student_Name_Label.grid(row=0, column=0,pady=130)
        Department_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Department_entry.grid(row=0, column=1, pady=10,padx=30)
        temp = self.Cam_Student_Zone_Label
        Save_Data = Button(self.Cam_Student_Zone_Label, text="Save Record", image=self.save_ico, compound=LEFT,command=lambda: STUDENT_FORM_SUBMIT())
        Save_Data.bind("<Button-1>",testing(self.Cam_Student_Zone_Label))
        Save_Data.grid(row=2, column=0, padx=10)
        Delete_Data = Button(self.Cam_Student_Zone_Label, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=2, column=1,padx=10)
        Update_Data = Button(self.Cam_Student_Zone_Label, text="Update", image=self.update_ico,compound=LEFT)
        Update_Data.grid(row=2, column=2,padx=10)

        #=========For maintain space==========
        Label(self.Cam_Student_Zone_Label).grid()
if __name__ == "__main__":
    root = Tk()
    gui = Stu_depart(root)
    gui.grid(row=2, column=1, sticky='nsew')
    mainloop()
