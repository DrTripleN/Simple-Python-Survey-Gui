import tkinter
from tkinter.ttk import *
from tkinter import messagebox

app = tkinter.Tk()
app.title("Centennial College")
app.geometry('750x400')
app.option_add("*font", ("Arial", 10))
app['background'] = "#e9d7c3"

# header
lblHeader = tkinter.Label(app, text="ICET STUDENT SURVEY", bg="#ccbee8", )
lblHeader.config(font=("Arial", 20, "bold italic"))
lblHeader.grid(column=0, row=0)
# name-entry
lblName = tkinter.Label(app, text="Full Name:", padx=20, pady=20, bg="#e9d7c3")
lblName.grid(column=0, row=1)
txtName = tkinter.Entry(app, width=40)
txtName.grid(column=4, row=1)
# RESIDENCY-RADIo
lblResi = tkinter.Label(app, text="Residency: ", bg="#e9d7c3")
lblResi.config(pady=10)
selected1 = tkinter.IntVar()

radioResi = tkinter.Radiobutton(app, text="Domestic", value=1, variable=selected1)
radioRes2 = tkinter.Radiobutton(app, text="International", value=2, variable=selected1)

lblResi.grid(column=0, row=2)
radioResi.grid(column=4, row=2)
radioRes2.grid(column=4, row=4)
# Program-combo
comboProgram = Combobox(app)
comboProgram['values'] = ('AI', 'Gaming', 'Health', 'Software')
comboProgram.current(1)
textProgram = tkinter.Label(app, text="Program:", pady=10, bg="#e9d7c3")
textProgram.grid(column=0, row=6)
comboProgram.grid(column=4, row=6)
# Checkbox
txtCourses = tkinter.Label(app, text="Course: ", pady=10, bg="#e9d7c3")
txtCourses.grid(column=0, row=8)
checked1 = tkinter.IntVar()
checked2 = tkinter.IntVar()
checked3 = tkinter.IntVar()
chkCourse1 = tkinter.Checkbutton(app, text="Programming 1", variable=checked1, bg="#e9d7c3")
chkCourse2 = tkinter.Checkbutton(app, text="Web Page Design", variable=checked2, bg="#e9d7c3")
chkCourse3 = tkinter.Checkbutton(app, text="Software Engineering", variable=checked3, pady=15, bg="#e9d7c3")
chkCourse1.grid(column=4, row=8)
chkCourse2.grid(column=4, row=10)
chkCourse3.grid(column=4, row=12)


# ENDBUTTONS
def reset():
    txtName.delete('0', tkinter.END)
    radioResi.deselect()
    radioRes2.deselect()
    comboProgram.set('')
    chkCourse1.deselect()
    chkCourse2.deselect()
    chkCourse3.deselect()


btnReset = tkinter.Button(app, text="Reset", command=reset, width=10, )
btnReset.grid(column=0, row=40)

courses = []


def viewData():
    if selected1.get() == 1:
        selected = "Domestic"

    else:
        selected = "International"

    if checked1.get() == 1:
        courses.append("COMP100")
    if checked2.get() == 1:
        courses.append("COMP213")
    if checked3.get() == 1:
        courses.append("COMP120")

    messagebox.showinfo('User Information',
                        f"{txtName.get()}\n{selected}\n{comboProgram.get()}\n{(courses)}")
    courses.clear()


def close():
    app.destroy()


btnOk = tkinter.Button(app, text="Ok", command=viewData, width=10, bg="green")
btnOk.grid(column=3, row=40)
btnExit = tkinter.Button(app, text="Exit", command=close, width=10, bg="red")
btnExit.grid(column=4, row=40)
app.mainloop()
