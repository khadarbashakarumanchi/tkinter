from tkinter import * 
import tkinter.messagebox as tmsg 

def add():
    global i 
    lbx.insert(END, f"Item {i}")  # Use END to append items to the end of the list
    i += 1 

i = 1  # Start with i = 1 since the first item is already added
root = Tk()
root.title("ListBox")
root.geometry("700x500") 

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of list box")  # Insert the first item

# Button to add more items to the Listbox
btn = Button(root, text="Add Item", command=add)
btn.pack(pady=10)

root.mainloop()
