from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

root=Tk()
root.title("py_log_reg_gui_app")
root.geometry("1250x700+210+100")

root.config(bg=background)

file = pathlib.Path("Employee Data.xlsx")
if file.exists():
    pass
else:
    file = Workbook()
    sheet = file.active
    sheet['A1'] = "Registration No: "
    sheet['B1'] = "Employee Name: "
    sheet['C1'] = "Father's Name: "
    sheet['D1'] = "Mother's Name: "
    sheet['E1'] = "Present Address: "
    sheet['F1'] = "Permanent Address: "
    sheet['G1'] = "Gender: "
    sheet['H1'] = "Date of Birth: "
    sheet['I1'] = "Nationality: "
    sheet['J1'] = "E-mail ID:"
    sheet['K1'] = "Contact No: "
    sheet['L1'] = "Company ID No: "
    sheet['M1'] = "Company Name: "
    sheet['N1'] = "Job Position: "
    sheet['O1'] = "Joining Date: "
    sheet['P1'] = "Till Now: "
    sheet['Q1'] = "Registration Date: "
    sheet['R1'] = "Count Experience: "
    sheet['S1'] = "Remarks: "
    sheet['T1'] = "Previous Job History: "


file.save("Employee Data.xlsx")

#Show Image Function
def showImage():
    global filename
    global img
    filename = filedialog.askopenfile(initialdir=os.getcwd(), title="Select Images", filetypes=(("JPG Fiel", "*.jpg"),
                                                                                                ("PNG File", "*.png"),
                                                                                                ("All Files", "*.txt")))
    img = (Image.open(filename))
    resized_image = img.resize((190,190))
    photo2 = ImageTk.PhotoImage(resized_image)
    lbl.config(image=photo2)
    lbl.image = photo2


#Exit Function
def Exit():
    root.destroy()

#Select Function
def selection():
    value = radio.get()
    if value == 1:
        gender = "Male"
        # print(gender)
    # elif value == 2:
    #     gender = "Female"
    #     print(gender)
    # elif value == 3:
    #     gender = "Others"
    else:
        gender = "Female"
        # print(gender)

#Top Frames
Label(root, text="Email: shipuidb@gmail.com", width=10, height=3, bg="#f0687c", anchor='e').pack(side=TOP, fill=X)
Label(root, text="Employee Registration", width=10, height=2, bg="#c36464", fg="#fff", font='arial 20 bold').pack(side=TOP, fill=X)

#Search Box to Update
search = StringVar()
Entry(root, textvariable=search, width=15, bd=2, font="arial 20").place(x=820, y=70)
imageicon3 = PhotoImage(file="./images/search.png")
srch = Button(root, text="Search", compound=LEFT, image=imageicon3, width=123, bg="#68ddfa", font="arial 13 bold")
srch.place(x=1060, y=60)
imageicon4 = PhotoImage(file="./images/layer.png")
update_Button = Button(root, image=imageicon4, bg="#c36464")
update_Button.place(x=110, y=64)

#Registration No
Label(root, text="Registration No", font="arial 13", fg=framebg, bg=background).place(x=30,y=150)
Label(root, text="Date", font="arial 13", fg=framebg, bg=background).place(x=500,y=150)

Registration = StringVar()
Date = StringVar()

reg_Entry = Entry(root, textvariable=Registration, width=15, font="arial 10")
reg_Entry.place(x=160, y=150)

#Registration Date
today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_Entry = Entry(root, textvariable=Date, width=15, font="arial 10")
date_Entry.place(x=550, y=150)
Date.set(d1)

#Employee Details
employee_obj = LabelFrame(root, text="Employee Details", bd=2, font=20, width=900, bg=framebg, fg=framefg, height=250, relief=GROOVE)
employee_obj.place(x=30, y=200)

Label(employee_obj, text="Full Name", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=50)
Label(employee_obj, text="Date of Birth", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=100)
Label(employee_obj, text="Gender", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=150)

Label(employee_obj, text="Nationality", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=50)
Label(employee_obj, text="Email", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=150)
Label(employee_obj, text="Contact No", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=100)

name = StringVar()
name_Entry = Entry(employee_obj, textvariable=name, width=20, font="arial 10")
name_Entry.place(x=160, y=50)

dob = StringVar()
dob_Entry = Entry(employee_obj, textvariable=dob, width=20, font="arial 10")
dob_Entry.place(x=160, y=100)

contact = StringVar()
contact_Entry = Entry(employee_obj, textvariable=contact, width=20, font="arial 10")
contact_Entry.place(x=630, y=100)

email = StringVar()
email_Entry = Entry(employee_obj, textvariable=email, width=20, font="arial 10")
email_Entry.place(x=630, y=150)

nationality = StringVar()
nationality_Entry = Entry(employee_obj, textvariable=nationality, width=20, font="arial 10")
nationality_Entry.place(x=630, y=50)

#ComboBox for Nationality
# Class = Combobox(employee_obj, values = ['1', '2','3','4','5'], font="Roboto 10", width=17, state="r")
# Class.place(x=630, y=50)
# Class.set("Select Class")

#Radio Button for Gender
radio = IntVar()
r1 = Radiobutton(employee_obj, text="Male", variable=radio, value=1, bg=framebg, fg=framefg, command=selection())
r1.place(x=150, y=150)
r2 = Radiobutton(employee_obj, text="Female", variable=radio, value=2, bg=framebg, fg=framefg, command=selection())
r2.place(x=200, y=150)

# r3 = Radiobutton(employee_obj, text="Others", variable=radio, value=2, bg=framebg, fg=framefg, command=selection())
# r3.place(x=250, y=150)


#Family Details
family_obj = LabelFrame(root, text="Family Details", bd=2, font=20, width=900, bg=framebg, fg=framefg, height=220, relief=GROOVE)
family_obj.place(x=30, y=470)

Label(family_obj, text="Father's Name", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=50)
Label(family_obj, text="Mother's Name", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=100)
Label(family_obj, text="Spouse Name", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=150)

Label(family_obj, text="Present Address", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=150)
Label(family_obj, text="Permanent Address", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=50)

father_Name = StringVar()
father_Name_Entry = Entry(family_obj, textvariable=father_Name, width=20, font="arial 10")
father_Name_Entry.place(x=160, y=50)

mother_Name = StringVar()
mother_Name_Entry = Entry(family_obj, textvariable=mother_Name, width=20, font="arial 10")
mother_Name_Entry.place(x=160, y=100)

spouse_Name = StringVar()
spouse_Name_Entry = Entry(family_obj, textvariable=spouse_Name, width=20, font="arial 10")
spouse_Name_Entry.place(x=160, y=150)

permanent_Add = StringVar()
permanent_Add_Entry = Entry(family_obj, textvariable=permanent_Add, width=20, font="arial 10")
permanent_Add_Entry.place(x=670, y=50)

present_Add = StringVar()
present_Add_Entry = Entry(family_obj, textvariable=present_Add, width=20, font="arial 10")
present_Add_Entry.place(x=670, y=150)

#image
f= Frame(root, bd=3, bg="black", width=200, height=200, relief=GROOVE)
f.place(x=1000, y=150)

img = PhotoImage(file="./images/uploading_photo.png")
lbl = Label(f, bg="black", image=img)
lbl.place(x=0, y=0)

#Button
Button(root, text="Upload", width=19, height=2, font="arial 12 bold", bg="lightblue", command=showImage).place(x=1000, y=370)
save_Button = Button(root, text="Save", width=19, height=2, font="arial 12 bold", bg="lightgreen")
save_Button.place(x=1000, y=450)
Button(root, text="Reset", width=19, height=2, font="arial 12 bold", bg="lightpink").place(x=1000, y=530)
Button(root, text="Exit", width=19, height=2, font="arial 12 bold", bg="grey", command=Exit).place(x=1000, y=610)



root.mainloop()
