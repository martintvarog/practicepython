import requests
from bs4 import BeautifulSoup

# "with" open + close statement , open 'simple.html' jako html_file
source = requests.get('https://www.seznam.cz/').text
#var. soup je bs (html.., 'lxml' = zrpacovani souboru s vyuzitim knihony lxml)
soup = BeautifulSoup(source, 'html.parser')
#print(soup.prettify())


#find by clas
for story_heading in soup.find_all(class_="article__title link link--show-visited"):
	#find headline 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())

    else: 
        print(story_heading.contents[0].strip())

print(story_heading)