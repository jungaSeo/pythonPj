from tkinter import *
from tkinter import messagebox

def onClick():
    data1 = text.get()
    messagebox.showinfo("입력받은 값>> ", data1)
    print("입력받은 값>> ", data1)

root = Tk() # 1. 틀 만들기 (생성자)           

name = Label(root, text = "이름입력하세요..")
name.pack()

        
text = Entry(root)
text.pack()


#btn = Button(root, text = "입력버튼", command=onClick) # 3. 버튼 생성
btn = Button(root, text = "입력버튼", command=onClick) # 3. 버튼 생성

btn.pack()  # 4. root에 얹기

root.mainloop()# 2. 계속 떠있게 만듦