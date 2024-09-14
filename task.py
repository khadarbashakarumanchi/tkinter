from tkinter import * 
root = Tk() 
root.title("Counter") 
root.geometry("700x500")

i = 0

def val():
    global i 
    i = i + 1 
    l1.config(text=f"Counter : {i}")
    
        
l1 = Label(root,text="Counter:{0}", 
           font = "Helvetica 20 bold", 
           bg = "yellow",
           fg="red", 
           padx=14, 
           pady=22 ,relief=SUNKEN )
l1.pack()

btn1 = Button(root , command=val , text="Onclick" , relief=SUNKEN)
btn1.pack(pady=88)
root.mainloop()