from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title('Red light, Green light - Task Manager!')
root.iconbitmap('c:/gui/Red light, Green light.ico')
root.geometry("550x600")

# Define our Font
my_font = Font(family="Brush Script MT", size=30)

# Create Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# Create listbox
my_list = Listbox(my_frame, font=my_font,
                 width=30, 
                 height=8,
                 bg="SystemButtonFace",
                 bd=0, 
                 fg="#000000", 
                 highlightthickness=0, 
                 selectbackground="#a6a6a6",
                 activestyle="none")

my_list.pack(side=LEFT, fill=BOTH)

# Create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# Create entry box to add items to the list
my_entry = Entry(root, font=("Helvetica", 24), width= 30)
my_entry.pack(pady= 20)

# Create a button frame
button_frame = Frame(root)
button_frame.pack(pady= 20)


# Button Functions
def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)
def cross_off_item():
    #Cross off item
    my_list.itemconfig(my_list.curselection(), fg="#A3A3A3")
    #Get rid of selection bar entry
    my_list.selection_clear(0,END)
def uncross_item():
    #Cross off item
    my_list.itemconfig(my_list.curselection(), fg="#000000")
    #Get rid of selection bar entry
    my_list.selection_clear(0,END)
def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#A3A3A3":
            my_list.delete(my_list.index(count))
        else:
             count += 1

# Menu Functions
def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/gui/data",
        title="Save File",
        filetypes=(
            ("Dat Files","*.dat"),
            ("All Files","*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

        # Delete crossed off items before saving
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#A3A3A3":
                my_list.delete(my_list.index(count))
            else:
                count += 1

        # Grab all stuff form list
        stuff = my_list.get(0, END)

        #Open file
        output_file = open(file_name, 'wb')

        # Actaully add stuff to the file
        pickle.dump(stuff, output_file)
def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="C:/gui/data",
        title="Open File",
        filetypes=(
            ("Dat Files","*.dat"),
            ("All Files","*.*")))
    if file_name:
        # Delete currently open list
        my_list.delete(0, END)
        # Open the file
        input_file = open(file_name, 'rb')
        # load data from file
        stuff = pickle.load(input_file)
        # Output stuff to screen
        for item in stuff:
            my_list.insert(END, item)
def clear_list():
    my_list.delete(0, END)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
# Add dropdown items
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=clear_list)


# Add buttons to frame
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)
delete_crossed_button = Button(button_frame, text="Delete Crossed", command=delete_crossed)
red_button = Button(button_frame, text="Red Light", command=red_item)
orange_button = Button(button_frame, text="Orange Light", command=orange_item)
green_button = Button(button_frame, text="Green Light", command=green_item)

# Add measurements of buttons
delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=1, column=0)
red_button.grid(row=1, column=1, padx=20)
orange_button.grid(row=1, column=2)
green_button.grid(row=1, column=3, padx=20)

root.mainloop()
