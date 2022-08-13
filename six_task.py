# import json
# with open('imdb 5task.json','r') as f:
#     a=json.load(f)
# dic={}
# i=0
# eng=0
# h=0
# t=0
# te=0
# while i<len(a):
#     if a[i]['language']=='English':
#         eng=eng+1
#         dic['english']=eng
#     if  a[i]['language']=='Hindi':
#         h=h+1
#         dic['Hindi']=h
    
#     if  a[i]['language']=='Tamil':
#         t=t+1
#         dic['Tamil']=t
#     if  a[i]['language']=='Telugu':
#         te=te+1
#         dic['Telugu']=t
        
#     i=i+1
# with open('imdb 6_task.json','w')as f:
#     json.dump(dic,f,indent=6)

import json
with open('imdb 5_task.json','r') as f:
    a=json.load(f)
dic={}
i=0
c=0
eng=0
h=0
t=0
te=0
while i<len(a):
    if a[i]['language'] in dic:
        dic[a[i]['language']]+=1
    else:  
        dic[a[i]['language']]=1
    i=i+1
with open('imdb 6_task.json','w')as f:
    json.dump(dic,f,indent=6)