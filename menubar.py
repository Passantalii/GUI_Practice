from tkinter import *
root = Tk()
root.title("Home")

def donothing():
    filewin = Toplevel(root)
    button = Button(root, text= "Do Nothing Button")
    button.pack()


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label= "New", command= donothing)
filemenu.add_command(label= "Open", command= donothing)
filemenu.add_command(label= "Save", command= donothing)
filemenu.add_command(label= "Save As...", command= donothing)
filemenu.add_command(label= "Close", command= donothing)

filemenu.add_separator()

filemenu.add_command(label= "Exit", command= donothing)
menubar.add_cascade(label= "File", menu= filemenu)
editmenu = Menu(menubar, tearoff= 0)
editmenu.add_command(label= "Undo", command= donothing)

editmenu.add_separator()

editmenu.add_command(label= "Cut",command= donothing)
editmenu.add_command(label= "Copy",command= donothing)
editmenu.add_command(label= "Paste",command= donothing)
editmenu.add_command(label= "Delete",command= donothing)
editmenu.add_command(label= "Select All",command= donothing)

menubar.add_cascade(label= "Edit", menu= editmenu)
helpmenu = Menu(menubar, tearoff= 0)
helpmenu.add_command(label= "Help Index",command= donothing)
helpmenu.add_command(label= "About...",command= donothing)
menubar.add_cascade(label= "Help", menu= helpmenu)

root.config(menu= menubar)
root.mainloop()