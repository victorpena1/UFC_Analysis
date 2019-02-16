import time
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
client = MongoClient()
# Access/Initiate Database
db = client['ufc_database']
# Access/Initiate Table
tab = db['events']

for x in range(1,20):
    av = 'http://ufcstats.com/statistics/events/completed'
    path = '?page={}'.format(x)
    url = av+path
    req = requests.get(url)
    print('Retrieving', url)
    soup = BeautifulSoup(req.text, 'html.parser')
    lst = soup.find_all('a', class_="b-link b-link_style_black") 
    time.sleep(3)

    for y in lst:
        url2 = y['href']
        req2 = requests.get(url2)
        print('Retrieving', url2)
        tab.insert_one({'event_name': y.text.strip(), 'raw_event': req2.text})
        time.sleep(3)


