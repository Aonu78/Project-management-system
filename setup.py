from tkinter import *
from PIL import ImageTk, Image
import Student_info_campus
import Student_info_depart
import Student_info_session
import Student_Info_Class
import Student_Info_Enroll
import Student_info_time
import Student_Info_Program
import Project_category_file
import Project_pro_file
import Project_proposal
import Project_phase
import Project_phase_member
import Internal_designation
import Internal_supervisor
import Assign_internal_supervisor
import External_File
import Student_Info
import External_Evaluation_Year
import External_Evaluation_Classes
import Int_Sup_Documentation_Result
import Ext_Sup_Viva_Result
import Assign_internal_super_report
from PyQt5 import QtCore, QtGui, QtWidgets

root = Tk()
root.wm_attributes('-fullscreen', 'true')
root.configure(background='#221f28')
global ima,ima2
global upper_button_frame
# ===============Images================#
ima = ImageTk.PhotoImage(Image.open('Images/new1.png'))
ima2 = ImageTk.PhotoImage(Image.open('Images/new2.png'))
dog = ImageTk.PhotoImage(Image.open(r'Images/book1.png'))
im3 = ImageTk.PhotoImage(Image.open('Images/new3.png'))
foto = ImageTk.PhotoImage(Image.open(r"Images/icons8-user-40.png"))
home_image_icon = ImageTk.PhotoImage(Image.open(r"Images/icons8-home-40.png"))
student_image_icon = ImageTk.PhotoImage(Image.open(r"Images/icons8-man-student-40.png"))

project_image_icon = ImageTk.PhotoImage(Image.open(r"Images/icons8-p-40.png"))

internal_image_icon = ImageTk.PhotoImage(Image.open(r"Images/icons8-teacher-40.png"))
assign_internal_imsge_icon = ImageTk.PhotoImage(
    Image.open(r"Images/businessapplication_accept_ok_male_man_you_negocio_2311 (1).ico"))
external_image_icon = ImageTk.PhotoImage(Image.open(r"Images/icons8-student-male-40.png"))
results_image_icon = ImageTk.PhotoImage(Image.open(r"Images/icons8-combo-chart-40.png"))
report_image_icon = ImageTk.PhotoImage(Image.open(r"Images/icons8-report-card-40.png"))
exit_image_icon = ImageTk.PhotoImage(Image.open(r"Images/icons8-shutdown-40.png"))

student_zone = ImageTk.PhotoImage(Image.open(r"Images/student_zone.png"))
project_zone = ImageTk.PhotoImage(Image.open(r"Images/project_zone.png"))
internal_zone = ImageTk.PhotoImage(Image.open(r"Images/internal_zone.png"))
assign_internal_zone = ImageTk.PhotoImage(Image.open(r"Images/assign_internal_zone.png"))
external_zone = ImageTk.PhotoImage(Image.open(r"Images/external_zone.png"))
results_zone = ImageTk.PhotoImage(Image.open(r"Images/result_zone.png"))
report_zone = ImageTk.PhotoImage(Image.open(r"Images/report_zone.png"))

stu_info_student_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-student-male-40 (1).png"))
stu_info_campus_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-university-campus-40.png"))
stu_info_dep_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-people-40.png"))
stu_info_session_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-planner-40.png"))
stu_info_pro_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-extensions-folder-40.png"))
stu_info_time_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-hourglass-40.png"))
stu_info_clas_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-classroom-40.png"))
stu_info_enrol_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-hand-right-40.png"))

pro_approve_ico = ImageTk.PhotoImage(Image.open(r"Images/approve.ico"))
pro_proposal_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-business-40.png"))
pro_phases_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-combo-chart-40.png"))
pro_phases_member_ico = ImageTk.PhotoImage(Image.open(r"Images/icons8-online-community-40.png"))

# ================Functions==================#
def garbage_func():
    global upper_button_frame
    global book_down_frame
    upper_button_frame = Label(root, bg='#221f28', borderwidth=0, relief=SUNKEN)
    upper_button_frame.grid(row=1, column=1, sticky='nsew')
    book_down_frame = Label(root, bg='#162538', borderwidth=0, font=30, relief=SUNKEN)
    book_down_frame.grid(row=1, column=0, sticky='nsew')


def testfun():
    Working_Area = Label(root, image=dog, borderwidth=0, relief=SUNKEN)
    Working_Area.grid(row=2, column=1, sticky='nsew')



def on_enter(e):
    # b1['background'] = 'green',
    # b1['foreground'] = 'red',
    # Student_func()
    Working_Area = Student_Info.StudentInfo(root)
    Working_Area.grid(row=2,column=1, sticky='nsew')


def on_leave(e):
    b1['background'] = 'SystemButtonFace'
def Stu_depart_enter(e):
    Working_Area = Student_info_depart.Stu_depart(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Stu_Ses_enter(e):
    Working_Area = Student_info_session.Stu_info_ses(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Stu_Time_enter(e):
    Working_Area = Student_info_time.Stu_info_Time(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Stu_Enroll_enter(e):
    Working_Area = Student_Info_Enroll.Stu_info_Enroll(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Stu_Pro_enter(e):
    Working_Area = Student_Info_Program.Stu_info_Program(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Stu_Class_enter(e):
    Working_Area = Student_Info_Class.Stu_info_Class(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Stu_cam_enter(e):
    b2['background'] = 'green',
    b2['foreground'] = 'red'
    Working_Area = Student_info_campus.Stu_cam(root)
    Working_Area.grid(row=2,column=1, sticky='nsew')
def Pro_category_enter(e):
    Working_Area = Project_category_file.Project_pro(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Pro_project_enter(e):
    Working_Area = Project_pro_file.Pro_Project(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Pro_proposal_enter(e):
    Working_Area = Project_proposal.Project_Proposal(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Pro_phase_enter(e):
    Working_Area = Project_phase.project_phases_class(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Pro_phase_mem_enter(e):
    Working_Area = Project_phase_member.Project_phase_member(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Int_design_enter(e):
    Working_Area = Internal_designation.Int_designation(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Int_super_enter(e):
    Working_Area = Internal_supervisor.Int_supervisor(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Ext_super_enter(e):
    Working_Area = External_File.Supervisor_Info(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Ext_Year_enter(e):
    Working_Area = External_Evaluation_Year.Evaluation_Year(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Ext_Class_enter(e):
    Working_Area = External_Evaluation_Classes.Supervisor_Classes_Info(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Ext_Doc_enter(e):
    Working_Area = Int_Sup_Documentation_Result.Result_Info(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Ext_Viva_enter(e):
    Working_Area = Ext_Sup_Viva_Result.Viva_Result(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
def Int_sup_report(e):
    Working_Area = Assign_internal_super_report.Supervisor_Report(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')
class Book_down:
    def Label_book_down(self):
        global book_down_frame
        book_down_frame = Label(root, bg='#162538', borderwidth=0, font=30, relief=SUNKEN)
        book_down_frame.grid(row=1, column=0, sticky='nsew')


def Home_func():
    book_down_frame.destroy()
    upper_button_frame.destroy()
    Working_Area.destroy()
    Slider_Label.destroy()
    Label_upper1.label1(0)
    Label_upper2.label2(0)
    garbage_func()
    Label_Slider.label3(0)
    Workind_Label.label4(0)

    # Working_Area = Label(root, image=im3, borderwidth=0, relief=SUNKEN)
    # Working_Area.grid(row=2, column=1, sticky='nsew')

    # Workind_Label.label4(0)
    Close_Button.close_btn(0)


def Student_func():
    Book_down.Label_book_down(0)
    Working_Area = Student_Info.StudentInfo(root)
    Working_Area.grid(row=2, column=1)
    upper_button_frame=Student_Button_Label.Student_info_button(0)
    # upper_button_frame.grid(row=1, column=1, sticky='nsew')


def Project_func():
    # Working_Area.destroy()
    # Book_down.Label_book_down(0)
    # Upper_frame.Label_upper_frame(0)
    upper_button_frame = Project_button_label.Pro_Button(0)
    Working_Area = Project_category_file.Project_pro(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')


def Internal_func():
    # Book_down.Label_book_down(0)
    # Upper_frame.Label_upper_frame(0)
    upper_button_frame = Internal_button_label.Int_Button(0)
    Working_Area = Internal_designation.Int_designation(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')


def Assign_internal_func():
    # Book_down.Label_book_down(0)
    # Upper_frame.Label_upper_frame(0)
    upper_button_frame = Assign_button_For_Internal_label.Assign_int_Button(0)
    Working_Area = Assign_internal_supervisor.Int_supervisor(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')


def External_func():
    upper_button_frame = External_button_label.Ext_Button(0)
    Working_Area = External_File.Supervisor_Info(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')


def Report_func():
    # Book_down.Label_book_down(0)
    upper_button_frame = Report_Button_Label.Report_Button(0)
    Working_Area = Label(root, image=report_zone, borderwidth=0, relief=SUNKEN)
    Working_Area.grid(row=2, column=1, sticky='nsew')


def Results_func():
    upper_button_frame = Assign_internal_button_label.Assign_int_Button(0)
    Working_Area = Int_Sup_Documentation_Result.Result_Info(root)
    Working_Area.grid(row=2, column=1, sticky='nsew')


class Student_Button_Label:
    def Student_info_button(self):
        Stu_upper_button_frame = Label(root, bg='#221f28', borderwidth=0, relief=SUNKEN)
        Stu_upper_button_frame.grid(row=1, column=1, sticky='nsew')

        color_label = Label(Stu_upper_button_frame, bg='#221f28', text='\t\t', borderwidth=0,
                            font=30, relief=SUNKEN)
        color_label.grid(row=0, column=0, sticky='nsew')
        global b1,b2
        b1 = Button(Stu_upper_button_frame, compound=LEFT, text='Student', font=40,
                    activeforeground='#00f0ff',image=stu_info_student_ico)
        b1.bind('<Button-1>', on_enter)
        b1.bind("<Return>", on_enter)
        b1.focus_set()
        b1.grid(row=0, column=1,padx=5)
        b2 = Button(Stu_upper_button_frame, compound=LEFT, text='Campus',image=stu_info_campus_ico)
        b2.bind("<Button-1>",Stu_cam_enter)
        b2.bind("<Return>", Stu_cam_enter)
        b2.focus_set()
        b2.grid(row=0, column=2,padx=5)
        b3 = Button(Stu_upper_button_frame, compound=LEFT, text='Department', activeforeground='#00f0ff',image=stu_info_dep_ico)
        b3.bind("<Button-1>",Stu_depart_enter)
        b3.bind("<Return>",Stu_depart_enter)
        b3.grid(row=0,column=3,padx=5)
        b4=Button(Stu_upper_button_frame, compound=LEFT, text='Session',image=stu_info_session_ico)
        b4.bind("<Button-1>", Stu_Ses_enter)
        b4.bind("<Return>", Stu_Ses_enter)
        b4.grid(row=0, column=4,padx=5)
        b5=Button(Stu_upper_button_frame, compound=LEFT, text='Program',image=stu_info_pro_ico)
        b5.bind("<Button-1>", Stu_Pro_enter)
        b5.bind("<Return>", Stu_Pro_enter)
        b5.grid(row=0, column=5,padx=5)
        b6=Button(Stu_upper_button_frame, compound=LEFT, text='Timing',image=stu_info_time_ico)
        b6.bind("<Button-1>", Stu_Time_enter)
        b6.bind("<Return>", Stu_Time_enter)
        b6.grid(row=0, column=6,padx=5)
        b7=Button(Stu_upper_button_frame, compound=LEFT, text='Classes',image=stu_info_clas_ico)
        b7.bind("<Button-1>", Stu_Class_enter)
        b7.bind("<Return>", Stu_Class_enter)
        b7.grid(row=0, column=7,padx=5)
        b8=Button(Stu_upper_button_frame, compound=LEFT, text='Enrollment',image=stu_info_enrol_ico)
        b8.bind("<Button-1>", Stu_Enroll_enter)
        b8.bind("<Return>", Stu_Enroll_enter)
        b8.grid(row=0, column=8,padx=5)


class Project_button_label:
    def Pro_Button(self):
        Pro_upper_button_frame = Label(root, bg='#221f28', borderwidth=0, relief=SUNKEN)
        Pro_upper_button_frame.grid(row=1, column=1, sticky='nsew')

        color_label = Label(Pro_upper_button_frame, bg='#221f28', text='             \t\t', borderwidth=0,
                            font=30, relief=SUNKEN)
        color_label.grid(row=0, column=0, sticky='nsew')
        global b1
        pb1 = Button(Pro_upper_button_frame, compound=LEFT, text='Project Category',image=pro_approve_ico)
        pb1.bind('<Button-1>', Pro_category_enter)
        # b1.bind("<Return>", on_enter)
        # b1.focus_set()
        pb1.grid(row=0, column=1,ipady=4,padx=10)
        b2 = Button(Pro_upper_button_frame, compound=LEFT, text='Project',image=project_image_icon)
        b2.bind('<Button-1>', Pro_project_enter)
        # b2.bind("<Return>", on_enter)
        # b2.focus_set()
        b2.grid(row=0, column=2,padx=10)
        b3 = Button(Pro_upper_button_frame, compound=LEFT, text='Proposal', activeforeground='#00f0ff',image=pro_proposal_ico)
        b3.bind("<Button-1>",Pro_proposal_enter)
        b3.grid(row=0,column=3,padx=10)
        b4 = Button(Pro_upper_button_frame, compound=LEFT, text='Pheses',image=pro_phases_ico)
        b4.bind("<Button-1>",Pro_phase_enter)
        b4.grid(row=0, column=4,padx=10)
        b5 = Button(Pro_upper_button_frame, compound=LEFT, text='Pheses Member',image=pro_phases_member_ico)
        b5.bind("<Button-1>",Pro_phase_mem_enter)
        b5.grid(row=0, column=5,padx=10)


class Internal_button_label:
    def Int_Button(self):
        Pro_upper_button_frame = Label(root, bg='#221f28', borderwidth=0, relief=SUNKEN)
        Pro_upper_button_frame.grid(row=1, column=1, sticky='nsew')

        color_label = Label(Pro_upper_button_frame, bg='#221f28', text='             \t\t', borderwidth=0,
                            font=30, relief=SUNKEN)
        color_label.grid(row=0, column=0, sticky='nsew')
        global b1
        pb1 = Button(Pro_upper_button_frame, compound=LEFT, text='Designation',image=pro_approve_ico)
        pb1.bind('<Button-1>',Int_design_enter)
        # b1.bind("<Return>", on_enter)
        # b1.focus_set()
        pb1.grid(row=0, column=1,ipady=4,padx=10)
        b2 = Button(Pro_upper_button_frame, compound=LEFT, text='Internal Supervisor',image=project_image_icon)
        b2.bind('<Button-1>',Int_super_enter)
        # b2.bind("<Return>", on_enter)
        # b2.focus_set()
        b2.grid(row=0, column=2,padx=10)


class External_button_label:
    def Ext_Button(self):
        Pro_upper_button_frame = Label(root, bg='#221f28', borderwidth=0, relief=SUNKEN)
        Pro_upper_button_frame.grid(row=1, column=1, sticky='nsew')

        color_label = Label(Pro_upper_button_frame, bg='#221f28', text='             \t\t', borderwidth=0,
                            font=30, relief=SUNKEN)
        color_label.grid(row=0, column=0, sticky='nsew')
        global b1
        pb1 = Button(Pro_upper_button_frame, compound=LEFT, text='External Supervisor',image=pro_approve_ico)
        pb1.bind('<Button-1>',Ext_super_enter)
        # b1.bind("<Return>", on_enter)
        # b1.focus_set()
        pb1.grid(row=0, column=1,ipady=4,padx=10)
        b2 = Button(Pro_upper_button_frame, compound=LEFT, text='Evaluation Year',image=project_image_icon)
        b2.bind('<Button-1>',Ext_Year_enter)
        # b2.bind("<Return>", on_enter)
        # b2.focus_set()
        b2.grid(row=0, column=2,padx=10)

        # pb1.grid(row=0, column=1, ipady=4, padx=10)
        b21 = Button(Pro_upper_button_frame, compound=LEFT, text='Evaluation Classes', image=project_image_icon)
        b21.bind('<Button-1>', Ext_Class_enter)
        # b2.bind("<Return>", on_enter)
        # b2.focus_set()
        b21.grid(row=0, column=3, padx=10)


class Assign_internal_button_label:
    def Assign_int_Button(self):
        Pro_upper_button_frame = Label(root, bg='#221f28', borderwidth=0, relief=SUNKEN)
        Pro_upper_button_frame.grid(row=1, column=1, sticky='nsew')

        color_label = Label(Pro_upper_button_frame, bg='#221f28', text='             \t\t', borderwidth=0,
                            font=30, relief=SUNKEN)
        color_label.grid(row=0, column=0, sticky='nsew')
        global b1
        pb1 = Button(Pro_upper_button_frame, compound=LEFT, text='Internal Supervisor Documentation Result',image=pro_approve_ico)
        pb1.bind('<Button-1>',Ext_Doc_enter)
        # b1.bind("<Return>", on_enter)
        # b1.focus_set()
        pb1.grid(row=0, column=1,ipady=4,padx=10)
        b2 = Button(Pro_upper_button_frame, compound=LEFT, text='External Supervisor Viva Result',image=project_image_icon)
        b2.bind('<Button-1>',Ext_Viva_enter)
        # b2.bind("<Return>", on_enter)
        # b2.focus_set()
        b2.grid(row=0, column=2,padx=10)

#
class Assign_button_For_Internal_label:
    def Assign_int_Button(self):
        Pro_upper_button_frame = Label(root, bg='#221f28', borderwidth=0, relief=SUNKEN)
        Pro_upper_button_frame.grid(row=1, column=1, sticky='nsew')

        color_label = Label(Pro_upper_button_frame, bg='#221f28', text='             \t\t', borderwidth=0,
                            font=30, relief=SUNKEN)
        color_label.grid(row=0, column=0, sticky='nsew')
        global b1
        pb1 = Button(Pro_upper_button_frame, compound=LEFT, text="Assign Internal Supervisor's to Students",image=pro_approve_ico)
        # pb1.bind('<Button-1>',Ext_Doc_enter)
        # b1.bind("<Return>", on_enter)
        # b1.focus_set()
        pb1.grid(row=0, column=1,ipady=4,padx=10)


class Report_Button_Label:
    def Report_Button(self):
        Pro_upper_button_frame = Label(root, bg='#221f28', borderwidth=0, relief=SUNKEN)
        Pro_upper_button_frame.grid(row=1, column=1, sticky='nsew')

        color_label = Label(Pro_upper_button_frame, bg='#221f28', text='             \t\t', borderwidth=0,
                            font=30, relief=SUNKEN)
        color_label.grid(row=0, column=0, sticky='nsew')
        global b1
        pb1 = Button(Pro_upper_button_frame, compound=LEFT, text='Assign Internal Supervisor Report',image=pro_approve_ico)
        pb1.bind('<Button-1>',Int_sup_report)
        # b1.bind("<Return>", on_enter)
        # b1.focus_set()
        pb1.grid(row=0, column=1,ipady=4,padx=10)

        pb1 = Button(Pro_upper_button_frame, compound=LEFT, text='Internal Supervisor Result Report',image=pro_approve_ico)
        # pb1.bind('<Button-1>',Results_func)
        # b1.bind("<Return>", on_enter)
        # b1.focus_set()
        pb1.grid(row=0, column=2,ipady=4,padx=10)

        pb1 = Button(Pro_upper_button_frame, compound=LEFT, text='External Supervisor Result Report', image=pro_approve_ico)
        # pb1.bind('<Button-1>', Results_func)
        # b1.bind("<Return>", on_enter)
        # b1.focus_set()
        pb1.grid(row=0, column=3, ipady=4, padx=10)

        pb1 = Button(Pro_upper_button_frame, compound=LEFT, text='Previously Project Done Report', image=pro_approve_ico)
        # pb1.bind('<Button-1>', Results_func)
        # b1.bind("<Return>", on_enter)
        # b1.focus_set()
        pb1.grid(row=0, column=4, ipady=4, padx=10)
# ================Frame1==================#
class Label_upper1:

    def __init__(self, x):
        self.x = x

    def label1(self):
        global Book_image_label
        Book_image_label = Label(root, image=ima, borderwidth=0, relief=SUNKEN)
        Book_image_label.grid(row=0, column=0, sticky='nsew')


# =================Frame 2=================#
class Label_upper2:
    def label2(self):
        global Title_Label
        Title_Label = Label(root, image=ima2, borderwidth=0, relief=SUNKEN)
        Title_Label.grid(row=0, column=1, sticky='nsew')
        Button(root, text='Software Project\n Management System', bg='#21405f', fg='#FFFFFF',
               font=('Helvetica', 18, 'bold'),
               borderwidth=0, relief=SUNKEN, state='disabled').grid(row=0, column=1, sticky=E, ipadx=40, ipady=18)


# ============Close Button=================#

class Close_Button:
    def close_btn(self):
        global close_button_label
        close_button_label = Button(root, text='X', foreground='#ffffff', bg='red', command=lambda: root.destroy(),
                                    font=8)
        close_button_label.grid(row=0, column=1, sticky=NE, ipadx=15, ipady=1)


###########################################

# =====================Frame 3=========================#

class Label_Slider:
    def label3(self):
        global Slider_Label
        Slider_Label = Label(root, bg='#221f28', borderwidth=0, relief=SUNKEN)
        Slider_Label.grid(row=2, column=0, sticky='nsew', rowspan=2)

        sl1_btn = Button(Slider_Label, compound=LEFT, font=('Helvetica', 16, 'bold'), text='Home',
                         image=home_image_icon,
                         borderwidth=0,
                         relief=SUNKEN, activeforeground='#ffffff', activebackground='#f0ff00',
                         takefocus='#00f0f0', command=Home_func)
        sl1_btn.grid(row=0, column=1, ipady=10, ipadx=30)
        sl2_btn = Button(Slider_Label, compound=LEFT, font=('Helvetica', 16, 'bold'), text='Student', image=student_image_icon,
               borderwidth=0,
               relief=SUNKEN, command=Student_func)
        sl2_btn.grid(row=1, ipady=10, column=1, ipadx=19)
        sl3_btn = Button(Slider_Label, compound=LEFT, font=('Helvetica', 16, 'bold'), text='Project', image=project_image_icon,
               borderwidth=0,
               relief=SUNKEN, command=Project_func)
        sl3_btn.grid(row=2, column=1, ipady=10, ipadx=23)
        sl4_btn = Button(Slider_Label, compound=LEFT, font=('Helvetica', 16, 'bold'), text='Internal', image=internal_image_icon,
               borderwidth=0,
               relief=SUNKEN, command=Internal_func)
        sl4_btn.grid(row=3, column=1, ipady=10, ipadx=21)
        sl5_btn = Button(Slider_Label, compound=LEFT, font=('Helvetica', 13, 'bold'), text='Assign Internal',
               image=assign_internal_imsge_icon,
               borderwidth=0, relief=SUNKEN, command=Assign_internal_func)
        sl5_btn.grid(row=4, column=1, ipady=10, ipadx=4)
        sl6_btn = Button(Slider_Label, compound=LEFT, font=('Helvetica', 16, 'bold'), text='External', image=external_image_icon,
               borderwidth=0,
               relief=SUNKEN, command=External_func)
        sl6_btn.grid(row=5, column=1, ipady=10, ipadx=17)
        sl7_btn = Button(Slider_Label, compound=LEFT, font=('Helvetica', 16, 'bold'), text='Report', image=report_image_icon,
               borderwidth=0,
               relief=SUNKEN, command=Report_func)
        sl7_btn.grid(row=7, column=1, ipady=10, ipadx=24)
        sl8_btn = Button(Slider_Label, compound=LEFT, font=('Helvetica', 16, 'bold'), text='Result', image=results_image_icon,
               borderwidth=0,
               relief=SUNKEN, command=Results_func)
        sl8_btn.grid(row=6, column=1, ipadx=26, ipady=10)
        sl9_btn = Button(Slider_Label, compound=LEFT, font=('Helvetica', 16, 'bold'), text='Exit', image=exit_image_icon,
               borderwidth=0,
               relief=SUNKEN, command=lambda: root.destroy())
        sl9_btn.grid(row=8, column=1, ipadx=39, ipady=10)
        # Label(frame3, text='').grid(row=9, column=1, ipadx=39, ipady=7)


# ====================Frame 4===================#

class Workind_Label:
    def label4(self):
        global Working_Area
        Working_Area = Label(root, image=im3, borderwidth=0, relief=SUNKEN)
        Working_Area.grid(row=2, column=1, sticky='nsew')


Label_upper1.label1(0)
Label_upper2.label2(0)
garbage_func()
Label_Slider.label3(0)
# Workind_Label.label4(0)
Working_Area = Label(root, image=im3, borderwidth=0, relief=SUNKEN)
Working_Area.grid(row=2, column=1, sticky='nsew')

Close_Button.close_btn(0)
mainloop()
