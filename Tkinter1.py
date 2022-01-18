from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
global D, t
D =-1
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
def open_win1():
    def whale():
        x1 = np.arange(0, 9.5, 1)#min max step
        y1=(2/27)*x1*x1-3
        x2 = np.arange(-10, 0.5, 1)#min max step
        y2=0.04*x2*x2-3
        x3 = np.arange(-9, -2.5, 1)#min max step
        y3=(2/9)*(x3+6)**2+1
        x4 = np.arange(-3, 9.5, 1)#min max step
        y4=(-1/12)*(x4-3)**2+6
        x5 = np.arange(5, 8.8  , 1)#min max step
        y5=(1/9)*(x5-5)**2+2
        x6 = np.arange(5, 9 , 1)#min max step
        y6=(1/8)*(x6-7)**2+1.5
        x7 = np.arange(-13, -8.5 , 1)#min max step
        y7=(-0.75)*(x7+11)**2+6
        x8 = np.arange(-15, -12.5 , 1)#min max step
        y8=(-0.5)*(x8+13)**2+3
        x9 = np.arange(-15, -9.5 , 1)#min max step
        y9=[1]*len(x9)
        x10 = np.arange(3, 4.5 , 1)#min max step
        y10=[3]*len(x10)
        fig = plt.figure()
        plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
        plt.title("whale")
        plt.ylabel("y")
        plt.xlabel("y")
        plt.grid(True)
        plt.show()
    def umbrella():
        x1 = np.arange(-12, 12, 0.5)#min max step
        y1=(-1/18)*x1*x1+12
        x2 = np.arange(-4, 4, 0.5)#min max step
        y2=(-1/8)*x2*x2+6
        x3 = np.arange(-12, -4, 0.5)#min max step
        y3=(-1/8)*(x3+8)**2+6
        x4 = np.arange(4, 12, 0.5)#min max step
        y4=(-1/8)*(x4-8)**2+6
        x5 = np.arange(-4, -0.3 , 0.5)#min max step
        y5=2*(x5+3)**2-9
        x6 = np.arange(-4, 0.2 , 0.5)#min max step
        y6=1.5*(x6+3)**2-10

        fig = plt.figure()
        plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
        plt.title("umbrella")
        plt.ylabel("y")
        plt.xlabel("y")
        plt.grid(True)
        plt.show()
    def butterfly():
        x1 = np.arange(-9, -1, 0.5)#min max step
        y1=(-1/8)*(x1+9)**2+8
        x2 = np.arange(1, 9, 0.5)#min max step
        y2=(-1/8)*(x2-9)**2+8
        x3 = np.arange(-9, -8, 0.5)#min max step
        y3=7*(x3+8)**2+1
        x4 = np.arange(8, 9, 0.5)#min max step
        y4=7*(x4-8)**2+1
        x5 = np.arange(-8, -1, 0.5)#min max step
        y5=(1/49)*(x5+1)**2
        x6 = np.arange(1, 8 , 0.5)#min max step
        y6=(1/49)*(x6-1)**2
        x7 = np.arange(-8, -1 , 0.5)#min max step
        y7=(-4/49)*(x7+1)**2
        x8 = np.arange(1, 8 , 0.5)#min max step
        y8=(-4/49)*(x8-1)**2
        x9 = np.arange(-8, -2 , 0.5)#min max step
        y9=(1/3)*(x9+5)**2-7
        x10 = np.arange(2, 8 , 0.5)#min max step
        y10=(1/3)*(x10-5)**2-7
        x11 = np.arange(-2, -1 , 0.5)#min max step
        y11=(-2)*(x11+1)**2-2
        x12 = np.arange(1, 2 , 0.5)#min max step
        y12=(-2)*(x12-1)**2-2
        x13 = np.arange(-1, 1 , 0.5)#min max step
        y13=(-4)*x13*x13*+2
        x14 = np.arange(-1, 1 , 0.5)#min max step
        y14=(4)*x14*x14*-6
        x15 = np.arange(-2, 0 , 0.5)#min max step
        y15=(-1.5)*x15*+2
        x16 = np.arange(0, 2 , 0.5)#min max step
        y16=(1.5)*x16*+2

        fig = plt.figure()
        plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16)
        plt.title("umbrella")
        plt.ylabel("y")
        plt.xlabel("y")
        plt.grid(True)
        plt.show()
    def frog():
        x1 = np.arange(-7,7.5, 0.5)#min max step
        y1=(-3/49)*x1*x1+8
        x2 = np.arange(-7,7.5, 0.5)#min max step
        y2=(4/49)*x2*x2+1
        x3 = np.arange(-6.8,-1.5, 0.5)#min max step
        y3=(-0.75)*(x3+4)**2+11
        x4 = np.arange(2,7.3, 0.5)#min max step
        y4=(-0.75)*(x4-4)**2+11
        x5 = np.arange(-5.8,-2.3  , 0.5)#min max step
        y5=-(x5+4)**2+9
        x6 = np.arange(2.8, 6.3 , 0.5)#min max step
        y6=-(x6-4)**2+9
        x7 = np.arange(-4,4.5 , 0.5)#min max step
        y7=(4/9)*x7*x7-5
        x8 = np.arange(-5.2,5.7 , 0.5)#min max step
        y8=(4/9)*x8*x8-9
        x9 = np.arange(-7,-2.3 , 0.5)#min max step
        y9=(-1/16)*(x9+3)**2-6
        x10 = np.arange(2.8,7.5 , 0.5)#min max step
        y10=(-1/16)*(x10-3)**2-6
        x11 = np.arange(-7,0.5, 0.5)#min max step
        y11=(1/9)*(x11+4)**2-11
        x12 = np.arange(0, 7.5 ,0.5)#min max step
        y12=(1/9)*(x12-4)**2-11
        x13 = np.arange(-7,-4.0 ,0.5)#min max step
        y13=-(x13+5)**2
        x14 = np.arange(4.5 ,7.5 ,0.5)#min max step
        y14=-(x14-5)**2
        x15 = np.arange(-3, 3.5 ,0.5)#min max step
        y15=(2/9)*x15*x15+2
        fig = plt.figure()
        plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15)
        plt.title('КИТ')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
    def glasses():
        x1 = np.arange(-9,-0.5, 0.5)#min max step
        y1=(-1/16)*(x1+5)**2+2
        x2 = np.arange(1,9.5, 0.5)#min max step
        y2=(-1/16)*(x2-5)**2+2
        x3 = np.arange(-9,-0.5, 0.5)#min max step
        y3=(1/4)*(x3+5)**2-3
        x4 = np.arange(1,9.5, 0.5)#min max step
        y4=(1/4)*(x4-5)**2-3
        x5 = np.arange(-9,-5.5  , 0.5)#min max step
        y5=-(x5+7)**2+5
        x6 = np.arange(6,9.5 , 0.5)#min max step
        y6=-(x6-7)**2+5
        x7 = np.arange(-1, 1.5 , 0.5)#min max step
        y7=(-0.5)*x7*x7+1.5
        fig = plt.figure()
        plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
        plt.title("glasses")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()  
    win1=Toplevel()#создаём второе(дочернее) окно
    win1.geometry("800x600")
    win1.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
    win1.configure(bg="#141414")

    var=StringVar()
    var.set("uks")
    r1=Radiobutton(win1,variable=var,bg="#6598d6",text="Whale",height=3, width=6,command=whale)
    r2=Radiobutton(win1,variable=var,bg="#8a8a8a",text="Glasses",height=3, width=6,command=glasses)
    r3=Radiobutton(win1,variable=var,bg="#e3de76",text="Umbrella",height=3, width=6,command=umbrella)
    r4=Radiobutton(win1,variable=var,bg="#93d171",text="Frog",height=3, width=6,command=frog)
    r5=Radiobutton(win1,variable=var,bg="#e38e76",text="Butterfly",height=3, width=6,command=butterfly)

    r1.pack(side=LEFT)
    r2.pack(side=RIGHT)
    r3.pack(side=BOTTOM)
    r4.pack(side=RIGHT)
    r5.pack()

    win1.mainloop()

def open_win2():
    win2=Toplevel()#создаём второе(дочернее) окно
    win2.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
    win2.configure(bg="#141414")
    win2.geometry("955x710")

    Label(win2, borderwidth=1, relief="solid",text=" ", width=20,height=5).grid(row=0, column=0)
    Label(win2, borderwidth=1, relief="solid",text=" 0 ", width=10,height=5).grid(row=0, column=1)
    Label(win2, borderwidth=1, relief="solid",text=" 1 ", width=10,height=5).grid(row=0, column=2)
    Label(win2, borderwidth=1, relief="solid",text=" 2 ", width=10,height=5).grid(row=0, column=3)
    Label(win2, borderwidth=1, relief="solid",text=" 3 ", width=10,height=5).grid(row=0, column=4)
    Label(win2, borderwidth=1, relief="solid",text=" 4 ", width=10,height=5).grid(row=0, column=5)
    Label(win2, borderwidth=1, relief="solid",text=" 5 ", width=10,height=5).grid(row=0, column=6)
    Label(win2, borderwidth=1, relief="solid",text=" 6 ", width=10,height=5).grid(row=0, column=7)
    Label(win2, borderwidth=1, relief="solid",text=" 7 ", width=10,height=5).grid(row=0, column=8)
    Label(win2, borderwidth=1, relief="solid",text=" 8 ", width=10,height=5).grid(row=0, column=9)
    Label(win2, borderwidth=1, relief="solid",text=" 9 ", width=10,height=5).grid(row=0, column=10)
    Label(win2, borderwidth=1, relief="solid",text=" 10 ", width=10,height=5).grid(row=0, column=11)

    Label(win2, borderwidth=0, relief="solid", text="7.40-8.25", width=10,height=2).grid(row=0, column=1,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="8.30-9.15", width=10,height=2).grid(row=0, column=2,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="9.20-10.05", width=10,height=2).grid(row=0, column=3,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="10.10-10.55", width=10,height=2).grid(row=0, column=4,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="11.00-11.45", width=10,height=2).grid(row=0, column=5,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="11.50-12.35", width=10,height=2).grid(row=0, column=6,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="12.40-13.25", width=10,height=2).grid(row=0, column=7,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="13.30-14.15", width=10,height=2).grid(row=0, column=8,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="14.20-15.05", width=10,height=2).grid(row=0, column=9,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="15.10-15.55", width=10,height=2).grid(row=0, column=10,sticky=S)
    Label(win2, borderwidth=0, relief="solid", text="16.00-16.45", width=10,height=2).grid(row=0, column=11,sticky=S)


    Label(win2, borderwidth=1, relief="solid",text="Esmaspäev", width=20,height=8).grid(row=1, column=0)
    Label(win2, borderwidth=1, relief="solid",text="Teisipäev", width=20,height=8).grid(row=2, column=0)
    Label(win2, borderwidth=1, relief="solid",text="Kolmapäev", width=20,height=8).grid(row=3, column=0)
    Label(win2, borderwidth=1, relief="solid",text="Neljapäev", width=20,height=8).grid(row=4, column=0)
    Label(win2, borderwidth=1, relief="solid",text="Reede", width=20,height=8).grid(row=5, column=0)

    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=1)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=1)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=1)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=1)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=1)


        #1
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=2)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=3)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=4)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=5)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=6)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=7)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=8)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=9)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=10)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=1, column=11)

    Label(win2, borderwidth=1, bg="#cab4c7", relief="solid",text="Eesti keel", width=10,height=4).grid(row=1, column=2,sticky=S)
    Label(win2, relief="solid",borderwidth=0, bg="#cab4c7" ,text="B234", width=5,height=1).grid(row=1, column=2,sticky=SW)
    Label(win2, borderwidth=1, bg="#80e092", relief="solid",text="Logistikateenused\nja varude juhtimine", width=10,height=8).grid(row=1, column=3, sticky=N+S+W+E, columnspan=2)
    Label(win2, borderwidth=1, bg="#fcb9d0", relief="solid",text="Matemaatika", width=10,height=8).grid(row=1, column=5, sticky=N+S+W+E, columnspan=2)
    Label(win2, borderwidth=1, bg="#94ed80", relief="solid",text="Keel ja kirjandus", width=10,height=8).grid(row=1, column=8, sticky=N+S+W+E, columnspan=2)
    Label(win2, borderwidth=1, bg="#fcb9d0", relief="solid",text="Tugiõpe\n(matema\natika)", width=10,height=8).grid(row=1, column=10, sticky=N+S+W+E)




        #2
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=2)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=3)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=4)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=5)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=6)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=7)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=8)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=9)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=10)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=2, column=11)

    Label(win2, borderwidth=1, bg="#e080e0", relief="solid",text="Tugiõpe\n(keemia)", width=10,height=4).grid(row=2, column=2,sticky=N+S+W+E)
    Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=2, column=3, sticky=N+S+W+E, columnspan=3)
    Label(win2, borderwidth=1, bg="#fcb9d0", relief="solid",text="Füüsika", width=10,height=8).grid(row=2, column=7, sticky=N+S+W+E, columnspan=2)

        #3
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=2)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=3)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=4)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=5)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=6)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=7)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=8)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=9)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=10)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=3, column=11)

    Label(win2, borderwidth=1, bg="#ff80ff", relief="solid",text="Tugiõpe\n(eesti keel)", width=10,height=4).grid(row=3, column=2,sticky=N)
    Label(win2, borderwidth=1, bg="#e080ce", relief="solid",text="Kuntsiained\n(eesti keeles)", width=10,height=8).grid(row=3, column=3, sticky=N+S+W+E, columnspan=2)
    Label(win2, borderwidth=1, bg="#e080c0", relief="solid",text="Kehaline kasvatus", width=10,height=8).grid(row=3, column=6, sticky=N+S+W+E, columnspan=2)

        #4
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=2)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=3)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=4)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=5)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=6)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=7)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=8)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=9)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=10)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=4, column=11)

    Label(win2, borderwidth=1, bg="#80e092", relief="solid",text="Logistikateenused\nja varude juhtimine", width=10,height=8).grid(row=4, column=2, sticky=N+S+W+E, columnspan=2)
    Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=4, column=5, sticky=N+S+W+E, columnspan=2)
    Label(win2, bg="#fffff0",text="Inglise keel", width=20,height=4).grid(row=4, column=7, sticky=N, columnspan=2)
    Label(win2, bg="#ff80a2",text="Rahendustrakvara", width=20,height=4).grid(row=4, column=7, sticky=S, columnspan=2)

    Label(win2, bg="#ff80a2",text="Rahendustrakvara", width=20,height=4).grid(row=4, column=9, sticky=N, columnspan=2)
    Label(win2, bg="#cab4c7",text="Eesti keel", width=20,height=4).grid(row=4, column=9,sticky=S, columnspan=2)
    Label(win2, borderwidth=1, bg="#ff80ff", relief="solid",text="Rühmaju\nhataja\ntund", width=10,height=4).grid(row=4, column=11,sticky=N+S+W+E)

        #5
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=2)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=3)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=4)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=5)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=6)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=7)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=8)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=9)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=10)
    Label(win2, borderwidth=1, relief="solid",text=" ", width=10,height=8).grid(row=5, column=11)

    Label(win2, bg="#ff80ff",text="Eesti keel", width=20,height=4).grid(row=5, column=2, sticky=N, columnspan=2)
    Label(win2, bg="#ff80a2",text="Rahendustrakvara", width=20,height=4).grid(row=5, column=2, sticky=S, columnspan=2)
    Label(win2, borderwidth=1, bg="#abe0ff", relief="solid",text="Programmeerimise alused\n(eesti keeles)", width=10,height=8).grid(row=5, column=4, sticky=N+S+W+E, columnspan=5)
    Label(win2, bg="#ff80a2",text="Rahendustrakvara", width=20,height=4).grid(row=5, column=9, sticky=N, columnspan=2)
    Label(win2, bg="#80ff80",text="Inglise keel", width=20,height=4).grid(row=5, column=9,sticky=S, columnspan=2)

    win2.mainloop()



def open_win():
    def lahenda():
        global a,b,c,D,t
        t=""
        graf=""
        if (a.get()!="" and b.get()!="" and c.get()!=""):
            if (float(a.get())==0 and float(b.get())==0 and float(c.get())==0):
                vastus.configure(text=f"Wrong!")
                a.configure(bg="red")
                b.configure(bg="red")
                c.configure(bg="red")
                graf=False
            elif float(a.get())==0 and float(b.get())!=0 and float(c.get())!=0:
                vastus.configure(text=f"Wrong!")
                a.configure(bg="red")
                b.configure(bg="#red")
                c.configure(bg="#red")
                graf=False
            elif float(a.get())!=0 and float(b.get())==0 and float(c.get())!=0:
                vastus.configure(text=f"Wrong!")
                b.configure(bg="red")
                a.configure(bg="#red")
                c.configure(bg="#red")
                graf=False
            elif float(a.get())!=0 and float(b.get())!=0 and float(c.get())==0:
                vastus.configure(text=f"Wrong!")
                c.configure(bg="red")
                b.configure(bg="#red")
                a.configure(bg="#red")
                graf=False
            elif float(a.get())!=0 and float(b.get())!=0 and float(c.get())!=0:
                a_=float(a.get())
                b_=float(b.get())
                c_=float(c.get())
                D=b_*b_-4*a_*c_
                if D > 0:
                    x1_=round((-1*b_+sqrt(D))/(2*a_),2)
                    x2_=round((-1*b_-sqrt(D))/(2*a_),2)
                    t=f"X1={x1_}, \nX2={x2_}"
                    graf=True
                elif D == 0:
                    x1_=round((-1*b_)/(2*a_),2)
                    t=f"X1={x1_}"
                    graf=True
                else:
                    t="No root"
                    graf=False
                vastus.configure(text=f"D={D}\n{t}")
                a.configure(bg="#f86263")
                b.configure(bg="#f86263")
                c.configure(bg="#f86263")
        else:

           if a.get()=="":
              a.configure(bg="red")
           if b.get()=="":
              b.configure(bg="red")
           if c.get()=="":
              c.configure(bg="red")
        return graf,D,t
    def graafik():
        graf,D,t=lahenda()
        if graf==True:
            a_=int(a.get())
            b_=int(b.get())
            c_=int(c.get())
            x0=(-b_)/(2*a_)
            y0=a_*x0*x0+b_*x0+c_
            x = np.arange(x0-10, x0+10, 0.5)#min max step
            y=a_*x*x+b_*x+c_
            fig = plt.figure()
            plt.plot(x, y,'b:o', x0, y0,'g-d')
            plt.title("Quadratic equation")
            plt.ylabel('y')
            plt.xlabel('x')
            plt.grid(True)
            plt.show()
            text=f"Вершина параболлы ({x0},{y0})"
        else:
            text=f"No root."
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

def open_win3():
    def lisa_nina():
        if var_nina.get()=="Nina":
            c.create_oval((225, 225, 275, 275), fill="#db5853", outline="black") #нос 
        elif var_nina.get()=="tühi":
            c.create_oval((225, 225, 275, 275), fill="#b39474", outline="#b39474") #нос 
    def lisa_suu():
        if var_suu.get()=="Suu":
            c.create_arc((100, 300, 400,400),start=180,extent=180, style=ARC, fill="black", outline="black")
        elif var_suu.get()=="tühi":
            c.create_arc((100, 300, 400,400),start=180,extent=180, style=ARC,   fill="#b39474", outline="#b39474")
    def lisa_eyes():
        if var_eyes.get()=="Silmad":
            c.create_oval((300, 100, 400, 200), fill="#a8a8a8", outline="black") #првый глаз


            c.create_oval((200, 200, 100, 100), fill="#a8a8a8", outline="black") #левый глаз


        elif var_eyes.get()=="tühi":
            c.create_oval((300, 100, 400, 200),  fill="#b39474", outline="#b39474") #првый глаз
            c.create_oval((200, 200, 100, 100),  fill="#b39474", outline="#b39474") #левый глаз
    def brov():
        if var_brov.get()=="Kulmu":
            c.create_line((300, 80, 400, 100), fill="black", width=3) #првый brov
            c.create_line((200, 80, 100, 100), fill="black", width=3) #levii brov
        elif var_brov.get()=="tühi":
            c.create_line((300, 80, 400, 100), fill="#b39474", width=3) #првый brov
            c.create_line((200, 80, 100, 100), fill="#b39474", width=3) #levii brov
    def zraki():
        if var_zraki.get()=="Tera":

            c.create_oval((375, 175, 325, 125), fill="black", outline="black") #првый z

            c.create_oval((125, 125, 175, 175), fill="black", outline="black") #левый z

        elif var_zraki.get()=="tühi":
            c.create_oval((375, 175, 325, 125),  fill="#b39474", outline="#b39474") #првый z
            c.create_oval((125, 125, 175, 175),  fill="#b39474", outline="#b39474") #левый z

    win17=Toplevel()#создаём второе(дочернее) окно
    win17.geometry("500x700")
    win17.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
    win17.configure(bg="#d8e0ca")

    c = Canvas(win17, width=500, height=500, bg="#c9c9c9")
    c.create_oval((10, 10, 490, 490), fill="#b39474", outline="black") #лицо
    var_nina=StringVar()
    ch_nina=Checkbutton(win17,text="1. Nina", variable=var_nina, onvalue="Nina", bg="#95b374",offvalue="tühi",command=lisa_nina)
    ch_nina.pack()
    var_suu=StringVar()
    ch_suu=Checkbutton(win17,text="2. Suu", variable=var_suu, onvalue="Suu", bg="#95b374",offvalue="tühi",command=lisa_suu)
    ch_suu.pack()
    var_eyes=StringVar()
    ch_eyes=Checkbutton(win17,text="3. Silmad", variable=var_eyes, onvalue="Silmad", bg="#95b374",offvalue="tühi",command=lisa_eyes)
    ch_eyes.pack()
    var_brov=StringVar()
    ch_brov=Checkbutton(win17,text="4. Kulmud", variable=var_brov, onvalue="Kulmu", bg="#95b374",offvalue="tühi",command=brov)
    ch_brov.pack()
    var_zraki=StringVar()
    ch_zraki=Checkbutton(win17,text="5. Silma Tera", variable=var_zraki, bg="#95b374",  onvalue="Tera", offvalue="tühi",command=zraki)
    ch_zraki.pack()

    c.pack()

    win17.mainloop()
def cmd():
    print("Radio button")
    aken.command=open_win1()
def cmd1():
    print("Exit . . . ")

    aken.destroy()
def cmd2():
    print("Toplevel")
    aken.command=open_win()
def cmd4():
    print("Photo robot")
    aken.command=open_win3()
def cmd5():
    print("Grid")
    aken.command=open_win2()



anim(0,0,"R A D I O   B U T T O N","#6598d6","#141414",cmd)
anim(0,37,"Q U A D R A T I C   E Q U A T I O N","#f86263","#141414", cmd2)
anim(0,74,"P H O T O   R O B O T","#88bf77","#141414", cmd4)
anim(0,111,"G R I D","#8f77bf","#141414",cmd5)
#148
anim(0,185,"E X I T","#ffcc66","#141414",cmd1)


#canvas=Canvas(aken,width=600,height=300)
#canvas.grid(columnspan=3)

aken.mainloop()
