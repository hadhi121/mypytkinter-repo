from tkinter import *

window = Tk()
window.title('MY FIRST GUI PROGRAM')

def delete():
    entry.delete(2,END)#deletes the line of text

def backspace():
    entry.delete(len(entry.get())-1,END)#if letter has 10 letter then it will start from 9

def getit():
    username = entry.get()
    print(f'hello {username}')

submitbutton = Button(window,text='submit',command = getit)
submitbutton.pack(side='right')

delete = Button(window,text='delete',command = delete)
delete.pack(side='right')

backspace = Button(window,text='backspace',command = backspace)
backspace.pack(side='right')

entry = Entry()
entry.config(font=('ink free',20,'bold'))
entry.config(bg="#111111")
entry.config(fg="#00FF00")
#entry.insert(0,'spongebob')
#entry.config(show='*')
#entry.config(state=DISABLED)

entry.pack()

window.mainloop()