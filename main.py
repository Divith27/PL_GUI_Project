from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Employee.db")

#Window Size and BG color
root = Tk()
root.title("Crusaders Org.")
root.geometry("1920x1080+0+0")
root.config(bg="#152D35")
root.state("zoomed")

#App Icon
p1 = PhotoImage(file="C:\My Projects\Coding\PL_GUI_Project\man.png")
root.iconphoto(False, p1)

#Variables
name = StringVar()
age = StringVar()
dob = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

#Title
title = Label(root, text="Crusaders Org.", font=("Lato", 25, "bold"), fg="#D4ECDD", bg="#152D35")
title.grid(row=0, padx=10, pady=15, columnspan=2, sticky="w")

#Layout
lblName = Label(root, text="Name", font=("Lato", 18, "bold"), fg="#D4ECDD", bg="#152D35")
lblName.grid(row=1, column=0, padx=10, pady=10)
txtName = Entry(root, textvariable=name, font=("Lato", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblAge = Label(root, text="Age", font=("Lato", 18, "bold"), fg="#D4ECDD", bg="#152D35")
lblAge.grid(row=2, column=0, padx=10, pady=10)
txtAge = Entry(root, textvariable=age, font=("Lato", 16), width=30)
txtAge.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblDob = Label(root, text="DOB", font=("Lato", 18, "bold"), fg="#D4ECDD", bg="#152D35")
lblDob.grid(row=1, column=2, padx=10, pady=10)
txtDob = Entry(root, textvariable=dob, font=("Lato", 16), width=30)
txtDob.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblEmail = Label(root, text="Email", font=("Lato", 18, "bold"), fg="#D4ECDD", bg="#152D35")
lblEmail.grid(row=2, column=2, padx=10, pady=10)
txtEmail = Entry(root, textvariable=email, font=("Lato", 16), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblContact = Label(root, text="Contact No.", font=("Lato", 18, "bold"), fg="#D4ECDD", bg="#152D35")
lblContact.grid(row=3, column=0, padx=10, pady=10)
txtContact = Entry(root, textvariable=contact, font=("Lato", 16), width=30)
txtContact.grid(row=3, column=1, padx=10, pady=10, sticky="w")

lblGender = Label(root, text="Gender", font=("Lato", 18, "bold"), fg="#D4ECDD", bg="#152D35")
lblGender.grid(row=3, column=2, padx=10, pady=10)
comboGender = ttk.Combobox(root, font=("Lato", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=3, padx=10, sticky="w")

lblAddress = Label(root, text="Address", font=("Lato", 18, "bold"), fg="#D4ECDD", bg="#152D35")
lblAddress.grid(row=4, column=0, padx=10, pady=10)
txtAddress = Text(root, width=70, height=1, font=("Lato", 16))
txtAddress.grid(row=4, column=0, padx=15, columnspan=5)

#Functions
def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    print(row)
    name.set(row[1])
    age.set(row[2])
    dob.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)

def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDob.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txtName.get(),txtAge.get(), txtDob.get() , txtEmail.get() ,comboGender.get(), txtContact.get(), txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()

def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDob.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtDob.get(), txtEmail.get(), comboGender.get(), txtContact.get(), txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()

def delete_employee():
    db.remove(row[0])
    clearAll()
    dispalyAll()

def clearAll():
    name.set("")
    age.set("")
    dob.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0, END)

#Main Buttons
btnAdd = Button(root, command=add_employee, text="Add", font=("Lato", 16, "bold"), bg="#112031", fg="#D4ECDD", padx=25, pady=5).grid(row=1, column=4,padx=25, pady=10)
btnUpdate = Button(root, command=update_employee, text="Update", font=("Lato", 16, "bold"), bg="#112031", fg="#D4ECDD", padx=10, pady=5).grid(row=2, column=4,padx=25, pady=10)
btnDelete = Button(root, command=delete_employee, text="Delete", font=("Lato", 16, "bold"), bg="#112031", fg="#D4ECDD", padx=13, pady=5).grid(row=3, column=4,padx=25, pady=10)
btnClear = Button(root, command=clearAll, text="Clear", font=("Lato", 16, "bold"), bg="#112031", fg="#D4ECDD", padx=19, pady=5).grid(row=4, column=4,padx=25, pady=10)

#Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1300, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=10)
tv.heading("2", text="Name")
tv.column("2", width=150)
tv.heading("3", text="Age")
tv.column("3", width=15)
tv.heading("4", text="D.O.B")
tv.column("4", width=70)
tv.heading("5", text="Email")
tv.column("5", width=220)
tv.heading("6", text="Gender")
tv.column("6", width=50)
tv.heading("7", text="Contact")
tv.column("7", width=100)
tv.heading("8", text="Address")
tv.column("8", width=400)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()

root.mainloop()