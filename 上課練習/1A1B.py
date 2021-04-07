#產生四位數亂數
#宣告一個空字串變數
#for迴圈i 0~3
#亂數不重複random.sample(range(1,9),1)
# ans=''
# x = str(random.sample(range(0,10),4))
# print(type(x))
# ans += x
# print(ans)



import tkinter as tk
import random

window = tk.Tk()
window.title('Guess Number')
window.geometry('800x600')
window.configure(background='light blue')



ans=''
y = str(random.sample(range(0,10),4))
A=0
def callA(x):
    x = str(number_entry.get())
    for i in range(0,4):
        if ans[i] == x[i]:
            A = A + 1
            return A
        
        
        
        
        
        
        
        
        
        
header_label = tk.Label(window, text='?A?B' , font=('Arial',30))
number_label = tk.Label(window, text='輸入', font=('Arial',30))
number_entry = tk.Entry(window, font=('Arial',30))
guess_btn = tk.Button(window, text='猜猜看', command=callA, font=('Arial',30))
result_label = tk.Label(window, font=('Arial',10),width=60,height=6)
 

#版面
header_label.grid(row=0, column=0 ,columnspan=2)
number_label.grid(row=1, column=0)
number_entry.grid(row=1, column=1)
guess_btn.grid(row=2, column=0)
result_label.grid(row=2,column=1)



window.mainloop()
        