from tkinter import *
root = Tk()
root.geometry("800x500")
root.title("Welcome")

#def hello():
    #print("Hello World")

rdbtn1 = Radiobutton(root, text= "Male", value=1)
rdbtn1.pack()
rdbtn2 = Radiobutton(root, text= "Female", value=2)
rdbtn2.pack()
#checkbtn = Checkbutton(root, text = "Auto Save", font= 14, command= hello, state= DISABLED, onvalue= 1, offvalue= 0)
#checkbtn.pack()

#lbfr1 = LabelFrame(root, text="This is a label frame")
#lbfr1.pack(expand= "yes", fill= "both")
#lb1 = Label(lbfr1, text= "This is a label")
#lb1.pack()

root.mainloop()