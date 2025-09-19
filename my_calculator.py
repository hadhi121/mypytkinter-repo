from tkinter import *

window = Tk()
window.title('MY FIRST CALCULATOR PROGRAM')
window.geometry('500x500')

def button_press(num):
    global equation_text

    equation_text += str(num)
    equation_label.set(equation_text)

def equals():
   global equation_text
   try:
        answer = str(eval(equation_text))
        equation_label.set(answer)
        equation_text = answer
   except ZeroDivisionError:
       equation_label.set('Arithmetic Error')
       equation_text = ''

   except SyntaxError:
       equation_label.set('Syntax Error')
       equation_text = ''

def clear():
    global equation_text

    equation_label.set('')
    equation_text = ''

equation_text = ''

equation_label = StringVar()

label = Label(window,
              textvariable = equation_label,
              font=('aerial',18,'bold'),bg='white',
              width = 24,height = 2)
label.pack()

frame = Frame(window)
frame.pack()

button1 =Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1),
                fg="#000000",bg="#5D5B5A",
                activebackground="#010617",
              activeforeground='#1C25D7')
button1.grid(row=0,column=0)

button2 =Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2),
                fg="#000000",bg="#5D5B5A",
                activebackground="#010617",
              activeforeground='#1C25D7')
button2.grid(row=0,column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3),
                fg="#000000",bg="#5D5B5A",
                activebackground="#010617",
              activeforeground='#1C25D7')
button3.grid(row=0,column=2)

button4 = Button(frame,text =4,height =4,width = 9,font =35,
                 command = lambda:button_press(4),
                 fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
button4.grid(row=1,column=0)

button5 = Button(frame,text = 5,height = 4,width = 9,font =35,
                 command = lambda:button_press(5),
                 fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
button5.grid(row=1,column=1)

button6 = Button(frame,text = 6,height = 4,width = 9,
                 font =35,
                 command = lambda:button_press(6),
                 fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
button6.grid(row=1,column=2)

button7 = Button(frame,text = 7,height = 4,width = 9,font =35,
                 command = lambda:button_press(7),
                fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
button7.grid(row=2,column=0)

button8 = Button(frame,text = 8,height = 4,width = 9,font =35,
                 command = lambda:button_press(8),
                 fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
button8.grid(row=2,column=1)

button9 = Button(frame,text = 9,height = 4,width = 9,font =35,
                 command = lambda:button_press(9),
                 fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
button9.grid(row=2,column=2)

button0 = Button(frame,text = 0,height = 4,width = 9,font =35,
                 command = lambda:button_press(0),
                 fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
button0.grid(row=3,column=0)

plus = Button(frame,text = '+',height = 4,width = 9,font =35,
                 command = lambda:button_press('+'),
                 fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
plus.grid(row=0,column=3)

minus = Button(frame,text = '-',height = 4,width = 9,font =35,
                 command = lambda:button_press('-'),
                 fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
minus.grid(row=1,column=3)

multiply = Button(frame,text = '*',height = 4,width = 9,font =35,
                 command = lambda:button_press('*'),
                 fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
multiply.grid(row=2,column=3)

divide = Button(frame,text = '/',height = 4,width = 9,font =35,
                 command = lambda:button_press('/'),
                 fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
divide.grid(row=3,column=3)

equal = Button(frame,text = '=',height = 4,width = 9,font =35,
                 command = equals,
                 fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
equal.grid(row=3,column=2)

decimal = Button(frame,text = '.',height = 4,width = 9,font =35,
                 command = lambda:button_press('.'),
                 fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
decimal.grid(row=3,column=1)

clear = Button(window,text = 'CLEAR',height = 4,width = 40,font =35,
                 command = clear,
                 fg="#000000",bg="#5D5B5A",
                 activebackground="#010617",
              activeforeground='#1C25D7')
clear.pack()




new_icon = PhotoImage(file='tk.png')
window.iconphoto(True,new_icon)
window.mainloop()