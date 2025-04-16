from tkinter import *
root = Tk()
root.geometry("800x500")
root.title("Place")

btn1 = Button(root, text= "Button1")
btn1.pack()
btn1.place(anchor= NW, width= 100,height= 80, bordermode= OUTSIDE)

root.mainloop()