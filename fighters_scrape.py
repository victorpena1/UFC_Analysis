import time
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
client = MongoClient()
# Access/Initiate Database
db = client['ufc_database']
# Access/Initiate Table
tab = db['fighters']
fighters_lst = set([])
for x in range(1,20):
    av = 'http://ufcstats.com/statistics/events/completed'
    path = '?page={}'.format(x)
    url = av+path
    req = requests.get(url)
    print('Retrieving', url)
    soup = BeautifulSoup(req.text, 'html.parser')
    lst = soup.find_all('a', class_="b-link b-link_style_black") 
    time.sleep(2)

    for y in lst:
        url2 = y['href']
        req2 = requests.get(url2)
        print('Retrieving', url2)
        soup2 = BeautifulSoup(req2.text, 'html.parser')
        lst2 = soup2.find_all('a', class_="b-link b-link_style_black") 
        time.sleep(2)

        for z in lst2:
            url3 = z['href']
            req3 = requests.get(url3)
            if z.text.strip() in fighters_lst:
                print('On record')
                time.sleep(2)
                continue
            else:
                print('Retrieving', url3)
                tab.insert_one({'fighter': z.text.strip(), 'raw_fighter': req3.text})
                fighters_lst.add(z.text.strip())
                time.sleep(2)
f_lst =list(fighters_lst)
print(f_lst)
tab.insert_one({'fighter_lst': f_lst})




