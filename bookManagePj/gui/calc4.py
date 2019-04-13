import sys
from tkinter import *

root = Tk()
root.geometry("300x340+50+50")
# x너비, y너비, x좌표, y좌표
root.title("Calculator")
#==============================================================================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    print(operator)
    text_Input.set(operator)
    print(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEqual():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
    
operator = ""
text_Input = StringVar()    
    
#==============================================================================================

Tops = Frame(root, width=300, height="20", bd=4, relief="raised")
# -- relief [default value:'flat']
# Frame위젯의 테두리모양 ("flat", "groove", "raised", "ridge", "solid", "sunken")
Tops.pack(side=TOP)

Below = Frame(root, width=300, height="300", bd=4, relief="raised")
Below.pack(side=BOTTOM)

txtDisplay = Entry(Tops, font=('arial', 18, 'bold'), textvariable=text_Input, width=21, bd=4, justify='right')
# -- Entry을 이용하여 텍스트를 입력받거나 출력하기 위한 기입창을 생성할 수 있습니다
# borderwidth=bd : 기입창의 테두리 두께
# insertwidth : 기입창의 키보드 커서 너비
# justify: 기입창의 문자열이 여러 줄 일 경우 정렬 방법 (center, left, right)
txtDisplay.grid(row= 0,column=0)
 
btn7 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="7", command = lambda:btnClick(7)).grid(row= 0, column=0)
# lambda == 익명 함수(anonymous function)
# proc 과 lambda 는 메소드 내에 또 메소드를 선언할 수 있는 기괴한 개념을 가지고 있는 함수(객체)
# https://cafe.naver.com/sonnysoft2004/66070
# proc 은 메소드 내에 삽입됩니다 (return 을 만나면 메소드가 종료되고, 외부 메소드의 다음 라인을 실행 할 수 없는 상태가 됩니다.)
# lambda 는 값을 반환하고 다음 라인을 실행합니다 (return 을 만나도 외부 메소드가 종료되지 않습니다)

 
btn8 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="8", command = lambda:btnClick(8)).grid(row= 0, column=1)
 
btn9 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="9", command = lambda:btnClick(9)).grid(row= 0, column=2)
 
btnAdd = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="+", command = lambda:btnClick("+")).grid(row= 0, column=3)
#==============================================================================================
 
btn4 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="4", command = lambda:btnClick(4)).grid(row= 1, column=0)
 
btn5 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="5", command = lambda:btnClick(5)).grid(row= 1, column=1)
 
btn6 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="6", command = lambda:btnClick(6)).grid(row= 1, column=2)
 
btnSub = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="-", command = lambda:btnClick("-")).grid(row= 1, column=3)
#==============================================================================================
 
btn1 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="1", command = lambda:btnClick(1)).grid(row= 2, column=0)
 
btn2 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="2", command = lambda:btnClick(2)).grid(row= 2, column=1)
 
btn3 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="3", command = lambda:btnClick(3)).grid(row= 2, column=2)
 
btnMult = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="*", command = lambda:btnClick("*")).grid(row= 2, column=3)
#==============================================================================================
 
btn0 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="0", command = lambda:btnClick(0)).grid(row= 3, column=0)
 
btnClear = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="C", command = btnClear).grid(row= 3, column=1)
 
btnEquals = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="=", command = btnEqual).grid(row= 3, column=2)
 
btnDiv = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial', 16, 'bold'), width=2, height=2,
text="/", command = lambda:btnClick("/")).grid(row= 3, column=3)
#==============================================================================================

root.mainloop()