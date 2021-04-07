# def n():
#     print('hi') 
#     print([1,2,3])
# n()
# def c(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(c(5,10))


# def max(a,b):
#     if a > b:
#         return a
#     else:
#         return b

#%% 
print('最大值為',max(20,15))
#%%     圓的面積
def x(r1):
    return r1**2*3.14 #加入 import math既有的函式可運用math.pi (r1**2*math.pi也可以)
r1=float(input('請輸入圓形的半徑?'))
#ans = x(r1)
#print('圓的面積為',ans)   若要這樣寫 要定義ans
print('圓的面積為',x(r1))

#%% 梯形面積
def x(a,b,c):
    return (a+b)*c/2
a=float(input('請輸入梯形的上底'))
b=float(input('請輸入梯形的底邊'))
c=float(input('請輸入梯形的高'))

print('梯形的面積為',x(a,b,c))

#%% 三角形面積
def x(a,h):
    return a*h/2
a=float(input('請輸入三角形底邊'))
h=float(input('請輸入三角形的高'))

print('三角形面積為',x(a,h))

#%%
import math
x=36
math.sqrt(x)

def x(num):
    j=2
    while j <= math.sqrt(num):
        if (num % j ==0):
            print(num,'被',j,)
            return False
        j += 1
    return True
for i in range (2,101):
    if x(i):
        print(i,'為質數')

#%%
def f(s='a', count=1):
    print(s * count)
f('Hi')
f('Hi',3)
f(3)
f(3,2)
f('3',2)


#%%日期
from datetime import datetime
def ymd():
    now=datetime.now()
    return (now.year,now.month,now.day)
    print(now)
a,b,c = ymd()
print(a,b,c)
print(ymd())
#%%遞迴

def fac(n):
    if n ==1:
        return 1
    else:
        return n*fac(n-1)
q=int(input('請輸入數值?'))
ans = fac(q)
print (q,'!=',fac(q))

for ii in range (1,20,1):
    print(ii,'!=',fac(ii))

#%%費波南西細數
# 1 1 2 3 5 8
# 1+1=2
# 2+1=3
# 3+2=5
# 5+3=8
# 8+5=13

def a(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        ans= a(n-1)+a(n-2)
        return ans
for i in range(1,21):
    print('第',i,'項總和=',a(i))
#%%最大公因數
def gcd(a,b):
    if a == 0 :
        return b
    else:
        return gcd(b%a,a)

a=int(input('請輸入a的數值?'))
b=int(input('請輸入b的數值?')) 

ans=gcd(a,b)
print(a,'與',b,'的最大公因數為',ans,sep='')   

#%%
def sum(a=1,b=10,c=1):
    '''
Args:
    a=第一個參數
    b=第二個參數
    c=第三個參數
Returns:
    回傳加總值

'''
    sum=0
    for i in range(a,b+1,c):
        sum += i
    return sum


help(sum)
print(sum.__doc__) 
print(sum(1,10,1))    

print(__name__)
if __name__=='__main__':
    print('Call it locally')
    print('sum 1 to 10=',sum(1,10,1))

