from bs4 import BeautifulSoup
import requests
import urllib.request
import csv
import json 
url = "https://emedicine.medscape.com/article/358433-overview"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

aas = soup.find_all("img", class_='pborder')
bbs = soup.find_all("span", class_='capt')
print(aas)
print(bbs)
image_src = []
image_script=[]
for a in aas:
  image_src.append(a['src'])
  # print(a['src'])
for b in bbs:
  # print(b.text)
  image_script.append(b.text)
print(len(image_src))
print(len(image_script))
f = csv.writer(open('emedicine.csv','w',newline='',encoding='utf-8'))
f.writerow(['Title','Link'])
for i in range(len(image_script)):
    f.writerow([image_script[i],image_src[i]])
