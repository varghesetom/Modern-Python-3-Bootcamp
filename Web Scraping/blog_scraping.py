# rithmschool.com/blog

import requests
from bs4 import BeautifulSoup
import csv

res = requests.get("https://www.rithmschool.com/blog")
text = res.text.encode("utf-8").decode("ascii", "ignore")

soup = BeautifulSoup(text, "html.parser")
articles = soup.find_all("article")
# print(articles)

with open("blog_links.csv", "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["title", "link", "date"])

    ## Get text from anchor tags within the articles
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        #href - url links
        url = a_tag["href"]
        #date
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])
