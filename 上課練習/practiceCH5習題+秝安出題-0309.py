# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:36:28 2021

@author: MCU
"""

#%%
#習題5-39.1
# n=0
# while True:
#     n=int(input('請輸入正整數n '))
#     sum = (n *(n + 1) * (2 * n + 1))/6
#     print(n,'的平方和',sum)
#     break
# 
sum = 0  #不可以寫在迴圈內，不然永遠加總值sum為0  
n=int(input('請輸入正整數n '))
for i in range(1 ,n + 1, 1):# 因為如果不加1,他只會跑到n-1->range(a,b)規則
    sum += (i**2)
print(sum)
#%%
#習題5-39.2
n = 1
while n<1000:
    if (n % 2 != 0) and (n % 3 != 0):
        print(n)
    n += 1    #這行如果不寫就永遠為1
    
#%%
#習題5-39.3
#for 迴圈
sum = 0
for i in range (1 , n+1):
    sum += i**2
    if sum > 1000:
        print('當n=',i,'為最小平方和',sum)
        break
#while迴圈
#%%        
sum = 0
i=1
while True:
    sum += (i**2)
    #i += 1 放這裡會導致在運算的時候會先帶到i所以當i已經到14大於1000了後，
    #他會先跑第47行繼續算i=15,sum此時到判斷時也會大於1000，print出來就會是15    
    if sum > 1000:
        print(i,sum)
        break
    else:
        i += 1
        
#%%
#習題5-40.4        
for i in range(1,20):
    for j in range(1,20):
        print(i,'*',j,'=',i*j,'\t',sep='',end='')
    print()
    
#%%
#習題5-40.5


for i in range(2,1001):#(2~1000每一個數字)
    sum = 1
    for j in range(2,i):#為什麼不是i-1:因為在搜尋因數的時候是不包含自己的本來在for迴圈後面的數字就是不包含#假設所有數字的因數都是2~自己本身
        if (i % j == 0): #判斷2~自己本身是否都被自己整除
            sum += j #如果被整除,sum加因數
        else:
            sum==sum #sum不變
    if (i == sum):
        print(i,'是完全數')


#%%
#習題5-40.6        
#random
import random
while True:
    c=random.randint(1,6)
    x=int(input('擲骰子開始請按1，退出遊戲請按2   '))
    if x == 1 :
        if c < 6:
            print('骰到',x,'電腦骰到',c,'繼續遊戲')
        else:
            print('電腦骰到',c,'結束遊戲')
            break
    elif x== 2 :
        print('不骰了')
        break
#%%
x=1
while True:
    x=int(input('請選1~6的數字'))
    if x == 6:
        print('6')
        break
    else:
        print(x)
        
#%%
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end="")
    print()
for i in range (1,6):
    for j in range (6,i+1,-1):
        print('*',end="")
    print()
    
#%%
#巢狀for迴圈->印出n層等腰三角形
#可以用input n=?
#for i in range (1,n+1)
    # for j in range(n-j,0,-1) $ for j in range(0,2i-1,1)*
for i in range(1,6):
    for j in range(6-i,0,-1): #印 5 4 3 2 1 層
        print(' ',end="")
    for j in range(0,2*i-1,1): #印 0 1 2 3 4 5層
        print('*',end="")
    print()
    
# for i in range(0,6):  #想要問倒著的為什麼還是算五層可是印四層
#     for j in range (6,2*i-1,-1):
#         print('*',end="")
#     print()
# for i in range(0,6):
   