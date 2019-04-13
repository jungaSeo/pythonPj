from tkinter import *
from click.decorators import command

def onClick():
    d2 = int(data2.get())
    age = 2019 - d2 + 1
    print(age)
    result["text"] = "나이는" + age;
#     data1 = text.get()
#     print("당신의 나이는", 2019 - int(data1), "입니다.")
    
    
w = Tk()

# 1. 이름입력(라벨+입력란)
name = Label(w, text = "이름을 입력하세요...")
name.pack()

text = Entry(w)
text.pack()

# 2. 태어난 해 입력
year = Label(w, text = "태어난 해를 입력하세요...")
year.pack()

text = Entry(w)
text.pack()

# 3. 버튼 처리
# btn = Button(w, text = "입력버튼", command=onClick) # 3. 버튼 생성
# btn.pack()
result = Button(w, text = "입력버튼", data2="") # 3. 버튼 생성
result.pack()


# 
# btn = Button(w, text="입력버튼", command = onClick) 
# btn.pack()


w.mainloop()