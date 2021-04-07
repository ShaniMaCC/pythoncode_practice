# 上衣=int(input('請輸入上衣數量?'))
# 褲子=int(input('請輸入褲子數量?'))
# 背心=int(input('請輸入背心數量?'))
# 總金額=上衣*300+褲子*350+背心*400
# print('訂購服裝的總金額為',總金額)



# s1='abcdefghijk'
# print('s1=','s1[1:]',s1[1:])
# print('s1=','s1[-2:]',s1[-2:])
# print('s1=','s1[1:4]',s1[1:4])
# print('s1=','s1[1:2]',s1[1:2])
# print('s1=','s1[-4:-2]',s1[-4:-2])
# print('s1=','s1[-2:-4]',s1[-2:-4])
# print('s1=','s1[7:-2]',s1[7:-2])
# print('s1=','s1[-2:7]',s1[-2:7])
# print('s1=','s1[::-2]',s1[::-2])
# print('s1=','s1[::-4]',s1[::-4])
# print('s1=','s1[::-1:2]',s1[::-1:2]


# t3 = (1,2,3)
# a,b,c= t3
# print('a=',a,'b=',b,'c=',c)
# t4 = (t3,4,5,6)
# print(t4)
# t5 = (t4,7,8)
# print(t5+t4)
# t6 = t5 + t4




# list=['牛奶','蛋','咖啡豆','西瓜','鳳梨']
# list.insert(0,'蘋果')
# list2=list.copy()
# print(list2)

# for aa in list:
#     if (aa=='蛋'):
         
#         print('蛋在這條串列中.')



# a={'蘋果':'Apple','書':'Book'}
# print('蘋果的英文為',a['蘋果'])
# print('香蕉的英文為',a.get('香蕉'))
# print('香蕉的英文為',a.get('香蕉','不在字典內'))

# b={'早安':'Good Morning','你好':'Hello'}
# for ch,en in b.items():
#     print(b)
# for k in b.keys():
#      print(k,b[k])
# for k in b.keys():
#     print(k)    
# for c in b.values():
#     print(c)


# Q = []
# A= input('請輸入代辦事項?')
# Q.append(A)
# A= input('請輸入代辦事項?')
# Q.append(A)
# A= input('請輸入代辦事項?')
# Q.append(A)
# A= input('請輸入代辦事項?')
# Q.append(A)
# A= input('請輸入代辦事項?')
# Q.append(A)
# print(Q.pop(0),Q.pop(0),Q)
# print(Q.pop(),Q)



# Ans = 'Y'
# while (Ans!='N'):    
#     dic = {'dog':'狗','fish':'魚','cat':'貓','pig':'豬'}
#     q =input('請輸入英文單字')
#     print(dic.get(q,'找不到單字'))
#     found =dic.get(q)
#     if (type(found) == type(None)):
#         q2 = input('要新增至字典嗎?(Y/N)')
#         if (q2 == 'Y'):
#             ans2= input('請輸入中文名稱: ')
#         dic[q]= ans2
#         print(dic)
#     Ans=input('還要查詢嗎?(Y/N)')
    
# Ans = 'Y'
# while (Ans!='N'):    
#     dic = {'dog':'狗','fish':'魚','cat':'貓','pig':'豬'}
#     q =input('請輸入英文單字')
#     print(dic.get(q,'找不到單字'))
#     found =dic.get(q)
#     if (found == None):
#         q2 = input('要新增至字典嗎?(Y/N)')
#         if (q2 == 'Y'):
#             ans2= input('請輸入中文名稱: ')
#         dic[q]= ans2
#         print(dic)
#         # if (ans2=='N'):
#         #     ans3= input('還要查詢嗎?')
#     Ans=input('還要查詢嗎?(Y/N)') 


# a = set('我是女生。')
# b = set('他是男生。')
# print(a)
# print(b)
# print(a | b) #同下方，兩者一樣
# print(b | a) 
# print(a & b) #同下方，兩者一樣
# print(b & a)
# print(a - b)
# print(b - a)
# print(a ^ b)
# print(b ^ a)



