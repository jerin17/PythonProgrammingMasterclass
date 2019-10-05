try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import tkinter
print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()


mainWindow = tkinter.Tk()

mainWindow.title("Hello World !")
mainWindow.geometry("640x480+500+0")
mainWindow.mainloop()
