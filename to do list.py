from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('Red light, Green light - Task Manager!')
root.iconbitmap('c:/gui/Red light, Green light.ico')
root.geometry("500x500")

#Define our Font
my_font = Font(family="Baskerville Old Face", size=30, weight="bold")

#Create Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#Create listbox
my_list = Listbox(my_frame, font=my_font, width=25, height=5, bg="SystemButtonFace", bd=0, fg="#464646")

my_list.pack()

#Create dummy list
stuff = ["Walk the dog", "Buy groceries", "Take a nap", "Learn Tkinter"]
#Add dummy list to list box
for item in stuff:
    my_list.insert(END, item)
root.mainloop()
