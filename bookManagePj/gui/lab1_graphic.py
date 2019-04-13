'''
# 1.
콘솔에서 과목명:
messageBox에 출력.

# 2.
콘솔에서 지금시각:
messageBox에 출력.
'''
from tkinter import messagebox


time = input("지금시각>> ")
messagebox.showinfo("지금시각 ", time)


subj = input("과목명>> ")
messagebox.showinfo("과목명 ", subj)


