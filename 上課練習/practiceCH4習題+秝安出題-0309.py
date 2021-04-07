# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 15:41:42 2021

@author: MCU
"""

# 習題4-18.1
x=float(input('請輸入眼睛度數'))
if x < 0.9 :
    print('近視')
elif x > 1.5 :
    print('遠視')
else:
    print('正常')
    
# 習題4-18.2
#%%
x=float(input('請輸入X值'))
y=float(input('請輸入Y值'))

if x > 0 and y > 0:
    print('(',x,',',y,')位在第一象限')
elif x > 0 and y < 0:
    print('(',x,',',y,')位在第四象限')
elif x < 0 and y > 0:
    print('(',x,',',y,')位在第二象限')
elif x == 0 and y == 0:
    print('(',x,',',y,')位在座標軸上')
else:
    print('(',x,',',y,')位在第三象限')
    
    
    
#%%
#習題4-19.3

t=float(input('請輸入體溫?')) 

if t < 36:
    print(t,'度，體溫過低')
elif 36 <= t < 38:
    print(t,'度，體溫正常')
elif 38 <= t < 39:
    print(t,'度，體溫有點燒')
else:
        print(t,'度，體溫很燒')

#%%
#習題4-20.4

while True: #這題可不放while迴圈 
    
    y=int(input('請輸入年份?'))
    
    if y%4 !=0:
        print('不是閏年')
    elif y%4==0 and y%100 !=0:
        print('是閏年')
    elif y%100==0 and y%400!=0:
        print('不是閏年')
    elif y%400==0:
        print('是閏年')

#%%

c=int(input('請輸入國文成績'))
e=int(input('請輸入英文成績'))
m=int(input('請輸入數學成績'))

if c > 90 and e > 90 and m > 90:
    print('你好棒喔全能資優生')
elif c >= 60 and e >= 60 and m >= 60:
    if c > 90 and e > 90:
        print('雙語資優')
    elif e > 90 and m > 90:
        print('英數資優')
    elif c > 90 and m > 90:
        print('國數資優')
    else:
        print('還不錯拉')
elif c < 60 or e < 60 or m < 60:
    print('下次再加油')
else:
    print('多多努力喔')    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
