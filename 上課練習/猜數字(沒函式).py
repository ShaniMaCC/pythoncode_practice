# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 18:27:27 2021

@author: MCU
"""


import random
x=[]
x = random.sample(range(0,10),4)
print(x)

while True:
        
        y = input('開始猜數字,請輸入四位數字0-9 ')
        z = list(y)    #input出來是字串,先轉成list
        count=len(z)
        if count == 4:
            for i in range(4): #這裡的for迴圈,是在把z再轉回整數 
                z[i] = int(z[i])
            if z[0] == z[1] or z[0] == z[2] or z[0] == z[3] or z[1] == z[2] or z[1] == z[3] or z[2] == z[3]:
                print("數字間不可以重複喔,請重新輸入")
                continue
                
            A = 0
            for i in range(0,4):
                if x[i] == z[i]:
                    A += 1
                    
            B = 0
            for i in range(0,4):
                for j in range(0,4):
                    if i != j:
                        if x[i] == z[j]:
                            B += 1 
                
            print(A,"A",B,"B")
            if A == 4:
                print("BINGO,你答對了")
                break
        else:
            print("請輸入四個數字就好了喔")
            continue