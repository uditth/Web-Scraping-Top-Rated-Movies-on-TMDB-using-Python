import requests

urlno=1
count=1
while urlno<501:
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key=0c5df131c1161ab486424d7d2afb54e7&language=en-US&page={urlno}"
    response = requests.get(url)
    abc=response.json()
    f = open("new_movie_list.txt", "a", encoding="utf-8")
    for i in range(20):
        lin=(f"{count}    Movie name:    {abc['results'][i]['original_title']}\n")
        f.write(lin)
        count+=1

    f.close()
    urlno = urlno + 1
print('data added')