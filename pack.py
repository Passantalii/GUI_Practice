from tkinter import *
root = Tk()
root.geometry("800x500")
root.title("Pack Options")

fr1 = Frame(root)
btn1 = Button(fr1, text= "button1")

fr2 = Frame(root)
btn2 = Button(fr2, text= "button2")

fr3 = Frame(root)
btn3 = Button(fr3, text= "button3")

fr4 = Frame(root)
btn4 = Button(fr4, text= "button4")

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()



#fr1.pack(side= TOP)
#fr2.pack(side= BOTTOM)
#fr3.pack(side= LEFT)
#fr4.pack(side= RIGHT)

fr1.grid(column=1, row=1)
fr2.grid(column=2, row=1)
fr3.grid(column=3, row=1)
fr4.grid(column=4, row=1)

root.mainloop()