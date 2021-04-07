import bs4, requests

headers01 = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'https://movies.yahoo.com.tw/movie_intheaters.html'
html = requests.get(url, headers=headers01)
print("網頁下載中 ...")
html.raise_for_status()                             # 驗證網頁是否下載成功                      
print("網頁下載完成")

yahoo = bs4.BeautifulSoup(html.text, 'lxml') 

info = yahoo.find_all('div', {'class':'release_movie_name'},limit=3)
names=[]
for i in range(len(info)):
    name=info[i].find('a').text
    name=name[19:len(name)]
    names.append(name)
print(names)

date = yahoo.find_all('div', {'class':'release_movie_time'},limit=3)
time = []
for i in range(len(date)):
      dates=(date[i].text)
      time.append(dates)
print(time)
      

point = yahoo.find_all('dl', {'class':'levelbox'},limit=3)
level = []
for i in range(len(point)):
    levels=(point[i].find('span').text)
    level.append(levels)
print(level)



# like = yahoo.select('#')
# level2 = []
# for i in range(len(like)):
#     like2=like[i].find('class')
#     print(like2)
#     # name=name[19:len(name)]
#     # names.append(name)
#     # l2=(like[i])
#     # print(l2)
# #     l2=l2[29:34]
