from tkinter import * 
root = Tk() 
root.title("Canvas widgets")

canvas_height = 400 
canvas_width = 800 
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root,height=canvas_height,width=canvas_width)
can_widget.pack()
#coordinates (x , y1) to (x2 , y2)
can_widget.create_line(0 , 0 , 800 , 400 , fill = "red")
can_widget.create_line(0 , 400 , 800 , 0 , fill="red")
#to create a rectanle specify coordinate top_left to bottom_right
can_widget.create_rectangle(3, 5 , 700 , 300)
can_widget.create_text(200 , 200 , text="hello world")
can_widget.create_oval(344 , 333 ,214 , 310)
root.mainloop()