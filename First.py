from tkinter import *
root = Tk()
root.geometry("800x500")
root.title("Home")
def btn_print():
    name = txt1.get("1.0","end")
    lb1["text"] = name
    lb1["bg"] = "black"
    
fr1 = Frame(root, bg= "grey")
fr1.pack()

txt1 = Text(fr1, width="50", height="5", bg="green", fg="white", font="40")
txt1.pack()

btn1 = Button(fr1,command=btn_print, text = "click me", width = "50", height = "2", font = "30", bg="black", fg="white", padx=20, pady=50)
btn1.pack()

lb1 = Label(fr1, text="Click Me", width="50", height="5", bg="red", fg="white", font="40")
lb1.pack()


root.mainloop()
