from tkinter import *
from PIL import Image, ImageTk, ImageDraw  # pip install pillow
from course import CourseClass
from students import StudentClass
def make_circle(image_path, size=(50, 50)):
    # Open the image and resize it
    image = Image.open(image_path).resize(size, Image.LANCZOS)
    
    # Create a circular mask
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)

    # Apply mask to image to get circular logo
    result = Image.new('RGBA', size, (0, 0, 0, 0))
    result.paste(image, (0, 0), mask)

    return result

class Project:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Load the circular logo
        self.logo_image = make_circle("images/logo_p.png")
        self.logo_dash = ImageTk.PhotoImage(self.logo_image)

        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT,
                      image=self.logo_dash, font=("goudy old style", 20, "bold"),
                      bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)

        Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2",command=self.add_course).place(x=20, y=5, width=200, height=40)

        Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2",command=self.add_Student).place(x=240, y=5, width=200, height=40)

        Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2").place(x=460, y=5, width=200, height=40)

        Button(M_Frame, text="View Student Results", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2").place(x=680, y=5, width=200, height=40)

        Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2").place(x=900, y=5, width=200, height=40)

        Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2").place(x=1120, y=5, width=200, height=40)

        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=400, y=180, width=920, height=350)

        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20),
                                bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20),
                                 bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20),
                                bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        footer = Label(self.root, text="SRMS Student Result Management System\nContact Us for any Technical Issue: 987xxxxx01",
                       font=("goudy old style", 12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def add_course(self):
        self.new_Win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_Win)
       
    def add_Student(self):
        self.new_Win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_Win)

if __name__ == "__main__":
    root = Tk()
    obj = Project(root)
    root.mainloop()