from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.timeout.com/film/best-movies-of-all-time")
data_file = response.text

soup = BeautifulSoup(data_file,"html.parser")
film_titles = soup.find_all(name="h3", class_="_h3_cuogz_1")
film_list = []
with open("film.txt","w") as file:
    for title in film_titles:
        file.write(f"{title.getText()}\n")
