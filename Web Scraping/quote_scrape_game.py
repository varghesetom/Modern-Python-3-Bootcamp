'''
When run, the program will scrape a website for a collection of quotes.
It'll pick one at random and display it.
The player will have four chances to guess who said the quote.
After every wrong guess he'll get a hint about the author's identity.
'''

## http://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup
import sys
import io
import re
import random
from time import sleep

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#
base_url = "http://quotes.toscrape.com"
url = "/page/1"
all_quotes = []
while url:
    res  = requests.get(f"{base_url}{url}")
    # print(f"Now Scraping {base_url}{url})")
    soup = BeautifulSoup(res.text, "html.parser")
    quote_all = soup.find_all(class_ = "quote")

    for i in range(len(quote_all)):
        author = quote_all[i].find(class_ = "author").get_text()
        quote = quote_all[i].find(class_ = "text").get_text()
        link = quote_all[i].find("a")["href"]
        all_quotes.append({
            "text": quote,
            "author" : author,
            "link" : link
        })

    next_btn = soup.find(class_ = "next")
    url = next_btn.find("a")["href"] if next_btn else None
    # url = None

    ## Not requesting all the time and overload their server or get caught...
    # sleep(2)
print(all_quotes)

def game():
    print('''Okay, let's play a mini-game where I give you a quote
    and you'll have to tell me who said it. Don't worry, I'll give you
    the list of possible people to narrow down your guesses. Keep in mind,
    you only have 3 guesses!''')
    guess = 4
    magic_quote = random.choice(all_quotes)
    print("\nThe quote is: ", magic_quote["text"])
    print("The people are: \n")
    print([i["author"] for i in all_quotes])
    print("What is your guess?")
    try:
        p1 = input()
        true_quoter = magic_quote["author"]
        while p1.lower() not in true_quoter:
            if p1.lower() in true_quoter.lower():
                print("You got it!")
                break
            guess -= 1
            if guess == 3:
                res = requests.get(f"{base_url}{magic_quote['link']}")
                soup = BeautifulSoup(res.text, "html.parser")
                birthday = soup.find(class_ = "author-born-date").get_text()
                location = soup.find(class_ = "author-born-location").get_text()
                print(birthday)
    except ValueError as e:
        print(e.log())
game()
