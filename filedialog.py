from tkinter import *
from tkinter import filedialog

def openfile():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\Asharaf\\Desktop\\BROCODE_TKINTER\\file1.txt",
                                           title='hello tkinter is good',
                                           filetypes=(('text files','*.txt'),('all files','*.*')))
    print(file_path)#gives path
    file_open = open(file_path,'r')
    print(file_open.read())
    file_open.close()



window = Tk()


button = Button(window,text = 'open',command = openfile)
button.pack()
window.mainloop()