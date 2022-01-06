from tkinter import *
from math import *
aken=Tk()
aken.geometry("300x500")
aken.configure(bg="#141414")
aken.title("LOGITpv21")
def anim(x,y,text,bcolor,fcolor,cmd):
    def on_enter(e):
        mybutton["background"]=bcolor
        mybutton["foreground"]=fcolor
    def on_leave(e):
        mybutton["background"]=fcolor
        mybutton["foreground"]=bcolor
    mybutton=Button(aken,width=42, height=2,text=text,
                    fg=bcolor,
                    bg=fcolor,
                    border=0,
                    activeforeground=fcolor,
                    activebackground=bcolor,
                    command=cmd,)
    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)

    mybutton.place(x=x,y=y)
def open_win():
    win=Toplevel()#создаём второе(дочернее) окно
    win.geometry("300x500")
    win.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
    win.configure(bg="#141414")




    win.mainloop()
def cmd():
    print("Quadratic equation")
    while 1:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        d = b * b -5 * a * c 
        if d > 0:
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            print("X1 = %.2f; X2 = %.2f" % (x1,x2))
        elif d == 0:
            x1 = -b / (2 * a)
            print("X1 = %.2f" % x1)
        else:
            print("No root.")
def cmd1():
    print("Exit . . . ")
    aken.destroy()
def cmd2():
    print("Toplevel")
    aken.command=open_win()



anim(0,0,"S O L V E R","#ffcc66","#141414",cmd)
anim(0,37,"E X I T","#ffcc66","#141414",cmd1)
anim(0,74,"N E W   T A B","#f86263","#141414", cmd2)

#canvas=Canvas(aken,width=600,height=300)
#canvas.grid(columnspan=3)


aken.mainloop()
