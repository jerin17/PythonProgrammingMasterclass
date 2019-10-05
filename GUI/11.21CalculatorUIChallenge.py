import tkinter

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)]]

mainwindow = tkinter.Tk()
mainwindow.title("Calculator")
mainwindow.geometry('640x480+400+200')
mainwindowpadding = 8
mainwindow['padx'] = mainwindowpadding

result = tkinter.Entry(mainwindow)
result.grid(row=0, column=0, sticky='nsew')

keypad = tkinter.Frame(mainwindow)
keypad.grid(row=1, column=0, sticky='nsew')

r = 0
for i in keys:
    c = 0
    for j in i:
        tkinter.Button(keypad, text=j[0], width=8, height=2).grid(row=r, column=c, columnspan=j[1], sticky=tkinter.E + tkinter.W)
        c += j[1]
    r += 1

mainwindow.update()
mainwindow.minsize(keypad.winfo_width() + mainwindowpadding, result.winfo_height() + keypad.winfo_height())
mainwindow.maxsize(keypad.winfo_width() + 50, result.winfo_height() + 50+ keypad.winfo_height())

mainwindow.mainloop()