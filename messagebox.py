from tkinter import *
from tkinter import messagebox #import messagebox library

def click():
    #messagebox.showinfo(title='IMPORTANT INFORMATION',message='YOU ARE A GREAT PERSON')
    #messagebox.showwarning(title='WARNING!',message='YOU HAVE A VIRUS!!!!')
    #messagebox.showerror(title='ERROR 404!',message='something went wrong :(')

    '''if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do take premium?'):
        print('You taken premium!')
    else:
        print('You canceled premium!')'''

    #if messagebox.askretrycancel(title='ask retry cancel',message='Do you want retry the thing?'):
        #print('You retried a thing!')
    #else:
        #print('You canceled a thing! :(')

    #if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
        #print('wow i like cake too')
    #else:
        #print('Why do you not like cake? :(')

    '''answer = messagebox.askquestion(title='ask question',message='Do you like coding?')
    if(answer == 'yes'):
        print('I like coding too :)')
    else:
        print('Why do you not like coding?')'''

    answer = messagebox.askyesnocancel(title=' Yes no cancel',message='Do you like to code?',icon='question')
    if answer == True:
        print("You like to code :)")
    elif answer==False:
        print("Then why are you watching a video on coding?")
    else:
        print("You have dodged the question ")


window = Tk()
button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()

