import tkinter
from tkinter import *

root = Tk()
root.title("Calcilator")
root.geometry("570x600+100+100")
root.resizable(False, False)
root.configure(bg="black")

equation = ""

def show(value):
    global equation
    if value in "+-*/%" and equation and equation[-1] in "+-*/%":
        equation = equation[:-1] + value
    else:
        equation += value
    label_result.config(text=equation)
    
def clear():
    global equation
    equation=""
    label_result.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result = eval(equation)
            equation = str(result)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)

label_result = Label(root,width=25,height=2,text="",font=("arial",30), fg="#fff", bg="black")
label_result.pack()

Button(root,text="C",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="red",command=lambda: clear()).place(x=10,y=100)
Button(root,text="%",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="green",command=lambda: show("%")).place(x=150,y=100)
Button(root,text="/",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="green",command=lambda: show("/")).place(x=290,y=100)
Button(root,text="*",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="green",command=lambda: show("*")).place(x=430,y=100)

Button(root,text="7",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda: show("7")).place(x=10,y=200)
Button(root,text="8",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda: show("8")).place(x=150,y=200)
Button(root,text="9",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda: show("9")).place(x=290,y=200)
Button(root,text="-",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="green",command=lambda: show("-")).place(x=430,y=200)

Button(root,text="4",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda: show("4")).place(x=10,y=300)
Button(root,text="5",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda: show("5")).place(x=150,y=300)
Button(root,text="6",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda: show("6")).place(x=290,y=300)
Button(root,text="+",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="green",command=lambda: show("+")).place(x=430,y=300)

Button(root,text="1",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda: show("1")).place(x=10,y=400)
Button(root,text="2",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda: show("2")).place(x=150,y=400)
Button(root,text="3",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda: show("3")).place(x=290,y=400)
Button(root,text="0",width=11,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda: show("0")).place(x=10,y=500)

Button(root,text=".",width=5,height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda: show(".")).place(x=290,y=500)
Button(root,text="=",width=5,height=3, font=("arial",30,"bold"), bd=1, fg="#fff", bg="orange",command=lambda: calculate()).place(x=430,y=400)

root.mainloop()
