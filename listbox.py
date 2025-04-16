from tkinter import *
root = Tk()
root.geometry("800x500")
root.title("Listbox")

lb1 = Listbox(root)
lb1.insert(1, "OP1")
lb1.insert(2, "OP2")
lb1.insert(3, "OP3")
lb1.insert(4, "OP4")
lb1.insert(5, "OP5")
lb1.pack()

def checklb():
    strcheck = lb1.get(ACTIVE)
    if strcheck == "OP1":
        print("1")
    elif strcheck == "OP2":
        print("2")
    elif strcheck == "OP3":
        print("3")
    elif strcheck == "OP4":
        print("4")
    elif strcheck == "OP5":
        print("5")

btn1 = Button(root, text= "Check", command= checklb)
btn1.pack()

root.mainloop()