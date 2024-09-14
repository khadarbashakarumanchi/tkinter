from tkinter import * 
import tkinter.messagebox as tmsg 

root = Tk()
root.title("Radio Button")
root.geometry("700x300") 
def order():
    tmsg.showinfo("food is ready" , f"we recieved your order for {var.get()} thanks for ordering")

var = StringVar()
var.set("radio")

Label(root , 
      text="what would you like ?",
      justify=LEFT, 
      font = "lucida 26 bold" , 
      padx=14).pack()

radio1 = Radiobutton(root , text = "idly" ,padx=14 , variable=var , value=1).pack(anchor="w")
radio2 = Radiobutton(root , text = "dosa" ,padx=14 , variable=var , value=2).pack(anchor="w")
radio3 = Radiobutton(root , text = "puri" ,padx=14 , variable=var , value=3).pack(anchor="w")
radio4 = Radiobutton(root , text = "vada" ,padx=14 , variable=var , value=4).pack(anchor="w")

Button(text="Order Now" , command=order).pack()
root.mainloop()