import requests
from bs4 import BeautifulSoup
import re
import csv

import warnings
warnings.filterwarnings('ignore')

count_2019 = 8
count_2020 = -4
url_list = []

month = [31, 30, 31, 30, 31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31]
count_month = 0

month_list = []

for i in range(15):
    for x in range(1, month[count_month]+1):
        if i < 5:
            if len(str(count_2019)) == 1:
                if len(str(x)) == 1:
                    URL = f'http://rank.ezme.net/?mode=naver&day=2019-0{str(count_2019)}-0{str(x)}'
                    month_list.append(f'20190{str(count_2019)}0{str(x)}')
                elif len(str(x)) ==2:
                    URL = f'http://rank.ezme.net/?mode=naver&day=2019-0{str(count_2019)}-{str(x)}'
                    month_list.append(f'20190{str(count_2019)}{str(x)}')
            elif len(str(count_2019)) == 2:
                if len(str(x)) == 1:
                    URL = f'http://rank.ezme.net/?mode=naver&day=2019-{str(count_2019)}-0{str(x)}'
                    month_list.append(f'2019{str(count_2019)}0{str(x)}')
                elif len(str(x)) ==2:
                    URL = f'http://rank.ezme.net/?mode=naver&day=2019-{str(count_2019)}-{str(x)}'
                    month_list.append(f'2019{str(count_2019)}{str(x)}')
            url_list.append(URL)
        else:
            if len(str(count_2020)) == 1:
                if len(str(x)) == 1:
                    URL = f'http://rank.ezme.net/?mode=naver&day=2020-0{str(count_2020)}-0{str(x)}'
                    month_list.append(f'20200{str(count_2020)}0{str(x)}')
                elif len(str(x)) ==2:
                    URL = f'http://rank.ezme.net/?mode=naver&day=2020-0{str(count_2020)}-{str(x)}'
                    month_list.append(f'20200{str(count_2020)}{str(x)}')
            elif len(str(count_2019)) == 2:
                if len(str(x)) == 1:
                    URL = f'http://rank.ezme.net/?mode=naver&day=2020-{str(count_2020)}-0{str(x)}'
                    month_list.append(f'2020{str(count_2020)}0{str(x)}')
                elif len(str(x)) ==2:
                    URL = f'http://rank.ezme.net/?mode=naver&day=2020-{str(count_2020)}-{str(x)}'
                    month_list.append(f'2020{str(count_2020)}{str(x)}')
            url_list.append(URL)
        
    count_month += 1
    count_2019 += 1
    count_2020 += 1

topic_list = []

for x in url_list:
    topic = []

    response = requests.get(x)
    soup= BeautifulSoup(response.content.decode('utf-8','replace'))
    data = soup.find_all('span','mdl-chip__text')
    for y in data:
        topic.append(y.get_text())

    # print(topic)
    print('--------------------------------------------------------------------------------------')
    print(x)
    
        
    topic_list.append(topic)
cnt=0
cnt2 = 0
for month in month_list:
    
    for time in range(24):
        for rank in range(0,10):
            if (month == '20191026') & (time == 11):
                pass
            elif (month == '20191128') & (time == 6):
                pass
            elif (month == '20191128') & (time == 7):
                pass
            elif (month == '20191211') & (time == 7):
                pass
            elif (month == '20191231') & (time == 8):
                pass
            elif (month == '20200317') & (time == 10):
                pass
            elif (month == '20200327') & (time == 10):
                pass
            elif (month == '20200402') | (month == '20200403') | (month == '20200404') | (month == '20200405') | (month == '20200406') | (month == '20200407') | (month == '20200408') | (month == '20200409') | (month == '20200410') | (month == '20200411') | (month == '20200412') | (month == '20200413') | (month == '20200414') | (month == '20200415'):
                pass
            elif (month == '20200426') & (time == 10):
                pass
            elif (month == '20200430') & (time == 6):
                pass
            elif (month == '20200506') & (time == 10):
                pass
            elif (month == '20200605') & (time == 10):
                pass
            elif (month == '20200705') & (time == 10):
                pass
            elif (month == '20200712') & (time == 10):
                pass
            elif (month == '20200715') & (time == 10):
                pass
            elif (month == '20200725') & (time == 10):
                pass
            elif (month == '20200806') & (time == 0):
                pass
            elif (month == '20200903') & (time == 3):
                pass
            elif (month == '20200903') & (time == 4):
                pass
            elif (month == '20200903') & (time == 5):
               pass
            elif (month == '20200903') & (time == 6):
               pass
            elif (month == '20200903') & (time == 7):
               pass
            elif (month == '20200903') & (time == 8):
               pass
            elif (month == '20200903') & (time == 9):
               pass
            elif (month == '20200903') & (time == 10):
               pass
            elif (month == '20200903') & (time == 11):
               pass
            elif (month == '20200903') & (time == 12):
               pass
            else:
                if len(topic_list[cnt][rank]) != 0:

                    with open('./search_trend1.csv','a') as csvfile:
                        fieldnames = ["날짜","시간","순위","키워드"]
                        csvwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
                        csvwriter.writerow({"날짜":month,"시간":time,"순위":rank+1,"키워드":topic_list[cnt][cnt2]})
                        print([month,time,rank+1,topic_list[cnt][cnt2]])
                        
                else:
                    print('--------------------------------------------------------------------------------------')
                    print('pass')
                    print('--------------------------------------------------------------------------------------')
                cnt2+=1
    cnt+=1
    cnt2 = 0