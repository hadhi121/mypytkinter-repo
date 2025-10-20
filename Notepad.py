from tkinter import *
from tkinter import Menu
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, END))


def open_file():
    file = filedialog.askopenfilename(defaultextension="*.txt",
                                      filetypes=[('Text files','*.txt'),
                                                 ('All files','*.*')])
    if file != '':#or u can write if file
        with open(file,'r') as f:
            text_area.delete(1.0,END)
            text_area.insert(1.0,f.read())

def new_file():
    text_area.delete('1.0',END)


#main window
window = Tk()
window.geometry('600x400')
window.title('Simple notepad')

# text area
text_area = Text(window,bg="#EFDF51",font=('ink free',15,'bold'))
text_area.pack()

#menu bar
menu_bar = Menu(window)



#sub_menu
file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label='New',command=new_file)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=window.destroy)


menu_bar.add_cascade(label='FILE',menu=file_menu)#sub menu assings to menu_bar
menu_bar.add_command(label='EDIT')
menu_bar.add_command(label='HELP')







#attach menu to window
window.config(menu=menu_bar)
window.mainloop()
