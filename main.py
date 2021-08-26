#!/usr/bin/env python3


import requests
from bs4 import BeautifulSoup
import os
import os.path
import string

pages=int(input())
article_type=input()
#pages=1
#article_type="Research Highlight"
for page in range(1,pages+1):
    url=f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={page}"
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all('article')
    os.mkdir(f'Page_{page}')
    os.chdir(f'Page_{page}')
    for i in articles:
        if i.find('span', {"class": "c-meta__type"}).text == article_type:
            hyperlink_tag = i.find('a', {'data-track-action': "view article"})
            link=hyperlink_tag.get('href')
            title=hyperlink_tag.text.strip(' ').translate(str.maketrans(" ", "_", string.punctuation))
            r1 = requests.get("https://www.nature.com" + link)
            soup1 = BeautifulSoup(r1.content, 'html.parser')

            data = soup1.find('div', {"class": "article-item__body"})
            file_name = f'{title}.txt'
            if data is None:
                data=soup1.find('div',{"class":"c-article-body u-clearfix"})
            # print(file_name)
            file = open(file_name, 'wb')
            #try:
            #soup2 = BeautifulSoup(data.content, 'html.parser')
            #page_content = data.find_all('p')
            #for k in page_content:
            #print(k.text)
            file.write(data.text.encode())
            #except:
            #    pass
            file.close()

    os.chdir(os.path.dirname(os.getcwd()))

print("Saved all articles.")
