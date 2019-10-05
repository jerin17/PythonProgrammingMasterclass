import tkinter

mainwindow = tkinter.Tk()

mainwindow.title("Pack Geometry Manager")
mainwindow.geometry("640x480+0+0")

l = tkinter.Label(mainwindow, text="Hello World !!")
l.pack(side='top')

# canvas = tkinter.Canvas(mainwindow, relief="raised", borderwidth=2)
# canvas.pack(side='left')
# canvas.pack(side="left", fill=tkinter.Y)
# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)
# canvas.pack(side="left", fill=tkinter.X, expand=True)

leftFrame = tkinter.Frame(mainwindow)
leftFrame.pack(side="left", anchor='n', fill=tkinter.Y, expand=False)
canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=2)
canvas.pack(side='top')

rightFrame = tkinter.Frame(mainwindow)
rightFrame.pack(side="right", anchor="n", expan=True)
button1 = tkinter.Button(rightFrame, text="Button 1")
button2 = tkinter.Button(rightFrame, text="Button 2")
button3 = tkinter.Button(rightFrame, text="Button 3")

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')



mainwindow.mainloop()
