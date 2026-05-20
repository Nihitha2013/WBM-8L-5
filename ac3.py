from tkinter import *

root=Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top=Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    l2=Label(top,text="This is toplevel window")
    l2.pack()

    top.mainloop()

l=Label(root, text="This is root window", fg="orange")
btn=Button(root, text="Click Me", fg="plum", command= topwin)

l.pack()
btn.pack()
root.mainloop()