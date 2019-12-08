from tkinter import *
import webbrowser

def openCodeIn():
    url_1 ='https://codein.withgoogle.com/dashboard/'
    webbrowser.open_new_tab(url_1)

root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button_1 = Button(topFrame, text='Open', fg='Purple',background='grey', activebackground='black', command=openCodeIn)
button_2 = Button(topFrame, text='Button_2', fg='blue')
button_3 = Button(bottomFrame, text='Button_3', fg='green')
button_4 = Button(bottomFrame, text='Button_4', fg='yellow')

button_1.pack(side=LEFT)
button_2.pack(side=RIGHT)
button_3.pack(side=LEFT)
button_4.pack(side=RIGHT)

root.mainloop()
