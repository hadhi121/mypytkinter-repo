from tkinter import *

window = Tk()
window.title('MY FIRST GUI PROGRAM')
window.geometry('400x400')


label_photo = PhotoImage(file='meme.png')
label = Label(window,
              text='I AM A PYTHON MASTER',
              font=('arial',20,'bold'),
              fg = "#4ce21a",
              bg = 'black',
              relief=RAISED,#border
              bd=5,#border width
              padx=15,#gap b/w border in x axis
              pady=10,#      ''       in y axis
              image=label_photo,
              compound='bottom')#image and text separating
label.pack()

new_icon = PhotoImage(file='tk.png')
window.iconphoto(True,new_icon)

window.config(background = "#760303")

window.mainloop()