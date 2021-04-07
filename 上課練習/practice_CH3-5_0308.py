
#4-2雙向選擇結構及多重選擇結構
# cost=int(input('請輸入商品金額'))
# num=int(input('請輸入購買商品數量'))
# total = cost * num

# if total>=2000 and num>=3:
#     print(int(total*0.63))

# elif total >=2000: 
#     print(int(total*0.9))       

# else:
#     print(total) 
    
    
# if total>=2000:
#     if num>=3:
#         print(int(total*0.63))
#     else:
#         print(int(total*0.9))
# else:
#     print(total)
    
    
#4-3多重選擇結構 
# cm=float(input('請輸入身高為幾公分? '))
# kg=float(input('請輸入體重為幾公斤? '))
# m=cm/100
# BMI = kg/(m**2)

# if BMI<18:
#     print(BMI,'體重過輕')
# elif BMI<24:
#     print(BMI,'體重正常')
# elif BMI<27:
#     print(BMI,'體重過重')
# else:
#     print(BMI,'體重肥胖')    




# #5-1for迴圈
# s=[]
# u=input('請輸入ASCII字元? ')
# s=list(u)
# print(s)

# for i in range(0,len(s)):
#     print(ord(s[i]))
    


#5-4

# while True:
#     acc=input('請輸入帳號?  ')
#     pwd=input('請輸入密碼?  ')
    
    
#     if acc=='abc'and pwd=='123':
#         print('登入成功') 
#         break
    
#     else:
#         print('登入失敗，請重新輸入')
#         acc2=input('請重新輸入帳號?  ')
#         pwd2=input('請重新輸入密碼?  ')
        
#         if acc2=='abc'and pwd2=='123':
#             print('登入成功') 
#             break
#         else:
#             print('登入失敗第二次，請重新輸入')
#             acc3=input('請重新輸入帳號?  ')
#             pwd3=input('請重新輸入密碼?  ')
         
            
#             if acc3=='abc'and pwd3=='123':
#                 print('登入成功') 
#                 break
#             else:
#                 print('帳號密碼登入超過三次，登入失敗')
#                 break
# # %%
# a='abc'
# p='123'
# x=0    
# while x<3:
#             #從0開始到2共三次
#     x +=1
#     aa=input('請輸入帳號?  ')
#     pp=input('請輸入密碼?  ')
#     if a==aa and p==pp:
#         print('登入成功') 
#         break
#     elif aa!=a and pp==p:
#         print('帳號輸入錯誤，',3-x,'次機會')
#     elif aa==a and pp!=p:
        
#         print('密碼輸入錯誤，',3-x,'次機會')
#     elif aa!=a and pp!=p:
        
#         print('帳號密碼輸入錯誤',3-x,'次機會')
#     else:
#         print('登入失敗，十分鐘後重新嘗試',3-x,'次機會')
        
#%%

#1=剪刀 2=石頭 3=布 4=離開

# W=0
# L=0
# E=0
# A=[]
# B=[]
# C=[]


# import random
# while True:
    
#     people = int(input('開始猜拳!請輸入1.剪刀/2.石頭/3.布/4.離開    '))
#     com = random.randint(1,3)
#     print(type(people))
  
#     if people==1 and com==3:
#         A.append('W')
#         print('這把我出剪刀，總共贏電腦',len(A),'次')
#     elif people==2 and com==1:
#         A.append('W')
#         print('這把我出石頭，總共贏電腦',len(A),'次')
#     elif people==3 and com==2:
#         A.append('W')
#         print('我出布，總共贏電腦',len(A),'次')
#     elif people==com:
#         B.append('E')
#         print('我們平手目前贏電腦', len(A), '平手', len(B), '次')
#     elif people== 4:
#         print('離開遊戲')
#         break
#     else:
#         C.append('L')
#         print('我輸了目前贏電腦', len(A), '平手', len(B), '輸了', len(C), '次')
# # P=(len(A) + len(B) + len(C) )     
# print('我的勝率為',(len(A)/(len(A)+len(B)+len(C)))*100,'%')



#%%

while True:
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
    
# for i in range(1,20):
#     for j in range(1,20):
#         print(i,'*',j,'=',i*j,'\t',sep='',end='')
#     print()
    

