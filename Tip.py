"""
!/usr/bin/python11
-*- coding: utf-8 -*-            
@Author : xuyuhao
@Time : 2023/12/30 0:05
@FileName: Tip.py
"""
from tkinter import *


class Tip:
    def __init__(self, text):
        self.tip = Tk()
        self.tip.overrideredirect(True)  # 隐藏窗口边框
        self.tip.attributes('-alpha', 0.7)  # 设置窗口透明度为50%
        self.tip.geometry('+0+0')  # 设置窗口左下角为显示位置
        self.tip.resizable(False, False)  # 设置窗口大小不可变
        self.tip.configure(bg='black')  # 设置窗口背景颜色为黑色
        self.tip.title('Tip')
        self.label = Label(self.tip, text=text, bg='white', font=('微软雅黑', 12))
        self.label.pack(ipadx=5, ipady=5)

    def show(self):
        self.tip.after(3000, self.hide)  # 3秒后自动销毁窗口
        self.tip.mainloop()

    def hide(self):
        self.tip.destroy()  # 销毁窗口
