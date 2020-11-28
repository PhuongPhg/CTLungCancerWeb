from urllib.parse import unquote
from selenium import webdriver
from pprint import pprint
import csv
import json

driver = webdriver.Firefox()

driver.get('https://duckduckgo.com/?q=lung+cancer+ct+scan&t=h_&iax=images&ia=images')

img_urls = driver.find_elements_by_class_name('tile--img__img')

links = []
titles = []
for tag in img_urls:
    src = tag.get_attribute('data-src')
    src = unquote(src)
    src = src.split('=', maxsplit=1)
    src = src[1]
    title = tag.get_attribute('alt')
    links.append(src)
    titles.append(title)
driver.close()
pprint(links)
pprint(titles)

f = csv.writer(open('duckduckgo.csv','w',newline='',encoding='utf-8'))
f.writerow(['Title','Link'])
for i in range(len(img_urls)):
    f.writerow([titles[i],links[i]])
