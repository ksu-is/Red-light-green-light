from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('Red light, Green light - Task Manager!')
root.iconbitmap('c:/gui/Red light, Green light.ico')
root.geometry("500x500")

#Define our Font
my_font = Font(family="Brush Script MT", size=30)

#Create Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#Create listbox
my_list = Listbox(my_frame, font=my_font,
                 width=25, 
                 height=5,
                 bg="SystemButtonFace",
                 bd=0, 
                 fg="#464646", 
                 highlightthickness=0, 
                 selectbackground="#a6a6a6",
                 activestyle="none")

my_list.pack(side=LEFT, fill=BOTH)

#Create dummy list
stuff = ["Walk the dog", "Buy groceries", "Take a nap", "Learn Tkinter"]
#Add dummy list to list box
for item in stuff:
    my_list.insert(END, item)

#Create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

#Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)


root.mainloop()
