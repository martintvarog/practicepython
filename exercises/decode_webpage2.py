import requests
from bs4 import BeautifulSoup

# "with" open + close statement , open 'simple.html' jako html_file
source = requests.get('https://www.washingtonpost.com/world/africa/nigeria-massacre-farmers-borno/2020/11/30/f4437886-3317-11eb-9699-00d311f13d2d_story.html').text
#var. soup je bs (html.., 'lxml' = zrpacovani souboru s vyuzitim knihony lxml)
soup = BeautifulSoup(source, 'html.parser')
#print(soup.prettify())


#find by cla
for paragraph in soup.find_all('p'):
    print(paragraph.text)

