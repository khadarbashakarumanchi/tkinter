from tkinter import * 
import tkinter.messagebox as tmsg 

root = Tk()
root.geometry("700x500")
root.title("Sliders")

#slider_h = Scale(root , from_=0 , to=100)
#slider_h.pack()
def getdollars():
    print(f"we have credited{slider_v.get()} dollars to your account")
    tmsg.showinfo("amount credited" , f"we have credited{slider_v.get()} dollars to your account")

Label(root , text = "what do you need").pack()

slider_v = Scale(root , from_= 10 , to=100 , orient=HORIZONTAL , tickinterval=40)
slider_v.set(34)
slider_v.pack()
Button(root , text="get dollars!" ,pady=20, command = getdollars).pack()
root.mainloop()