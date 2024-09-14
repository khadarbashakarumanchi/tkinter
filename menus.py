from tkinter import * 
root = Tk() 
root.title("Menus") 
root.geometry("700x300")

def myfun():
    print("welcome")

#plain menu with out drop down
#(menu_a = Menu(root)
#menu_a.add_command(label="file" , command=myfun)
#menu_a.add_command(label="quit" , command=quit)
#root.config() 

mainmenu = Menu(root)

m1 = Menu(mainmenu , tearoff=0)
m1.add_command(label="New project" , command=myfun)
m1.add_command(label="Save" , command=myfun)
m1.add_command(label="save as" , command=myfun)
m1.add_command(label="print" , command=myfun)
#root.config(menu=m1)

mainmenu.add_cascade( label="File",menu=m1)

#mainmenu = Menu(root)
m2 = Menu(mainmenu , tearoff=0)
m2.add_command(label="cut" , command=myfun)
m2.add_command(label="copy" , command=myfun)
m2.add_command(label="extract" , command=myfun)
m2.add_command(label="export" , command=myfun)
root.config(menu=mainmenu)

mainmenu.add_cascade( label="Edit",menu=m2)


root.mainloop()

