from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('MY QUIZ PROGRAM')
window.geometry('400x300')

def check_answer(selected_option):
    global score,question_index
    correct_answer = questions[question_index][2]

    if selected_option == correct_answer:
        messagebox.showinfo('RESULT','CORRECT ANSWER')
        score+=1
    else:
        messagebox.showerror('RESULT',f'INCORRECT ANSWER \nCORRECT ANSWER IS {correct_answer}.')

    question_index+=1
    

    if question_index < len(questions):
            load_question()
    else:
            show_result()


def load_question():
     q_text,q_options,_ = questions[question_index]
     question_label.config(text=q_text)

     option1.config(text=q_options[0],command=lambda :check_answer(q_options[0]))
     option2.config(text=q_options[1],command=lambda :check_answer(q_options[1]))
     option3.config(text=q_options[2],command=lambda :check_answer(q_options[2]))



def show_result():
    percentage = (score/len(questions)) * 100
    messagebox.showinfo('RESULT',f'YOU GOT {score}/{len(questions)} MARKS IN THIS TEST.\n YOU ACHIEVED {percentage:.2f}% IN THIS TEST.')
    window.destroy()


questions = [
    ["What does CPU stand for?", 
     ["Central Processing Unit", "Computer Personal Unit", "Control Processing Utility"], 
     "Central Processing Unit"],

    ["What does GPU stand for?", 
     ["Graphical Processing Utility", "Gaming Processor Unit","Graphics Processing Unit"], 
     "Graphics Processing Unit"],

    ["What does RAM stand for?", 
     ["Read And Modify","Random Access Memory", "Run Access Module"], 
     "Random Access Memory"]
]
             

#global variables 
score = 0 
question_index = 0


#GUI
welcome_label1 = Label(window,text='WELCOME TO MY QUIZ GAME',font=('arial',15,'bold'))
welcome_label1.pack(pady=10)


question_label = Label(window,text = '',
                       font = ('arial',14,'bold'))
question_label.pack(pady=10)

option1 = Button(window,text='',font=('arial',10),width=30)
option1.pack(pady=5)
option2 = Button(window,text='',font=('arial',10),width=30)
option2.pack(pady=5)
option3 = Button(window,text='',font=('arial',10),width=30)
option3.pack(pady=5)

load_question()#start the quiz

window.config(background="#00ff9d")
window.mainloop()
