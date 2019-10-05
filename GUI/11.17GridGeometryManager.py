import tkinter

mainwindow = tkinter.Tk()

mainwindow.title("Pack Geometry Manager")
mainwindow.geometry("640x480+0+0")

l = tkinter.Label(mainwindow, text="Hello World !!")
l.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainwindow)
leftFrame.grid(row=1, column=1)
canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=2)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainwindow)
rightFrame.grid(row=1, column=2, sticky='n')
button1 = tkinter.Button(rightFrame, text="Button 1")
button2 = tkinter.Button(rightFrame, text="Button 2")
button3 = tkinter.Button(rightFrame, text="Button 3")

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configuring the column
mainwindow.columnconfigure(0, weight=1)
mainwindow.columnconfigure(1, weight=1)
mainwindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief="sunken", borderwidth=1)
rightFrame.config(relief="sunken", borderwidth=1)
leftFrame.grid(sticky="ns")
rightFrame.grid(sticky="new")

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')

mainwindow.mainloop()
