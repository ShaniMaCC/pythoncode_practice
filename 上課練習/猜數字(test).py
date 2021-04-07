# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:08:45 2021

@author: MCU
"""

import random
ans=[]
for k in range(4):
    xxx = random.sample(range(0,9),4)

    ans = xxx
print(ans) #ans的tpye是list

def calla(c):
    global ans
    While True:    
        x = input('請輸入數字') #這時候x是str
        y = list(x)    
        for j in range(4):
            y[j] = int(y[j])
        
        A = 0
        for i in range(0,4):
            if ans[i] == c[i]:
                A += 1
        # return A
            
        B = 4 - len(set(ans) - set(y))- A
        print(A,'A',B,'B')
        if a == 4:
        break
# print(calla(y))
        
