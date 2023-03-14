from bs4 import BeautifulSoup
import requests
#import lxml

# with open("website.html", encoding="utf8") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content,'html.parser')
# print(soup.a)
#
# anchor_tags = soup.find_all(name="a")
# print(anchor_tags)
#
# for tag in anchor_tags:
#     print(tag.getText())
data_file = requests.get("https://news.ycombinator.com/")
response = data_file.text

soup = BeautifulSoup(response, 'html.parser')
temp_1 = soup.find_all(name="span",class_="titleline")
article_title = []
article_link = []
for info in temp_1:
    temp = info.find("a")
    article_title.append(temp.getText())
    article_link.append(temp.get("href"))
temp_1 = soup.find_all(name="span", class_="score")
article_scores = [int(score.getText().split()[0]) for score in temp_1]
index_max = article_scores.index(max(article_scores))
print(f"Title: {article_title[index_max]}\nLink: {article_link[index_max]}\nScore:{article_scores[index_max]}")
print(article_scores)
