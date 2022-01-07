from tkinter import *
from math import *
global a,b,c, D
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
    def lahenda():
        if (a.get()!=" " and b.get()!=" " and c.get()!=" "):
            a_=float(a.get())
            b_=float(b.get())
            c_=float(c.get())
            D=b_*b_-4*a_*c_
            if D>0:
                x1_=round((-1*b_+sqrt(D))/(2*a_),2)
                x2_=round((-1*b_-sqrt(D))/(2*a_),2)
                t=f"x1={x1_}, \nx2={x2_}"
                graf=True
            elif D==0:
                x1_=round((-1*b_)/(2*a_),2)
                t=f"x1={x1_}"
                graf=True
            else:
                t="No root."
                graf=False
            vastus.configure(text=f"D={D}\n{t}")
            a.configure(bg="#f86263")
            b.configure(bg="#f86263")
            c.configure(bg="#f86263")
        else:
            if a.get()=="":
                a.configure(bg="#de7879")
            if b.get()=="":
                b.configure(bg="#de7879")
            if c.get()=="":
                c.configure(bg="#de7879")
        return graf,D,t
    def graafik():
        flag,D,t=lahenda()
        if flag==True:
            a_=int(a.get())
            b_=int(b.get())
            c_=int(c.get())
            x0=(-b_)/(2*a_)
            y0=a_*x0*x0+b_*x0+c_
            x = np.arange(x0-10, x0+10, 0.5)#min max step
            y=a_*x*x+b_*x+c_
            fig = plt.figure()
            plt.plot(x, y,'b:o', x0, y0,'g-d')
            plt.title('Квадратное уравнение')
            plt.ylabel('y')
            plt.xlabel('x')
            plt.grid(True)
            plt.show()
            text=f"Вершина параболлы ({x0},{y0})"
        else:
            text=f"График нет возможности построить"
        vastus.configure(text=f"D={D}\n{t}\n{text}")
    global a,b,c
    win=Toplevel()#создаём второе(дочернее) окно
    win.geometry("500x400")
    win.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
    win.configure(bg="#141414")
    lbl=Label(win,text="Q u a d r a t i c   e q u a t i o n",fg="#f86263", bg="#141414")
    lbl.pack()
    vastus=Label(win, text="S o l u t i o n", height=4, width=60, bg="#ffcc66")
    vastus.pack(side=BOTTOM)
    a=Entry(win, bg="#f77273", width=3)
    a.pack(side=LEFT)
    x2=Label(win,text="x * * 2 + ", bg="#f86263", padx=10)
    x2.pack(side=LEFT)
    b=Entry(win, bg="#f77273", width=3)
    b.pack(side=LEFT)
    x=Label(win,text=" x + ", bg="#f86263")
    x.pack(side=LEFT)
    c=Entry(win,bg="#f77273",width=3)
    c.pack(side=LEFT)
    y=Label(win, text=" = 0 ", bg="#f86263")
    y.pack(side=LEFT)
    btn=Button(win,text="E n t e r",bg="#f86263",command=lahenda)
    btn.pack(side=LEFT)
    btn_g=Button(win,text="G r a p h i c",bg="#f86263", command=graafik)
    btn_g.pack(side=LEFT)

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



anim(0,0,"S O L V E R","#6598d6","#141414",cmd)
anim(0,37,"E X I T","#ffcc66","#141414",cmd1)
anim(0,74,"N E W   T A B","#f86263","#141414", cmd2)

#canvas=Canvas(aken,width=600,height=300)
#canvas.grid(columnspan=3)


aken.mainloop()
