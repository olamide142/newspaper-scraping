import re
import requests
import json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import sys, time



li ={}


def main():
    print("[+] Started...")
    headlines()


def headlines():
    headlines_url = "https://www.dailytrust.com.ng/headlines"
    check = True
    news = {}
    while check:
        result = requests.get(headlines_url).content
        soup = BeautifulSoup(result, 'lxml')
        for i in (soup.find_all('div', class_="media-body")): 
            link = i.a
            news[link.get_text()] = link.get("href")
            # get the content of each news
            
        check = False
    
    for x,y in enumerate(news.items()):
        li[str(x+1)] = y[1]
        print(f"[{x+1}]  {y[0]}")
    

  


def get_news_content(to_check_date_or_not, link):
    '''Get Html of news page'''
    print('[+] LOADING...')
    # if to_check_date_or_not == None: to_check_date_or_not = False 
    result = requests.get(link).content
    soup = BeautifulSoup(result, 'lxml')

    # Check to see if it the current day only if the user passes True
    # if to_check_date_or_not:
    #     current_date = datetime.now()
    #     current_date = current_date.strftime('%b %d, %Y')
    #     published_on = soup.find('time', class_="published").get_text()
    #     yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%b %d, %Y')
    #     status_on_news_date = yesterday_date in published_on or current_date in published_on
    #     # Return False to the headline function meaning you're done reading yesterday and todays news
    #     if status_on_news_date == False:
    #         return False
    
    # Remove all adverts if the news was from yesterday or today 
    for div in soup.find_all("ins", {'class':'adsbygoogle'}): 
        div.decompose()
    
    # if status_on_news_date:
    if True:
        print('[+] DONE!')
        time.sleep(1.5)

        news_content = soup.find('article')
        print(news_content)


    # download all news image
    # Get content to pdf





if __name__ == "__main__":
    # Get Headline 
    headlines()

    selection = input("Select news by number: ")

    # link to the new selected
    # print(li[selection])

    get_news_content(False, li[selection])
