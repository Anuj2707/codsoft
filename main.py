import tkinter
from tkinter import *

equ=""
def display(val):
    global equ
    equ+=val
    labelresult.config(text=equ)
def clear():
    global equ
    equ=""
    labelresult.config(text=equ)
def cal():
    global equ
    res=""
    if equ!="":
        try:
            res=eval(equ)
        except:
            res="error"
            equ=""
    labelresult.config(text=res)




win=tkinter.Tk()
win.title("CALCULATOR")
win.geometry("580x605+100+200")
win.resizable(False,False)
win.configure(bg="white")

#titleimage
titleimage=PhotoImage(file="cal.png")
win.iconphoto(False,titleimage)


labelresult=Label(win,width=25,height=2,text="",font=("poppins",30,"bold"))
labelresult.pack()

#buttons
Button(win,text="C",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="red",command=lambda: clear()).place(x=10,y=100)
Button(win,text="/",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="lightblue",command=lambda: display("/")).place(x=150,y=100)
Button(win,text="%",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="lightblue",command=lambda: display("%")).place(x=290,y=100)
Button(win,text="*",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="lightblue",command=lambda: display("*")).place(x=430,y=100)


Button(win,text="7",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="grey",command=lambda: display("7")).place(x=10,y=200)
Button(win,text="8",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="grey",command=lambda: display("8")).place(x=150,y=200)
Button(win,text="9",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="grey",command=lambda: display("9")).place(x=290,y=200)
Button(win,text="-",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="lightblue",command=lambda: display("-")).place(x=430,y=200)

Button(win,text="4",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="grey",command=lambda: display("4")).place(x=10,y=300)
Button(win,text="5",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="grey",command=lambda: display("5")).place(x=150,y=300)
Button(win,text="6",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="grey",command=lambda: display("6")).place(x=290,y=300)
Button(win,text="+",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="lightblue",command=lambda: display("+")).place(x=430,y=300)

Button(win,text="1",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="grey",command=lambda: display("1")).place(x=10,y=400)
Button(win,text="2",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="grey",command=lambda: display("2")).place(x=150,y=400)
Button(win,text="3",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="grey",command=lambda: display("3")).place(x=290,y=400)
Button(win,text=".",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="lightblue",command=lambda: display(".")).place(x=430,y=400)

Button(win,text="(",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="grey",command=lambda: display("(")).place(x=10,y=500)
Button(win,text=")",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="grey",command=lambda: display(")")).place(x=150,y=500)
Button(win,text="0",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="grey",command=lambda: display("0")).place(x=290,y=500)
Button(win,text="=",width=5,height=1,font=("poppins",30,"bold"),bd=1.5,fg="white",bg="darkblue",command=lambda: cal()).place(x=430,y=500)







win.mainloop()
