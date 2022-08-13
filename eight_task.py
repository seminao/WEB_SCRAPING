import json 
from bs4 import BeautifulSoup
with open ("imdb 1_task.json","r") as f:
    a=json.load(f)
i=0
while i<len(a):
    l=a[i]["url"]
    k=l[-10:-1]
    i=i+1
    f=open(k+".json","w") 
    json.dump(a[i],f,indent=2)