from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("message box")
root.geometry("700x300")
def myfun():
    print("welcome")
def msg():
    print("get ready")
    a = tmsg.showinfo("msg box of GUI")
def rate():
    print("rate us")
    val = tmsg.askquestion("ask you exp?" ,"how was your exp")
    
    if val == "yes":
        msg1 = "Great , rate us on play store"
    else:
        msg1 = "sorry for inconvinience , we will look into it"
    tmsg.showinfo("Experience" , msg1)

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


mainmenu.add_cascade( label="Edit",menu=m2)

m3 = Menu(mainmenu , tearoff=0)
m3.add_command(label="fix" , command=msg)
m3.add_command(label="run" , command=msg )
m3.add_command(label="Rate us" , command=rate )

mainmenu.add_cascade(label="Help" , menu=m3)

root.config(menu=mainmenu)

root.mainloop()