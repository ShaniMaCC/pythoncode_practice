# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:12:28 2021

@author: MCU
"""

#%% 
#習題page6-31,1
#變數1=輸入密碼
#變數2=計算密碼長度
#變數3=數數字個數
#變數4=數英文(小寫)個數
#變數5=數英文(大寫)個數
#變數6=特殊符號個數


pwd=input('請輸入密碼') #變數1 
#a = len(pwd) #變數2 

def p(x):
    m = 0 #變數3
    e1 = 0 #變數4
    e2 = 0 #變數5
    c = 0 #變數6
    for i in list(pwd):  #for i in range(0,a) 這時候才要設變數2 len if a[i]
        if i >= '0' and i <= '9': #把數字跟英文都當作str(加上' '),電腦會轉換ASCII
            m += 1
        elif i >='a' and i <= 'z':
            e1 += 1
        elif i >='A' and i <= 'Z' :
            e2 += 1
        else :
            c += 1
    
    if c == 0:
        if m == 0 :
            if e1+e2 < 6:
                print('這是不安全的密碼')
            else:
                print('這可能是安全的密碼')
        elif e1 == 0 and e2 == 0 :
            if m < 6:
                print('這是不安全的密碼')
            else:
                print('這可能是安全的密碼')
        else :
            if (m + e1+ e2) < 6:
                print('這是不安全的密碼')
            elif (m + e1 + e2) >= 6 and (m + e1 + e2) < 10:
                print('這是安全的密碼')
            else :
                print('這是非常安全的密碼')
    else:
        print('密碼不可包含特殊符號，請重新輸入')

p(pwd)

# if c == 0 and e1 == 0 and e2 == 0 and m < 6:
#     print('這是不安全的密碼')
# elif c == 0 and e1 == 0 and e2 == 0 and m > 6:
#     print('這可能是安全的密碼')
# elif c == 0 and






#%% 
#習題page6-31,2

b=int(input('請輸入列數?'))
h=int(input('請輸入行數?'))
g=str(input('請輸入要顯示的字元?'))

def x(x,y,z):
    for i in range (1,b+1):
        for j in range (1,h+1):
            print(g,end="")
        print()
    
x(b,h,g)
#print(x(b,h,g)) 這個會錯誤,函式裡面有print外面就不要了




























