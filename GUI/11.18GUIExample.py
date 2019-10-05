import tkinter
import os
mainwindow = tkinter.Tk()
mainwindow.title("Grid Demo Layout")
mainwindow.geometry("640x480-8-200")
mainwindow['padx'] = 10

label = tkinter.Label(mainwindow, text='Tkinter Grid Demo')
label.grid(row=0, column=0, columnspan=3)

mainwindow.columnconfigure(0, weight=1)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=3)
mainwindow.columnconfigure(3, weight=3)
mainwindow.columnconfigure(4, weight=3)
mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=10)
mainwindow.rowconfigure(2, weight=1)
mainwindow.rowconfigure(3, weight=3)
mainwindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainwindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for i in os.listdir('/Windows/System32'):
    fileList.insert(tkinter.END, i)

listScroll = tkinter.Scrollbar(mainwindow, orient=tkinter.VERTICAL, command=fileList.yview())
listScroll.grid(row=1, column=1, sticky="nsw", rowspan=2)
fileList['yscrollcommand'] = listScroll.set

# Frame for radio Button
optionFrame = tkinter.LabelFrame(mainwindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(3)

# radio Button
r1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
r2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
r3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)

r1.grid(row=0, column=0, sticky='w')
r2.grid(row=1, column=0, sticky='w')
r3.grid(row=2, column=0, sticky='w')

# widget to display result
resultLabel = tkinter.Label(mainwindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')

result = tkinter.Entry(mainwindow)
result.grid(row=2, column=2, sticky='sw')


# frame for time spinners
timeFrame = tkinter.LabelFrame(mainwindow, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')

# Spinner
hh = tkinter.Spinbox(timeFrame, width=2, value=tuple(range(0, 24)))
mm = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
ss = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hh.grid(row=0, column=0)
tkinter.Label(timeFrame, text=' : ').grid(row=0, column=1)
mm.grid(row=0, column=2)
tkinter.Label(timeFrame, text=' : ').grid(row=0, column=3)
ss.grid(row=0, column=4)
timeFrame['padx'] = 36


# frame for date spinners
dateFrame = tkinter.LabelFrame(mainwindow, text='Date')
dateFrame.grid(row=4, column=0, sticky='new')

ddlabel = tkinter.Label(dateFrame, text='Day')
mmlabel = tkinter.Label(dateFrame, text='Month')
yylabel = tkinter.Label(dateFrame, text='Year')

ddlabel.grid(row=0, column=0, sticky='w')
mmlabel.grid(row=0, column=1, sticky='w')
yylabel.grid(row=0, column=2, sticky='w')

# spinners
dd = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
mm = tkinter.Spinbox(dateFrame, width=5, value=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
yy = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)

dd.grid(row=1, column=0)
mm.grid(row=1, column=1)
yy.grid(row=1, column=2)
dateFrame['padx']=36

# OK button
ok = tkinter.Button(mainwindow, text='OK', width=3)
ok.grid(row=4, column=3, sticky='e')

# Cancel button
cancel = tkinter.Button(mainwindow, text='Cancel', width=8, command=mainwindow.destroy)
cancel.grid(row=4, column=4)

mainwindow.mainloop()
print(rbValue.get())