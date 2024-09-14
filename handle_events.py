from tkinter import * 
root = Tk() 
root.title("Events")
root.geometry("600x300")

def wels(e):
    print(f"you clicked {e.x} , {e.y}")
    
widget = Button(root , text="click me")
widget.pack()

widget.bind("<Button-1>" , wels)
widget.bind("<Double-Button-1>" , quit)
root.mainloop()


#<Button-1>: Left mouse button click.
#<Button-2>: Middle mouse button click.
#<Button-3>: Right mouse button click.
#<Double-Button-1>: Double-click left mouse button.
#<B1-Motion>: Mouse drag while holding left mouse button.
#Keyboard Events:

#<Key>: Any key press.
#<KeyPress-A>: Pressing the "A" key.
#<Return>: Pressing the "Enter" key.
#<Escape>: Pressing the "Esc" key.
#Window Events:

#<Configure>: Event for window resizing.
#<FocusIn>: When a widget gains focus.
#<FocusOut>: When a widget loses focus.
