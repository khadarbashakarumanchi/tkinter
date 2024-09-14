from tkinter import *

root = Tk()
root.geometry("700x500")
root.title("Scrollbar")

# Create a Scrollbar widget
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create a Listbox and link it to the scrollbar
lbx = Listbox(root, yscrollcommand=scrollbar.set)

# Insert items into the Listbox
for i in range(400):
    lbx.insert(END, f"Item {i}")

# Pack the Listbox to fill both x and y space
lbx.pack(fill=BOTH, padx=24)

# Configure the scrollbar to control the Listbox
scrollbar.config(command=lbx.yview)

root.mainloop()
