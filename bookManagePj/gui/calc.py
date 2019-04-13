import sys
from tkinter import *

    
w = Tk()
w.geometry("400x200+50+50")
w.title("Calculator")

# ==================================================================
def btnClick(numbers):
    global operator 
    operator = str(numbers)
    textIn1.set(operator)
    sumup = str(eval(num1.get() + operator + num2.get()))
    print(sumup)
    textResult.set(sumup)
    
operator = ""
textResult=StringVar()
textIn1 = StringVar()

# ==================================================================

Tops = Frame(w, width=400, height="20", bd=4, relief="raised")
Tops.pack()

Center = Frame(w, width=400, height="20", bd=4, relief="raised")
Center.pack()

Below1 = Frame(w, width=400, height="20", bd=4, relief="raised")
Below1.pack()

Below2 = Frame(w, width=400, height="20", bd=4, relief="raised")
Below2.pack()


# ==================================================================

num1 = Entry(Tops, width=15, font=('arial', 12, 'bold'), justify="right")
num1.pack(side = LEFT)

opt = Label(Tops, width=5, font=('arial', 12, 'bold'), textvariable= textIn1)
opt.pack(side = LEFT)

num2 = Entry(Tops, width=15, font=('arial', 12, 'bold'), justify="right")
num2.pack(side = LEFT)

# ==================================================================

equal = Label(Center, width=3, font=('arial', 12, 'bold'), text="=")
equal.pack(side = LEFT)

result = Label(Center, width=30, font=('arial', 12, 'bold'), justify="right", textvariable= textResult)
result.pack(side = LEFT)

# ==================================================================

btn1 = Button(Below1, text="+", font=('arial', 12, 'bold'), padx=5, pady=5, command=lambda:btnClick("+"))
btn1.pack(side= LEFT)

btn2 = Button(Below1, text="-", font=('arial', 12, 'bold'), padx=5, pady=5, command=lambda:btnClick("-"))
btn2.pack(side= LEFT)

btn3 = Button(Below1, text="*", font=('arial', 12, 'bold'), padx=5, pady=5, command=lambda:btnClick("*"))
btn3.pack(side= LEFT)

btn4 = Button(Below1, text="/", font=('arial', 12, 'bold'), padx=5, pady=5, command=lambda:btnClick("/"))
btn4.pack(side= LEFT)

btn5 = Button(Below1, text="%", font=('arial', 12, 'bold'), padx=5, pady=5, command=lambda:btnClick("%"))
btn5.pack(side= LEFT)

btn6 = Button(Below1, text="**", font=('arial', 12, 'bold'), padx=5, pady=5, command=lambda:btnClick("**"))
btn6.pack(side= LEFT)

btn7 = Button(Below1, text="//", font=('arial', 12, 'bold'), padx=5, pady=5, command=lambda:btnClick("//"))
btn7.pack(side= LEFT)

# ==================================================================

btn8 = Button(Below2, text="==", font=('arial', 12, 'bold'), padx=5, pady=5, command=lambda:btnClick("=="))
btn8.pack(side= LEFT)

btn9 = Button(Below2, text="!=", font=('arial', 12, 'bold'), padx=5, pady=5, command=lambda:btnClick("=="))
btn9.pack(side= LEFT)

btn10 = Button(Below2, text=">", font=('arial', 12, 'bold'), padx=5, pady=5, command=lambda:btnClick(">"))
btn10.pack(side= LEFT)

btn11 = Button(Below2, text="<", font=('arial', 12, 'bold'), padx=5, pady=5, command=lambda:btnClick("<"))
btn11.pack(side= LEFT)

btn12 = Button(Below2, text=">=", font=('arial', 12, 'bold'), padx=5, pady=5, command=lambda:btnClick(">="))
btn12.pack(side= LEFT)

btn13 = Button(Below2, text="<=", font=('arial', 12, 'bold'), padx=5, pady=5, command=lambda:btnClick("<="))
btn13.pack(side= LEFT)



w.mainloop()