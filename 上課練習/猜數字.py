import tkinter as tk
import random

window = tk.Tk()
window.title('Guess Number')
window.geometry('800x600')
window.configure(background='light blue')

ans= random.randint(0,100)
guess_count=0
minnum=0
maxnum=99
def guess_number():
    global guess_count
    global ans
    global minnum
    global maxnum
    A = input_entry.get()
    #R = "猜數字(" + str(minnum)+"-"+ str(maxnum) +")"
    guess = int(A)
    guess_count += 1
    if ans == guess:
        # print('你答對了是數字',guess)
        R="你答對了是{}\n你總共猜了{}次".format(str(guess),str(guess_count))
        print(R)
    elif guess > ans:
        R='猜的太大了請繼續'
        maxnum = guess-1
        R+= "("+ str(minnum)+"-"+ str(maxnum) +")"
        print(R)
    else:
        R='猜的太小了請繼續'
        minnum = guess+1
        R+= "("+ str(minnum)+"-"+ str(maxnum) +")"
        print(R)
    result_label.configure(text=R)    


header_label = tk.Label(window, text='Guess Number' , font=('Arial',30))
input_label = tk.Label(window, text='輸入', font=('Arial',30))
input_entry = tk.Entry(window, font=('Arial',30))
guess_btn = tk.Button(window, text='猜猜看', command=guess_number, font=('Arial',30))
result_label = tk.Label(window, font=('Arial',10),width=60,height=6)


#版面
header_label.grid(row=0, column=0 ,columnspan=2)
input_label.grid(row=1, column=0)
input_entry.grid(row=1, column=1)
guess_btn.grid(row=2, column=0)
result_label.grid(row=2,column=1)



window.mainloop()