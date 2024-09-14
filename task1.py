from tkinter import * 
root = Tk()
root.title("Task")
root.geometry("700x500")

def val():
    selected_value = var.get()
    if selected_value == 1:
        l1.config(text="python", fg="green")  
    elif selected_value == 2:
        l1.config(text="javaScript", fg="blue")  
    elif selected_value == 3:
        l1.config(text="Sql", fg="red")  
    else:
        l1.config(text="Invalid Selection")


l1 = Label(root , 
           text = "python , javaScript,Sql" ,
           font="Helvetica 24 bold",
           fg = "blue")
l1.pack() 

var = IntVar()

r1 = Radiobutton(root , text = "python" ,padx=14 , variable=var , value=1 , command = val)
r1.pack(anchor="w")
r2 = Radiobutton(root , text = "javaScript" ,padx=14 , variable=var , value=2 , command = val)
r2.pack(anchor="w")
r3 = Radiobutton(root , text = "Sql" ,padx=14 , variable=var , value=3 , command = val)
r3.pack(anchor="w")


root.mainloop() 
