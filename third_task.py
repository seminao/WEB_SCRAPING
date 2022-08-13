import requests
import json
from bs4 import BeautifulSoup
rel=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(rel.content,"html.parser")
movies=soup.find("tbody",class_="lister-list",).find_all("tr")
list=[]
for movie in movies:
    dic={"movie":"","year":"","rating":"","position":"","link":""}
    name=movie.find('td',class_="titleColumn").a.text
    ratings=movie.find('td',class_="ratingColumn imdbRating").strong.text
    position=movie.find("td",class_='titleColumn').get_text(strip=True).split('.')[0]
    year=movie.find("td",class_="titleColumn").span.text.strip("()")
    url=movie.find("td",class_="titleColumn").a["href"]
    link="https://www.midb.com/"+url
    dic["movie"]=name
    dic["year"]=year
    dic["rating"]=ratings
    dic["position"]=position
    dic["link"]=link
    list.append(dic)
answer_dic={}
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
i=0
while i<len(list):
    if list[i]["year"]>="1950" and list[i]["year"]<="1959":
        list1.append(list[i])
        answer_dic["1950"]=list1
    if list[i]["year"]>="1960" and list[i]["year"]<="1969":
        list2.append(list[i])
        answer_dic["1960"]=list2
    if list[i]["year"]>="1970" and list[i]["year"]<="1979":
        list3.append(list[i])
        answer_dic["1970"]=list3
    
    if list[i]["year"]>="1980" and list[i]["year"]<="1989":
        list4.append(list[i])
        answer_dic["1980"]=list4
    if list[i]["year"]>="1990" and list[i]["year"]<="1999":
        list5.append(list[i])
        answer_dic["1990"]=list5
    
    if list[i]["year"]>="2000" and list[i]["year"]<="2009":
        list6.append(list[i])
        answer_dic["2000"]=list6   
    i=i+1
with open("imdb 3_task.json","w")as f:
    json.dump(answer_dic,f,indent=8)
    
    
    
# import json
# f=open("Movie_year.json")
# year=json.load(f)
# def group_by_decade():
#     year_1=1955
#     dict={}
#     for i in range(year_1,2022,10):
#         movies_list=[]
#         for j in year:
#             if year_1<int(j) and int(j)<(year_1+10):
#                 movies_list.append(year[j])
#         dict[year_1]=movies_list  
#         year_1+=10
#     with open ("task3.json","w") as f1:
#         json.dump(dict,f1,indent=5)
# group_by_decade()