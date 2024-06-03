from tkinter import *
exp = ""
def input(num):
    global exp
    exp = exp + str(num)
    eq.set(exp)
def Result():
    try: 
        global exp
        total = str(eval(exp))
        eq.set(total)
        exp = ""
    except:
        eq.set("error")
        exp = ""
def clear():
    global exp
    exp = ""
    eq.set("")    
if __name__ == "__main__":
    win = Tk()
    win.config(bg="powder blue")
    win.title("Pandey's Calculator")
    win.option_add('*font','lucida 15 bold')
    win.geometry("433x408")
    eq = StringVar()

display = Entry(win, relief=RIDGE, textvariable=eq, justify='right',bd=40)

display.grid(columnspan=10, ipadx=45)

butn1 = Button(win, text = '1', fg = 'black', 
                 command=lambda: input(1)  ,bd=5, height=3, width=6)
butn1.grid(row=1 ,column =0)

butn2 = Button(win, text = '2', fg = 'black', 
                 command=lambda: input(2)  ,bd=5, height=3, width=6)
butn2.grid(row=1 ,column =1)

butn3 = Button(win, text = '3', fg = 'black', 
                 command=lambda: input(3)  ,bd=5, height=3, width=6)
butn3.grid(row=1 ,column =2)

plus = Button(win, text = '+', fg = 'black', 
                command=lambda: input("+")  ,bd=5, height=3, width=6)
plus.grid(row=1 ,column =3)

butn4 = Button(win, text = '4', fg = 'black',
                 command=lambda: input(4)  ,bd=5, height=3, width=6)
butn4.grid(row=2 ,column =0)

butn5 = Button(win, text = '5', fg = 'black', 
                 command=lambda: input(5)  ,bd=5, height=3, width=6)
butn5.grid(row=2 ,column =1)

butn6 = Button(win, text = '6', fg = 'black',
                 command=lambda: input(6)  ,bd=5, height=3, width=6)
butn6.grid(row=2 ,column =2)

minus = Button(win, text = '-', fg = 'black', 
                 command=lambda: input("-")  ,bd=5, height=3, width=6)
minus.grid(row=2 ,column =3)

butn7 = Button(win, text = '7', fg = 'black',
                 command=lambda: input(7)  ,bd=5, height=3, width=6)
butn7.grid(row=3 ,column =0)

butn8 = Button(win, text = '8', fg = 'black', 
                 command=lambda: input(8)  ,bd=5, height=3, width=6)
butn8.grid(row=3 ,column =1)

butn9 = Button(win, text = '9', fg = 'black',
                 command=lambda: input(9)  ,bd=5, height=3, width=6)
butn9.grid(row=3 ,column =2)

multilpy = Button(win, text = '*', fg = 'black', 
                   command=lambda: input("*")  ,bd=5, height=3, width=6)
multilpy.grid(row=3 ,column =3)       

butn0 = Button(win, text = '0', fg = 'black', 
                 command=lambda: input(0)  ,bd=5, height=3, width=6) 
butn0.grid(row=4 ,column =0)

divide = Button(win, text = '/', fg = 'black',  
                 command=lambda: input("/")  ,bd=5, height=3, width=6)
divide.grid(row=4 ,column =1) 

equal = Button(win, text = '=', fg = 'black', 
                 command= Result, bd=5, height=3, width=6)
equal.grid(row=4 ,column =2)

clear = Button(win, text = 'C', fg = 'black', 
                 command= clear, bd=5, height=3, width=6)   
clear.grid(row=4 ,column =3)

win.mainloop()