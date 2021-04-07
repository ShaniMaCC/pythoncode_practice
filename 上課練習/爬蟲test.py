import tkinter as tk
import bs4, requests



window = tk.Tk()
window.title('電影時刻')
window.geometry('1040x800')
window.configure(background='gray')

def movie_search(): #用headers偽裝成瀏覽器下載網頁
    headers01 = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
                Safari/537.36', }
    url = 'https://movies.yahoo.com.tw/movie_intheaters.html' #我們決定以yahoo電影作為專案的網頁
    html = requests.get(url, headers=headers01)
    print("網頁下載中 ...")
    html.raise_for_status()                                                  
    print("網頁下載完成")
    
    yahoo = bs4.BeautifulSoup(html.text, 'lxml') 
    
    info = yahoo.find_all('div', {'class':'release_movie_name'},limit=3) 
    #首先我們用find_all在div裡的moviename抓取電影名稱 限制只有三個
    names=[] #新增一個空的清單會把找到的電影名稱放到這裡

    for i in range(len(info)):#用for迴圈抓取我們需要的資料
        name=info[i].find('a').text #首先先找到我們要抓取的目標資料所在標籤
        name=name[19:len(name)]#這部分是將多餘的資料去除選出我們要的電影名稱
        names.append(name)#新增至name清單裡
    print(names)
    result001_label.configure(text=names[0])
    result002_label.configure(text=names[1])
    result003_label.configure(text=names[2])       
    
    
    
    
    date = yahoo.find_all('div', {'class':'release_movie_time'},limit=3)
    time = []
  
    for i in range(len(date)):
          dates=(date[i].text)
          time.append(dates)
    print(time)
    result004_label.configure(text=time[0])
    result005_label.configure(text=time[1])
    result006_label.configure(text=time[2])       
    
    point = yahoo.find_all('dl', {'class':'levelbox'},limit=3)
    level = []
    
    for i in range(len(point)):
        levels=(point[i].find('span').text)
        level.append(levels)
    print(level)
    result007_label.configure(text=level[0])
    result008_label.configure(text=level[1])
    result009_label.configure(text=level[2]) 
    

def clean():
    result001_label.configure(text='')
    result002_label.configure(text='')
    result003_label.configure(text='')
    result004_label.configure(text='')
    result005_label.configure(text='')
    result006_label.configure(text='')
    result007_label.configure(text='')
    result008_label.configure(text='')
    result009_label.configure(text='')       
        
   
    
    
header_label = tk.Label(window, text='近期上映', font=('Arial', 30))
movie_btn = tk.Button(window, text='馬上查詢', command=movie_search, font=('Arial', 30))
clean_btn = tk.Button(window, text='清除', command=clean, font=('Arial', 30))
name_label = tk.Label(window, text='電影名稱', font=('Arial', 30))
time_label = tk.Label(window, text='上映日期', font=('Arial', 30))
point_label = tk.Label(window, text='觀眾期待度', font=('Arial', 30))
result001_label = tk.Label(window, font=('Arial', 20), width=10, height=1 )
result002_label = tk.Label(window, font=('Arial', 20), width=10, height=1 )
result003_label = tk.Label(window, font=('Arial', 20), width=10, height=1 )
result004_label = tk.Label(window, font=('Arial', 12), width=20, height=1 )
result005_label = tk.Label(window, font=('Arial', 12), width=20, height=1 )
result006_label = tk.Label(window, font=('Arial', 12), width=20, height=1 )
result007_label = tk.Label(window, font=('Arial', 20), width=10, height=1 )
result008_label = tk.Label(window, font=('Arial', 20), width=10, height=1 )
result009_label = tk.Label(window, font=('Arial', 20), width=10, height=1 )
# 版面配置
header_label.grid(row=0, column=0, columnspan=4)
movie_btn.grid(row=1, column=0)
clean_btn.grid(row=1, column=3)
name_label.grid(row=2, column=0)
# name_label.grid(row=2, column=1)
# name_label.grid(row=2, column=2)
result001_label.grid(row=2, column=1)
result002_label.grid(row=2, column=2)
result003_label.grid(row=2, column=3)
time_label.grid(row=3, column=0)
result004_label.grid(row=3, column=1)
result005_label.grid(row=3, column=2)
result006_label.grid(row=3, column=3)
point_label.grid(row=4, column=0)
result007_label.grid(row=4, column=1)
result008_label.grid(row=4, column=2)
result009_label.grid(row=4, column=3)

window.mainloop()