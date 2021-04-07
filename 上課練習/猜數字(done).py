# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:14:10 2021

@author: MCU
"""
from tkinter import messagebox,scrolledtext
import tkinter as tk
import random


x=[]
x = random.sample(range(0,10),4)
print(x)
A=0
B=0
def calla(zz):
        global A,x   
        A = 0
        for i in range(0,4):
            if x[i] == zz[i]:
                A += 1
        return A
def callb(ww):
        global B,x                    
        B = 0
        for i in range(0,4):
            for j in range(0,4):
                if i != j:
                    if x[i] == ww[j]:
                        B += 1 
            return B



def AB():
    # global x
    # while True:     
    y = input_entry.get()
    z = list(y)    #input出來是字串,先轉成list
    count=len(z)
    if count == 4:
        for i in range(4): #這裡的for迴圈,是在把z再轉回整數 
            z[i] = int(z[i])
        # if z[0] == z[1] or z[0] == z[2] or z[0] == z[3] or z[1] == z[2] or z[1] == z[3] or z[2] == z[3]:
            # print("數字間不可以重複喔,請重新輸入")
            # continue
        aa=calla(z)
        bb=callb(z)
                
        R= aa,"A",bb,"B"
        resultt=str(aa)+"A"+str(bb)+"B"
        if aa == 4:
            R="BINGO,你答對了"
            result_label.configure(text=R)
        history_h.insert("end",y+":"+resultt+"\n")
    else:
        messagebox.showinfo("錯誤","請輸入四個數字就好了喔")
            # continue
    # result_label.configure(text=R)
    
window = tk.Tk()
window.title('?A?B')
window.geometry('800x600')
window.configure(background='light blue')

        
header_label = tk.Label(window, text='?A?B' , font=('Arial',20))
input_label = tk.Label(window, text='輸入', font=('Arial',20))
input_entry = tk.Entry(window, font=('Arial',15))
guess_btn = tk.Button(window, text='開始猜數字\n請輸入四位數字0-9', command= AB, font=('Arial',20))
result_label = tk.Label(window, font=('Arial',15),width=20,height=6)
history_h =tk.scrolledtext.ScrolledText(window,wrap='word',height=10,width=22,font=('Arial',12))
history_h.insert("end",'history:\n')

#版面
header_label.grid(row=0, column=0 ,columnspan=2)
input_label.grid(row=1, column=0)
input_entry.grid(row=1, column=1)
guess_btn.grid(row=2, column=0)
result_label.grid(row=2,column=1)
history_h.grid(row=3,column=1,columnspan=2)


window.mainloop()        
        
        
        
        

    