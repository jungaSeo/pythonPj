import sys
from tkinter import *

def clear():
    txtDisplay.delete(0, END)
    return 

root = Tk()

frame = Frame(root)
frame.pack()

root.title('Calculator')

num1 = StringVar()

topframe = Frame(root)
topframe.pack(side=TOP)

txtDisplay = Entry(frame, text = num1, bd=20, insertwidth=1, font=30)
# Entry을 이용하여 텍스트를 입력받거나 출력하기 위한 기입창을 생성할 수 있습니다
# borderwidth=bd : 기입창의 테두리 두께
# insertwidth : 기입창의 키보드 커서 너비

txtDisplay.pack(side=TOP)


 
button1 = Button(topframe,padx=16, pady=16, bd=8, text="1", fg="black") 
# padx: 버튼의 테두리와 내용의 가로 여백
# pady : 버튼의 테두리와 내용의 세로 여백
button1.pack(side = LEFT)
button2 = Button(topframe,padx=16, pady=16, bd=8, text="2", fg="black") 
button2.pack(side = LEFT)
button3 = Button(topframe,padx=16, pady=16, bd=8, text="3", fg="black") 
button3.pack(side = LEFT)
button4 = Button(topframe,padx=16, pady=16, bd=8, text="4", fg="black") 
button4.pack(side = LEFT)

frame1 = Frame(root)
frame1.pack(side = TOP)
button1 = Button(frame1,padx=16, pady=16, bd=8, text="5", fg="black") 
button1.pack(side = LEFT)
button2 = Button(frame1,padx=16, pady=16, bd=8, text="6", fg="black") 
button2.pack(side = LEFT)
button3 = Button(frame1,padx=16, pady=16, bd=8, text="7", fg="black") 
button3.pack(side = LEFT)
button4 = Button(frame1,padx=16, pady=16, bd=8, text="8", fg="black") 
button4.pack(side = LEFT)

frame2 = Frame(root)
frame2.pack(side = TOP)
 
button1 = Button(frame2,padx=16, pady=16, bd=8, text="9", fg="black") 
button1.pack(side = LEFT)
button2 = Button(frame2,padx=16, pady=16, bd=8, text="0", fg="black") 
button2.pack(side = LEFT)
button3 = Button(frame2,padx=16, pady=16, bd=8, text="C", fg="black", command = clear) 
button3.pack(side = LEFT)
button4 = Button(frame2,padx=16, pady=16, bd=8, text="-", fg="black") 
button4.pack(side = LEFT)
 
frame3 = Frame(root)
frame3.pack(side = TOP)

button1 = Button(frame3,padx=16, pady=16, bd=8, text="*", fg="black") 
button1.pack(side = LEFT)
button2 = Button(frame3,padx=16, pady=16, bd=8, text="/", fg="black") 
button2.pack(side = LEFT)
button3 = Button(frame3,padx=16, pady=16, bd=8, text="-", fg="black") 
button3.pack(side = LEFT)
button4 = Button(frame3,padx=16, pady=16, bd=8, text="+", fg="black") 
button4.pack(side = LEFT)

root.mainloop() 