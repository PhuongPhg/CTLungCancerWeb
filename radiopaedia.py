from bs4 import BeautifulSoup
import requests
import urllib.request
import csv
import json

url = "https://radiopaedia.org/articles/lung-cancer-3"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

aas = soup.find_all("img", class_='media-object centered-image')
bbs = soup.find_all("span", class_='hidden-sm hidden-xs editable-text-on-dark')
# print(aas)

image_src = []
image_script=[]
for a in aas:
  image_src.append(a['src'])

  print(a['src'])

for b in bbs:
  print(b.text)
  image_script.append(b.text)
txt='['
f = csv.writer(open('radiopaedia.json','w',newline='',encoding='utf-8'))
f.writerow(['Title','Link'])
for i in range(len(image_script)):
  txt=txt+'{'+"Title"+':'+image_src[i]+'}'
txt=txt+']'
    # f.writerows(json.dumps([image_script[i],image_src[i]]))
# print(json.dumps(txt))