from tkinter import * 
root = Tk() 
root.title("Travel form") 
root.geometry("700x300")

def getvals():
    print("form working")
    print(f"{nameval.get(),phoneval.get(),genval.get(),conval.get(),payval.get()}") 
    
#heading
Label(root, font = ("comicsansns" , 12 , "bold" ) , text = "Holmes travels" , pady=15).grid(row=0 , column=4)
#side names
name = Label(root , text = "username")
phone = Label(root , text="Phone")
gender = Label(root , text="Gender")
con = Label(root , text="contact")
pay = Label(root , text="pyment")

#packing 
name.grid(row=1 , column= 2)
phone.grid(row=2 , column=2)
gender.grid(row=3 , column=2)
con.grid(row= 4, column=2)
pay.grid(row=5 , column=2) 

nameval = StringVar() 
phoneval = StringVar() 
genval = StringVar() 
conval = StringVar() 
payval = StringVar()
foodservice = IntVar()
#box to enter value
e1 = Entry(root,textvariable=nameval).grid(row=1 , column=4)
e2 = Entry(root,textvariable=phoneval).grid(row= 2, column=4)
e3 = Entry(root,textvariable=genval).grid(row= 3, column=4)
e4 = Entry(root,textvariable=conval).grid(row=4 , column=4)
e5 = Entry(root,textvariable=payval).grid(row= 5, column=4)

foodservice = Checkbutton(text = "book your meals" , variable=foodservice)
foodservice.grid(row=6,column=4)
Button(text="submit to holmes travels" , command=getvals).grid(row=7,column=4)
root.mainloop()