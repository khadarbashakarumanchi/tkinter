#Entry widget and grid layout in tkinter  cells
from tkinter import * 
root = Tk() 
root.geometry("700x300") 

def getvals():
    print(f"user value is {uservalue.get()}")
    print(f"user value is {passvalue.get()}")
    
    
user = Label(root ,text="Username")
user.grid(row=0,column=0)

password = Label(root , text = "Password")
password.grid(row=1 , column=0)
#variable classes in tkinter 
#BooleanVar,IntVar,DoubleVar,StringVar
uservalue = StringVar() 
passvalue = StringVar() 

e1 = Entry(root , textvariable=uservalue) 
e1.grid(row=0 , column=1)
e2 = Entry(root , textvariable=passvalue)
e2.grid(row=1 , column=1)
btn1 = Button(text="Submit",command = getvals).grid()

root.mainloop()