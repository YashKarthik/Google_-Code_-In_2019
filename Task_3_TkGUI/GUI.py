from tkinter import *
import webbrowser
from tkinter.filedialog import askopenfile
from tkinter import filedialog
import os
import subprocess



def openCodeIn():
    url_1 ='https://codein.withgoogle.com/dashboard/'
    webbrowser.open_new_tab(url_1)
def openFinder():
    rep = filedialog.askopenfilenames(
    	parent=root,
    	initialdir='/',
    	initialfile='Macintosh HD',
    	filetypes=[
    		("All files", "*"),
    		("JPEG", "*.jpg"),
    		("All files", "*")])
def openGitHubDesk():
	subprocess.call('/Applications/GitHub Desktop.app')
def openVsCode():
    subprocess.call('/Applications/Visual Studio Code.app')
   
    
root = Tk()
root.configure(background='#808080')

label_ = Label(text="Hey, I'm Jarvis, here to help you get around with you everyday tasks.😃", fg='black', font='Helvetica 18 bold', bg='#808080')
label__= Label(text='Most Used:', fg='black', bg='#808080', font='Helvetica 18 bold')
label_1 = Label(text="Check for updates on you Google Code In Dashboard.", fg='purple', bg='#808080')
button_1 = Button(text='Dashboard', fg='black',command=openCodeIn, highlightbackground='#a9a9a9')
label_2 = Label(text="Manage files with Finder/Github Desktop", fg='purple', bg='#808080')
button_2 = Button(text='Finder', fg='black', command=openFinder, highlightbackground='#a9a9a9')
button__2 = Button(text='GitH.Deskt', fg='black', command=openGitHubDesk, highlightbackground='#a9a9a9')
label_3 = Label(text='Tackle code with VsCode', fg='purple', bg='#808080')
button_3 = Button(text='VsCode', fg='black', command=openVsCode, highlightbackground='#a9a9a9')

button_1.configure(background='#808080')

label_.grid(row=0)
label__.grid(row=2, column=0, sticky=W)
label_1.grid(row=2, column=0, sticky=E)
button_1.grid(row=2, column=1, sticky=W)
label_2.grid(row=3, column=0, sticky=E)
button_2.grid(row=3, column=1, sticky=W)
button__2.grid(row=3, column=2, sticky=W)
label_3.grid(row=4, column=0, sticky=E)
button_3.grid(row=4, column=1, sticky=W)


root.mainloop()
