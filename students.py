from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class StudentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="Manage Course Details", 
                      font=("goudy old style", 20, "bold"),
                      bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)

        self.var_roll = StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()

        lbl_Roll = Label(self.root, text="Roll No.", font=("goudy old style", 15, 'bold'), bg="white")
        lbl_Roll.place(x=10, y=60)
        lbl_Name = Label(self.root, text="Name", font=("goudy old style", 15, 'bold'), bg="white")
        lbl_Name.place(x=10, y=100)
        lbl_Email = Label(self.root, text="Email", font=("goudy old style", 15, 'bold'), bg="white")
        lbl_Email.place(x=10, y=140)
        lbl_Gender = Label(self.root, text="Gender", font=("goudy old style", 15, 'bold'), bg="white")
        lbl_Gender.place(x=10, y=180)
        
        
        lbl_state = Label(self.root, text="State", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=220)
        txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, 'bold'), bg="lightyellow").place(x=150, y=220, width=150)

        lbl_city = Label(self.root, text="City", font=("goudy old style", 15, 'bold'), bg="white").place(x=310, y=220)
        txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, 'bold'), bg="lightyellow").place(x=380, y=220, width=100)

        lbl_pin = Label(self.root, text="Pin", font=("goudy old style", 15, 'bold'), bg="white").place(x=500, y=220)
        txt_pin = Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15, 'bold'), bg="lightyellow").place(x=560, y=220, width=120)

       
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15, 'bold'), bg="white").place(x=10, y=260)

        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_roll.place(x=150, y=60, width=200)

        txt_name=Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, 'bold'), bg="lightyellow").place(x=150, y=100, width=200)
        txt_email= Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, 'bold'), bg="lightyellow").place(x=150, y=140, width=200)
        self.txt_gender= ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select","Male","Female","Others"),font=("goudy old style", 15, 'bold'), state='readonly',justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)
       


        
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 15, 'bold'), bg="white")
        lbl_dob.place(x=360, y=60)
        lbl_Contact = Label(self.root, text="Contact", font=("goudy old style", 15, 'bold'), bg="white")
        lbl_Contact.place(x=360, y=100)
        lbl_addmission = Label(self.root, text="Addmission", font=("goudy old style", 15, 'bold'), bg="white")
        lbl_addmission.place(x=360, y=140)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, 'bold'), bg="white")
        lbl_course.place(x=360, y=180)


        self.Course_list=[]


        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, 'bold'), bg="lightyellow").place(x=480, y=60, width=200)

        txt_Contact=Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, 'bold'), bg="lightyellow").place(x=480, y=100, width=200)
        txt_addmission= Entry(self.root, textvariable=self.a_date,font=("goudy old style", 15, 'bold'), bg="lightyellow").place(x=480, y=140, width=200)
        self.txt_course= ttk.Combobox(self.root, textvariable=self.var_course,values=self.Course_list,font=("goudy old style", 15, 'bold'), state='readonly',justify=CENTER)
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.set('Empty')


        
        

        
        self.txt_address = Text(self.root, font=("goudy old style", 15, 'bold'), bg="lightyellow")
        self.txt_address.place(x=150, y=260, width=540, height=100)

        Button(self.root, text='Save', font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.add).place(x=150, y=400, width=110, height=40)
        Button(self.root, text='Update', font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2",command=self.update).place(x=270, y=400, width=110, height=40)
        Button(self.root, text='Delete', font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2",command=self.delete).place(x=390, y=400, width=110, height=40)
        Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear).place(x=510, y=400, width=110, height=40)

        self.var_search = StringVar()
        lbl_search_roll = Label(self.root, text="Roll No.", font=("goudy old style", 15, 'bold'), bg="white")
        lbl_search_roll.place(x=720, y=60)
        Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, 'bold'), bg="lightyellow").place(x=870, y=60, width=180)
        Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2",command=self.search).place(x=1070, y=60, width=120, height=28)

        self.c_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.c_frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.c_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.c_frame, orient=HORIZONTAL)
        self.CourseTable = ttk.Treeview(self.c_frame, columns=("Roll", "name", "email", "gender", "dob","contact","addmission","course","state","city","pin","address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("Roll", text="Roll No.")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("addmission", text="Addmission")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("state", text="State")
        self.CourseTable.heading("city", text="City")
        self.CourseTable.heading("pin", text="Pin")
        self.CourseTable["show"] = 'headings'
        self.CourseTable.column("roll", width=50)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("email", width=100)
        self.CourseTable.column("gender", width=100)
        self.CourseTable.column("contact", width=100)
        self.CourseTable.column("addmission", width=100)
        self.CourseTable.column("course", width=100)
        self.CourseTable.column("state", width=100)
        self.CourseTable.column("city", width=100)
        self.CourseTable.column("pin", width=150)
        
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        # self.var_roll.set(row[4])
        self.txt_description.delete('1.0',END)
        self.txt_roll.config(state=NORMAL)
    
    def delete(self):
        con = sqlite3.connect(database="project.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
                return

            # Check if course already exists
            cur.execute("SELECT * FROM course WHERE name = ?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "please select course from the list first", parent=self.root)
            else:
                op=messagebox.askyesno('confirm','Do you really want to delete?',parent=self.root)
                if op==True:
                    cur.execute('delete from course where name=?',(self.var_roll.get(),))
                    con.commit()
                    messagebox.showinfo("Delete","Course deleted successfully",parent=self.root)
                    self.clear()


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()




    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
       
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        # print(row)
        self.var_roll.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        # self.var_roll.set(row[4])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])

    def add(self):
        con = sqlite3.connect(database="project.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
                return

            # Check if course already exists
            cur.execute("SELECT * FROM course WHERE name = ?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Course Name already present", parent=self.root)
            else:
                # Insert new course
                cur.execute("INSERT INTO course (name, duration, charges, description) VALUES (?, ?, ?, ?)", (
                    self.var_roll.get(),
                    self.var_duration.get(),
                    self.var_charges.get(),
                    self.txt_description.get("1.0", END).strip()
                ))
                con.commit()
                messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                self.clear()
                self.show()  # Refresh the table
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()



    def update(self):
        con = sqlite3.connect(database="project.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
                return

            # Check if course already exists
            cur.execute("SELECT * FROM course WHERE name = ?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row  == None:
                messagebox.showerror("Error", "Select Course from list", parent=self.root)
            else:
                # Insert new course
                cur.execute("update course set duration=?, charges=?, description=? where name=?", (
                   
                    self.var_duration.get(),
                    self.var_charges.get(),
                    self.txt_description.get("1.0", END).strip(),
                     self.var_roll.get(),
                ))
                con.commit()
                messagebox.showinfo("Success", "Course update successfully", parent=self.root)
                self.clear()
                self.show()  # Refresh the table
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()
    def show(self):
        con = sqlite3.connect(database="project.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()
    def search(self):
        con = sqlite3.connect(database="project.db")
        cur = con.cursor()
        try:
            cur.execute(f"SELECT * FROM course where Name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def clear(self):
        self.var_roll.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.txt_description.delete("1.0", END)      


        

if __name__ == "__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()
