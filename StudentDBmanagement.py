from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
#home screen
db=Database("python_db")
root=Tk()
root.title("STUDENT_INFORMATION SYSTEM")
root.geometry("1370x780")
root.state("zoom")

#enteries frame

entries_frame=Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="STUDENT_INFORMATION SYSTEM",font=("caliber",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2)


lname=Label(entries_frame,text="NAME",font=("caliber",16),bg="#535c68",fg="white")
lname.grid(row=1,column=0)
name=StringVar()

txtname=Entry(entries_frame,textvariable=name,font=("caliber",16),bg="#535c68",fg="white",width=30)
txtname.grid(row=1,column=1,padx=10,pady=10)

age=StringVar()
lage=Label(entries_frame,text="AGE",font=("caliber",16),bg="#535c68",fg="white")
lage.grid(row=1,column=2)
txtage=Entry(entries_frame,textvariable=age,font=("caliber",16),bg="#535c68",fg="white",width=30)
txtage.grid(row=1,column=3,padx=10,pady=10)


dob=StringVar()
ldob=Label(entries_frame,text="D_O_B",font=("caliber",16),bg="#535c68",fg="white")
ldob.grid(row=2,column=0)
txtdob=Entry(entries_frame,textvariable=dob,font=("caliber",16),bg="#535c68",fg="white",width=30)
txtdob.grid(row=2,column=1,padx=10,pady=10)

email=StringVar()
lemail=Label(entries_frame,text="EMAIL",font=("caliber",16),bg="#535c68",fg="white")
lemail.grid(row=2,column=2)
txtemail=Entry(entries_frame,textvariable=email,font=("caliber",16),bg="#535c68",fg="white",width=30)
txtemail.grid(row=2,column=3,padx=10,pady=10)

gender=StringVar()
lgender=Label(entries_frame,text="GENDER",font=("caliber",16),bg="#535c68",fg="white")
lgender.grid(row=3,column=0)
combogender=ttk.Combobox(entries_frame,font=("caliber",16,),width=28,textvariable=gender,state="readonly")
combogender['values']=("MALE","FEMAL")
combogender.grid(row=3,column=1,padx=10,pady=10)

contact=StringVar()
lcon=Label(entries_frame,text="CONTACT",font=("caliber",16),bg="#535c68",fg="white")
lcon.grid(row=3,column=2)
txtcon=Entry(entries_frame,textvariable=contact,font=("caliber",16),bg="#535c68",fg="white",width=30)
txtcon.grid(row=3,column=3,padx=10,pady=10)

address=StringVar()
ladd=Label(entries_frame,text="ADDRESS",font=("caliber",16),bg="#535c68",fg="white")
ladd.grid(row=4,column=0,padx=10,pady=10)

txtadd=Text(entries_frame,width=85,height=5,font=("caliber",16))
txtadd.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data["values"]
    name.set(row[1])
    age.set(row[2])
    dob.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtadd.delete(1.0, END)
    txtadd.insert(END, row[7])

def displayall():
    tv.delete(*tv.get_children())
    for res in db.view():
        tv.insert("", END, values=res)

def add_student():
    if( txtname.get()=="" or txtadd.get(1.0,END)=="" or txtage.get()=="" or txtcon.get()=="" or txtdob.get()=="" or txtemail.get()=="" ):
        messagebox.showerror("ERROR!!!!!!!!","please fill all the all details")
        return
    db.insert(txtname.get(),txtage.get(),txtdob.get(),txtemail.get(),combogender.get(),txtcon.get(),txtadd.get(1.0,END))
    messagebox.showinfo("MESSAGE","Insert values successfully")
    clearall()
    displayall()





def update_student():
    if (txtname.get() == "" or txtadd.get(1.0,END) == "" or txtage.get() == "" or txtcon.get() == "" or txtdob.get() == "" or txtemail.get() == ""):
        messagebox.showerror("ERROR!!!!!!!!", "please fill all the all details")
        return
    db.update(row[0],txtname.get(), txtage.get(), txtdob.get(), txtemail.get(), combogender.get(), txtcon.get(),
              txtadd.get(1.0, END))
    messagebox.showinfo("MESSAGE", "Updated information successfully")
    clearall()
    displayall()


def delete_student():
    print("DELETE")
    db.remove(row[0])
    clearall()
    displayall()

def clearall():
    name.set("")
    age.set("")
    dob.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtadd.delete(1.0,END)




btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,pady=10,padx=10,sticky="w")

btnadd=Button(btn_frame,command=add_student,text="Add_Student",width=15,font=("caliber",16,"bold"),bg="#16a085",fg="white",bd=0)
btnadd.grid(row=0,column=0)

btnedit=Button(btn_frame,command=update_student,text="Update Details",width=15,font=("calibe",16,"bold"),bg="#2988b9",fg="white",bd=0)
btnedit.grid(row=0,column=1,padx=10)

btndel=Button(btn_frame,command=delete_student,text="Delete Details",width=15,font=("calibe",16,"bold"),bg="#c0392b",fg="white",bd=0)
btndel.grid(row=0,column=2,padx=10)

btnclr=Button(btn_frame,command=clearall,text="Clear Details",width=15,font=("calibe",16,"bold"),bg="#f39c12",fg="white",bd=0)
btnclr.grid(row=0,column=3,padx=10)

#table frame
tree_frame=Frame(root, bg="white")
tree_frame.place(x=0, y=407, width=1980, height=520)

style = ttk.Style()
style.configure("mystyle.Treeview",font=("calibe",16),rowhieght=50)
style.configure("mystyle.Treeview.Heading", font=("calibe", 10))
tv = ttk.Treeview(tree_frame,columns=('1', '2', '3', '4', '5', '6', '7', '8'), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=1)
tv.heading("2", text="NAME")
tv.column("2", width=10)
tv.heading("3", text="AGE")
tv.column("3", width=5)
tv.heading("4", text="D_O_B")
tv.column("4", width=10)
tv.heading("5", text="EMAIL")
tv.column("5", width=15)
tv.heading("6", text="GENDER")
tv.column("6", width=10)
tv.heading("7", text="CONTACT")
tv.column("7", width=10)
tv.heading("8", text="ADDRESS")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)
displayall()
root.mainloop()
