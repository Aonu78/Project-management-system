from tkinter import *
from PIL import Image,ImageTk
from tksheet import Sheet
import sqlite3

# root.wm_attributes('-fullscreen', 'true')

def data_collector():
    global data_list, i
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute('''SELECT * from Project_Category_Table''');
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
    cur.execute("insert into Project_Category_Table(Category_Name) values (?)",(Category_entry.get(),))
    conn.commit()
    # print(Department_entry.get())
    print("Data Submited")

    conn.close()
    testing(temp)


class Project_pro(Frame):
    def __init__(self,windows):
        global Category_entry,temp
        Frame.__init__(self)
        self.img_stu = ImageTk.PhotoImage(Image.open(r'Images/project for edit.png'))
        self.save_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-save-64.png"))
        self.delete_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-delete-bin-64.png"))
        self.update_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-database-export-64.png"))
        self.Project_Zone_Label = Label(self,borderwidth=0)
        self.Project_Zone_Label.grid(row=0, column=1, sticky='nsew', columnspan=10)
        Image_Label = Label(self.Project_Zone_Label, image=self.img_stu)
        Image_Label.grid(row=0, column=0, columnspan=10)

        Data_frame = LabelFrame(self.Project_Zone_Label, text="PROJECT CATEGORY ", font=('Helvetica', 16, 'bold'))
        Data_frame.grid(row=1, column=0, pady=14, columnspan=5)

        Category_Label = Label(Data_frame, text="Category: ", font=('Helvetica', 12, 'bold'))
        Category_Label.grid(row=0, column=0, pady=140)
        Category_entry = Entry(Data_frame, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
        Category_entry.grid(row=0, column=1, pady=10, padx=30)

        Save_Data = Button(self.Project_Zone_Label,command=lambda :STUDENT_FORM_SUBMIT(), text="Save Record", image=self.save_ico, compound=LEFT)
        Save_Data.grid(row=2, column=0, padx=10)
        Delete_Data = Button(self.Project_Zone_Label, text="Delete", image=self.delete_ico, compound=LEFT)
        Delete_Data.grid(row=2, column=1, padx=10)
        Update_Data = Button(self.Project_Zone_Label, text="Update", image=self.update_ico, compound=LEFT)
        Update_Data.grid(row=2, column=2, padx=10)
        temp = self.Project_Zone_Label
        testing(self.Project_Zone_Label)
        # Gridview = Label(self.Project_Zone_Label, text="Data GridView: ")
        # Gridview.grid(row=1, column=6, columnspan=3)
        # data_entry_space = Entry(Gridview, borderwidth=10, width=100)
        # data_entry_space.grid(row=0, column=1)
        # data_entry_space.insert(0, "Name: ")



if __name__ == '__main__':
    root = Tk()
    lms = Project_pro(root)
    lms.grid(row=0,column=0)
    mainloop()