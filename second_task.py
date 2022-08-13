
import json
def group_by_year():
    with open("imdb 1_task.json","r") as f:
        a=json.load(f)
        years=[]
        for i in a:
            year=i["year"]
            if year not in years:
                years.append(year)
            years.sort()
            # list comprihansion
        movie_dict={i:[] for i in years}
        for i in a:
            year=i["year"]
            for x in movie_dict:
                if x==year:
                    movie_dict[x].append(i)
            with open("imdb 2_task.json","w") as k:
                json.dump(movie_dict,k,indent=4)
group_by_year()