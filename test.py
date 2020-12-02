from bs4 import BeautifulSoup
import requests
import urllib.request
import csv
import json 
url = "https://medpix.nlm.nih.gov/search?allen=true&allt=true&alli=true&query=lung%20cancer"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

aas = soup.find_all("img", class_='image ng-scope')
print(aas)
