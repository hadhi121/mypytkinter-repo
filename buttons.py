from tkinter import *

window = Tk()
window.title('MY FIRST GUI PROGRAM')
window.geometry('400x400')

count = 0
def click():
    global count 
    count += 1
    label.config(text = count)

button = Button(window,text='click me!!')
button.config(command=click)
button.config(font=('ink free',50,'bold','italic'))
button.config(fg='#e7f20a',bg="#f25f0a")
button.config(activebackground="#0a40f2",
              activeforeground='#e7f20a')

cursor = PhotoImage(file='cursor.png')
button.config(image=cursor)
button.config(compound='bottom')
#button.config(state='active') or u can disable
button.pack()

label = Label(window,text = count)
label.config(font=('monospace',50))
label.pack()



window.mainloop()



'''meme_image = PhotoImage(file='meme.png')
label=Label(window)
label.config(image=meme_image)
label.pack()'''