import time
import requests
import json
from bs4 import BeautifulSoup
with open('imdb 1_task.json','r') as f:
    a=json.load(f)
url_list=[]
for i in a:
    url_list.append(i['url'])
# b=url_list[:25]
list=[]
for j in url_list:
    time.sleep(1)
    rel=requests.get(j)
    soup=BeautifulSoup(rel.content,"html.parser")
    con=soup.find('script',type='application/ld+json').text
    h=json.loads(con)
    dic={}
    for k in h:
        dic['name']=h['name']
        dic['director']=h['director'][0]['name']
        dic['image']=h['image']
        dic['description']=h['description']
        dic["language"]=h['review']['inLanguage']
        dic['genre']=h['genre']
        dic['country']='india'
    list.append(dic)

with open('imdb 5_task.json','w') as file:
    json.dump(list,file,indent=8)
    
    
