import sqlite3
from tkinter import *
from tkcalendar import DateEntry, Calendar
import time
import random
root = Tk()
conn = sqlite3.connect('Whole_Database.db')
cmd = conn.cursor()


def test(Campus_entry):
    print("Enter in test mode")
    conn = sqlite3.connect('Whole_Database.db')
    cmd = conn.cursor()
    cmd.execute(f"insert into campustable(campusname) values (?)", [Campus_entry])
    conn.commit()
    # print(Campus_entry.get())
    print("Data Submited")

    conn.close()


# create table for Student Info-------------------
# cmd.execute('create table student_info (student_name text,student_father_name text,registration_no text,date_of_birth text,mobile_no text,c_n_i_c text)')
# create table for Student campus---------------------
# cmd.execute('create table campustable(campusname text)')
# create department table
# cmd.execute('create table Depart_table(name text)')
# create session for student
# cmd.execute('create table Depart_table(name text)')
# create Program table
# cmd.execute('create table Program_table(Name text,Department text)')


# testing table
import string
import random # define the random module
S = 6  # number of characters in the string.
# call random.choices() string module to find the string in Uppercase + numeric data.


# ran = ''.join(random.choices(string.ascii_uppercase, k = S))
# print("The randomly generated string is : " + str(ran)) # print the random data

# cmd.execute('create table Pro(Name text,Department text)')
# cmd.execute('DROP TABLE IF EXISTS Pro')
# asd = cmd.execute('select count(Name) from Pro')
#
# for ij in asd:
#     print(ij)
# cmd.execute('select * from campustable')
# data_list1 =[]
# for student in cmd:
#     print(student)
#     if student[0] == 'Pro':
#         cmd.execute('DROP TABLE IF EXISTS Pro')

        # print('Found,,,,,,,,,,,,,....................... table delete')
# done
# cmd.execute('select Registration_No,Student_Name,Roll_No,Internal_Name,Designation,E_Mail from Assign_Internal_Supervisor_Tabel')
# data_list1 =[]
# for student in cmd:
#     print(student)

# project phase member table
cmd.execute('create table Project_Phase_Member(Registration_NO text,Project_Name text, participation text)')

# create timming
# cmd.execute('create table Time_table(time text)')
# create class table
# cmd.execute('create table student_class (class_name text,student_department_name text,session text,program text,timing text)')
# assign class
# cmd.execute('create table student_class_assign (Registration_No text,Session text,Class_Name text)')
# create timming table
# cmd.execute('create table Timetable(Timing_Name text)')
# create enrollment table
# cmd.execute('create table student_enroll (Registration_No text,Student_Name text,Class_Name text,Session text,Timing text,Department_Name text,Program text, Roll_No text)')
# create projectcategory table
# cmd.execute('create table Project_Category_Table(Category_Name text)')
# create table project phase
# cmd.execute('create table Student_Project_Tabel (Project text,Category text,Registration_No text,Student_Name text,Class_Name text,Date_Created text,Date_Modified text, Confirmed text)')
# create table project proposal
# cmd.execute('create table Student_Proposal_Tabel (Registration_No text,Student_Name text,Project_Name text,Introduction text,Problem_Statement text,Mathdology text,Tools text,Technique text)')
#create project phase table
# cmd.execute('create table Student_Phase2_Table (Registration_No text,Project_Name text,Phase text,Discription text)')
# create  designation internal table
# cmd.execute('create table Internal_designation (designation text)')
# create Internal supervisor table
# cmd.execute('create table Internal_Supervisor_Tabel (Supervisor_Name text,Designation text,Department text,Employment_Code text,Phone_No text,Mobile_No text,E_Mail text)')
# create assign internal supervisor table
# cmd.execute('create table Assign_Internal_Supervisor_Tabel (Registration_No text,Student_Name text,Class_Name text,Session text,Timing text,Department_Name text,Program text, Roll_No text,Employment_Code text,Internal_Name text,Designation text,Department text,Mobile_No text,E_Mail text)')
#create external supervisor table
# cmd.execute('create table External_Supervisor_Table (Supervisor text,Organization text,'
#             'Designation text,Department text,Phone text,Mobile text,E_Mail text)')
#create external evaluation clasees table
# cmd.execute('create table External_Evaluation_Class_Table (Evaluation_Year text,Department text,'
#             'Program text,Class text,Session text,Timing text,Total_Student text,Total_Evaluation text)')
# create evaluation year table
# cmd.execute('create table External_Evaluation_Year_Table (Evaluation_Year text,Document_Submission text,Thesis_Submission text)')
# create internal supervisor documentation result table
# cmd.execute('create table Internal_Supervisor_Docum_Result_Tabel (Department_Name text,Program text,'
#             'Evaluation_Year text,Session text,Timing text,Registration_No text,Phase text,Student_Name text,'
#             'Enrollment text,Internal_Name text,Project_Name text,Marks text,GPA text,Grade text)')
# create external supervisor viva result table
# cmd.execute('create table External_Supervisor_Viva_Result_Table (Department_Name text,Program text,'
#             'Evaluation_Year text,Session text,Timing text,Registration_No text,External_Name text,'
#             'Phase text,Student_Name text,'
            # 'Enrollment text,Internal_Name text,Project_Name text,Marks text,GPA text,Grade text)')
# Assign internal supervisor report table

# Campus_entry = Entry(root, borderwidth=3, width=40, font=('Helvetica', 12, 'bold'))
# Campus_entry.grid(row=0, column=1, pady=10, padx=30)
# cmd.execute("insert into campustable(campusname) values '"+asdf+"'")
# cmd.execute("insert into campustable(campusname) values (?)",(Campus_entry.get(),))
# Button(root, text='click', command=lambda: pong()).grid()
# print(f"kjcsiisadfiusadolui{Campus_entry.get()}")
# asd = DateEntry(root, borderwidth=3, width=30, font=('Helvetica', 12, 'bold'))
# asd = Entry(root, width=4)
# asd.grid()
# bsd = DateEntry(root, borderwidth=3, width=30, font=('Helvetica', 12, 'bold'))
# bsd.grid()
# print(asd + bsd)
conn.commit()
conn.close()
mainloop()
