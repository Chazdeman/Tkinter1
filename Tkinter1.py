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


anim(0,0,"S O L V E R","#ffcc66","#141414",cmd)
anim(0,37,"E X I T","#ffcc66","#141414",cmd1)

aken.mainloop()