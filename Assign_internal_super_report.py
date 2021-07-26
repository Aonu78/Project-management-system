from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tksheet import Sheet
import sqlite3

D_Value = []
P_Value = []
S_Value = []
T_Value = []
C_Value = []
# ws['bg']='#fb0'

from tksheet import Sheet
import sqlite3


# root.wm_attributes('-fullscreen', 'true')

def data_collector():
    global data_list, i
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute('''SELECT * from Internal_designation''');
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
    frame.grid(row=1, column=6, columnspan=3)
    sheet.grid(row=0, column=0, sticky="nswe")


def Department_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT name from Depart_table")
    for sdf in cmd:
        D_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return D_Value
def Class_Name_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT class_name from student_class")
    for sdf in cmd:
        C_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return C_Value
def Timing_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT Timing_Name from Timetable")
    for sdf in cmd:
        T_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return T_Value
def Program_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT Name from Program_table")
    for sdf in cmd:
        P_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return P_Value
def Session_value():
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"SELECT Session from Session_table")
    for sdf in cmd:
        S_Value.append(sdf)
        # print(sdf)
    conn.commit()
    conn.close()
    return S_Value



def data_getter():
    global data_list, i
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute('''select Registration_No,Student_Name,Roll_No,Internal_Name,Designation,
    E_Mail from Assign_Internal_Supervisor_Tabel''')
    data_list = []
    data_free = []
    lok = 65
    i = 1
    for student in cmd:
        for j in range(len(student)):
            data_list.append(student[j])
            print("........................................................")
            print(data_free)
            print("........................................................")
        data_free.append(data_list)
        data_list = []
        i = i + 1
    conn.close()
    return data_free


def sequence():
    if Department_Entry.get() != '' and Program_Entry.get() != '' and Session_Entry.get() != '' and Class_Name_Entry.get() != '' and Timing_Entry.get() != '':
        Get_Report_Clicked()
    else:
        print("Fill All the field")


def Get_Report_Clicked():
    if Department_Entry.get() != '' and Program_Entry.get() != '' and Session_Entry.get() != '' and Class_Name_Entry.get() != '' and Timing_Entry.get() != '':
        print("Work Done Ho gya")
        tx1 = Label(temp,text= 'Department Of', font=('Helvetica', 12, 'bold'))
        tx1.grid(row=3,column=2)
        tx2 = Label(temp,text= Department_Entry.get(), font=('Helvetica', 12, 'bold'))
        tx2.grid(row=3,column=3,pady=2)

        tx1 = Label(temp, text='Program', font=('Helvetica', 12, 'bold'))
        tx1.grid(row=4, column=0)
        tx2 = Label(temp, text=Program_Entry.get(), font=('Helvetica', 12, 'bold'))
        tx2.grid(row=4, column=1,pady=2)

        tx1 = Label(temp, text='Session', font=('Helvetica', 12, 'bold'))
        tx1.grid(row=4, column=4)
        tx2 = Label(temp, text=Session_Entry.get(), font=('Helvetica', 12, 'bold'))
        tx2.grid(row=4, column=5)

        tx1 = Label(temp, text='Class', font=('Helvetica', 12, 'bold'))
        tx1.grid(row=5, column=0)
        tx2 = Label(temp, text=Class_Name_Entry.get(), font=('Helvetica', 12, 'bold'))
        tx2.grid(row=5, column=1)

        tx1 = Label(temp, text='Timing', font=('Helvetica', 12, 'bold'))
        tx1.grid(row=5, column=4)
        tx2 = Label(temp, text=Timing_Entry.get(), font=('Helvetica', 12, 'bold'))
        tx2.grid(row=5, column=5)

        tv = ttk.Treeview()
        tv['columns'] = ('Registration No', 'Student Name', 'Roll No', 'Internal Supervisor Name', 'Designation','E_Mail')
        tv.column('#0', width=0, stretch=NO)
        tv.column('Registration No', anchor=CENTER, width=80)
        tv.column('Student Name', anchor=CENTER, width=80)
        tv.column('Roll No', anchor=CENTER, width=80)
        tv.column('Internal Supervisor Name', anchor=CENTER, width=80)
        tv.column('Designation', anchor=CENTER, width=80)
        tv.column('E_Mail', anchor=CENTER, width=80)

        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('Registration No', text='Registration No', anchor=CENTER)
        tv.heading('Student Name', text='Student Name', anchor=CENTER)
        tv.heading('Roll No', text='Roll No', anchor=CENTER)
        tv.heading('Internal Supervisor Name', text='Internal Supervisor Name', anchor=CENTER)
        tv.heading('Designation', text='Designation', anchor=CENTER)
        tv.heading('E_Mail', text='E_Mail', anchor=CENTER)
        i = 0
        temper = []
        for setter in data_getter():
            for j in setter:
                temper.append(j)
            tv.insert(parent='', index=i, values=(temper))
            print(temper)
            temper = []
            i = i + 1
        tv.grid(row=6,column=0,columnspan=6)
    else:
        print('pagl hy kya')


class Supervisor_Report(Frame):
    def __init__(self, window):
        Frame.__init__(self)
        global temp
        global Department_Entry
        self.l_logo = ImageTk.PhotoImage(Image.open(r'Images/uos logo2.png'))
        Department_Label = Label(self,text='Department', font=('Helvetica', 12, 'bold'))
        Department_Label.grid(row=0,column=0)
        Department_Entry = ttk.Combobox(self, values=Department_value(), font=('Helvetica', 12, 'bold'))
        Department_Entry.grid(row=0,column=1,pady=20)
        global Class_Name_Entry
        Class_Name_Label = Label(self, text='Class Name', font=('Helvetica', 12, 'bold'))
        Class_Name_Label.grid(row=0, column=2)
        Class_Name_Entry = ttk.Combobox(self, values=Class_Name_value(), font=('Helvetica', 12, 'bold'))
        Class_Name_Entry.grid(row=0,column=3)
        global Timing_Entry
        Timing_Label = Label(self, text='Timing', font=('Helvetica', 12, 'bold'))
        Timing_Label.grid(row=0, column=4)
        Timing_Entry = ttk.Combobox(self, values=Timing_value(), font=('Helvetica', 12, 'bold'))
        Timing_Entry.grid(row=0,column=5,padx=20)
        global Program_Entry
        Program_Label = Label(self, text='Program', font=('Helvetica', 12, 'bold'))
        Program_Label.grid(row=1, column=0)
        Program_Entry = ttk.Combobox(self, values=Program_value(), font=('Helvetica', 12, 'bold'))
        Program_Entry.grid(row=1,column=1)
        global Session_Entry
        Session_Label = Label(self, text='Session', font=('Helvetica', 12, 'bold'))
        Session_Label.grid(row=1, column=2)
        Session_Entry = ttk.Combobox(self, values=Session_value(), font=('Helvetica', 12, 'bold'))
        Session_Entry.grid(row=1,column=3)

        Get_Report = Button(self,text='Get Report',command=lambda : sequence(), font=('Helvetica', 18, 'bold'))
        Get_Report.grid(row=1,column=4,padx=30,columnspan=2)
        temp = self
        uos_logo = Label(self,image=self.l_logo)
        uos_logo.grid(row=2,column=0)
        dis = Label(self,text='UNIVERSITY OF SARGODHA',font=('Castellar', 40, 'bold'))
        dis.grid(row=2,column=1,columnspan=4)

if __name__ == "__main__":
    root = Tk()
    gui = Supervisor_Report(root)
    gui.grid(row=2, column=1, sticky='nsew')
    mainloop()
