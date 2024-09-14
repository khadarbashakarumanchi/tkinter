#packing buttons  

from tkinter import * 
root = Tk() 
root.geometry("500x300") 
def hello():
    print("Hello tkinter")


root.title("my application") 
frame = Frame(root , borderwidth=6 , bg = "grey", relief=SUNKEN )
frame.pack(side = LEFT , anchor = "nw")
btn1 = Button( frame , fg="red", text= "printnow" ,command = hello)
btn1.pack(side=LEFT , padx=23)
btn2 = Button( frame , fg="red", text= "printnow" , command = hello)
btn2.pack(side=LEFT , padx=23)
btn3 = Button( frame , fg="red", text= "printnow")
btn3.pack(side=LEFT , padx=23)
btn4 = Button( frame , fg="red", text= "printnow")
btn4.pack(side=LEFT , padx=23)
root.mainloop() 
