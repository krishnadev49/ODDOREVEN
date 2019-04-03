import tkinter as tk
import threading
b = 0
def Draw(p):
    l=p
    frame=tk.Frame(root,width=100,height=100,relief='solid',bd=1)
    frame.place(x=10,y=10)
    text=tk.Label(frame,text=l)
    text.pack()

def Refresher():
    global b
    b=b+1
    Draw(b)
    threading.Timer(5, Refresher).start()
    
root=tk.Tk()
Refresher()
root.mainloop()