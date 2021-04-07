#%%
s=input('請輸入一句英文句子  ')
s1=s.title()
s2=s.capitalize()
s3=s.upper()
s4=s.swapcase()
a=s1.split(' ')
print(a[::-1])
print(s2)
print(s3)
print(s4)
# s5=s.replace([0],'pig')
# print(s5)

#%%
全班學生 = set(['john','mary','tina','fiona','claire','eva','ben','bill','bert'])
英文及格 = set(['john','mary','fiona','claire','ben','bill'])
數學及格 = set(['mary','fiona','claire','eva','ben'])
print(英文及格&數學及格) 
print(全班學生-數學及格) #全^數
print(英文及格&(全班學生-數學及格)) #英-數


#%%
a='「紅豆生南國，春來發幾枝？願君多采擷，此物最相思。」<作者：王維>'
b='「春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。」<作者：孟浩然>'
aa=set(a)
bb=set(b)
aa.remove('，')
aa.remove('？')
aa.remove('。')
aa.remove('「')
aa.remove('」')
aa.remove('：')
aa.remove('<')
aa.remove('>')
print(aa)
bb.remove('，')
bb.remove('。')
bb.remove('「')
bb.remove('」')
bb.remove('：')
bb.remove('<')
bb.remove('>')
print(bb)
print(aa&bb)

#%%
S1=str(input('請輸入第一首詩   '))
S2=str(input('請輸入第二首詩   '))
ss1=set(S1)
ss2=set(S2)
ss1.remove('，')
ss1.remove('？')
ss1.remove('。')
ss1.remove('「')
ss1.remove('」')
ss1.remove('：')
ss1.remove('<')
ss1.remove('>')
ss2.remove('，')
ss2.remove('。')
ss2.remove('「')
ss2.remove('」')
ss2.remove('：')
ss2.remove('<')
ss2.remove('>')
print(ss1&ss2)



#%%
n=[]
e=[]
name=input('請輸入姓名? ')
n.append(name)   #append是針對n的set 所以是n.append ()內中是新增的資料name
email=input('請輸入email? ')
e.append(email)
name=input('請輸入姓名? ')
n.append(name)
email=input('請輸入email? ')
e.append(email)
name=input('請輸入姓名? ')
n.append(name)
email=input('請輸入email? ')
e.append(email)

serch={'查詢姓名':n,'查詢信箱':e}  #再設一個新的set
q=input('請輸入要查詢信箱的姓名?')

姓名=n.index(q)
print(serch['查詢信箱'][姓名])

#姓名 成績 學號

#%%
number=[]
name=[]
score=[]


a=input('輸入學號?')
number.append(a)
b=input('輸入姓名?')
name.append(b)
c=input('輸入成績?')
score.append(c)
a=input('輸入學號?')
number.append(a)
b=input('輸入姓名?')
name.append(b)
c=input('輸入成績?')
score.append(c)
a=input('輸入學號?')
number.append(a)
b=input('輸入姓名?')
name.append(b)
c=input('輸入成績?')
score.append(c)


final={'aa':number,'bb':name,'cc':score}
q=input('請輸入學生學號進行查詢')
serch=number.index(q) #q是number這個set裡面的index序列幾
print(final['bb'][serch],final['cc'][serch])



for 


# pass
# def __init__(self,a,b,c):
#     self.a = a
#     self.b = b
#     self.c = c
    



















