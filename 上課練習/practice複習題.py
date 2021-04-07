# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:28:40 2021

@author: MCU
"""


A = 10
B = 20
C = A + B
D = 30
E = A + D
print(E)

#%%
guess_count=0
minnum=0
maxnum=99

import random
ans= random.randint(0,100)
print(ans)
while True:
    A = "猜猜我的年紀是幾歲?(" + str(minnum) +"-"+ str(maxnum)+")"
    guess = int(input(A))
    # guess = int(input("猜猜我的年紀是幾歲?" + str(minnum) +"-"+ str(maxnum) +))  
    guess_count += 1    
    if ans == guess:
        print('你答對了我是',guess,'歲')
        break
    elif guess > ans:
        print('猜的太大了請繼續')
        maxnum = guess-1
    elif guess < ans:
        print('猜的太小了請繼續')
        minnum = guess+1
bingo="你總共猜了"+str(guess_count)+"次"
print(bingo)
#%% 偶數        
n = int(input('請輸入整數數字  '))

def x(a):
    if n % 2 == 0:
        print(n,'is Even')
    else:
        print(n,'is not Even')
        
x(n)

#%%質數

n = int(input('請輸入整數數字  '))

def x(a):
    for i in range (2,n):
        
        if n % i == 0:
            # i+=1
            print(n,'不是質數')
            break
        else :
            print(n,'是質數')
            return
x(n)

#%% 想問秝安
def y(n):
    prime = True
    for i in range (2,n):
        if n % i == 0:
            prime = False
            break
    return prime
s = []
for j in range(2,100):
    if y(j) :
        s.append(j)

print(s)

#%%
Sentence = 'Washington D.C'
Sentence.lower()
print(Sentence.upper())

listS=list(Sentence)
print(listS)
letters=[]
for let in listS:
    if let not in letters:
        letters.append(let)
        
print('有{}種不同字母'.format(len(letters))) #{}裡面是變數後面.format

#%%
#算Histogram,每個字母有幾個
for let in letters:
    print("{}有{}個".format(let,listS.count(let)))

#%%
word = open('test1.txt','r')
line = word.readline()
line = line.lower()
L = line.split()
print(L)
print(len(L),'個單字')
w2 = []
for i in L:
    if i not in w2:
        w2.append(i)

print('有{}種不同的單字'.format(len(w2)))


#%%
word = open('test1.txt','r')
line = word.readline()

L1 = line.split()
L2 = set(L1)
print(type(L2))
L2.remove(',')
