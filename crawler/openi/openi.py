import requests
import json
import csv

url = "https://openi.nlm.nih.gov/api/search?it=c&m=1&n=75&query=lung%20cancer"

payload={}
headers = {
  'app-id': '5f769957523f0171b65ae49c',
  'Cookie': 'lbnodeid=859049602.47873.0000'
}

response = requests.request("GET", url, headers=headers, data=payload)
res_json=response.json()
a= json.dumps(res_json)
b=json.loads(a)
# print(b['list'][0]['imgLarge'])
img_src=[]
img_script=[]
for i in range(len(b['list'])):
  img_src.append('https://openi.nlm.nih.gov/'+b['list'][i]['imgLarge'])
  # img_script.append(b['list'][i]['image'])
  c=b['list'][i]['image']
  img_script.append(' '.join(c['caption'].split()[:9])+'...')
# print(img_script)

f = csv.writer(open('openi.csv','w',newline='',encoding='utf-8'))
f.writerow(['Title','Link'])
for i in range(len(img_script)):
    f.writerow([img_script[i],img_src[i]])
