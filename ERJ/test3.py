from selenium import webdriver
import csv
import json
# The webdriver is based on which web browser you use, please install a new one on your pc
driver = webdriver.Edge(executable_path='D:\Study\ICT Year 3\Web Application Development\msedgedriver.exe')
driver.get('https://erj.ersjournals.com/content/19/4/722.figures-only')
p_element = driver.find_elements_by_class_name('fig-inline-img')
# img_urls = []
# img_titles = []
f = csv.writer(open('erj_crawl.csv','w',newline='',encoding='utf-8'))
f.writerow(['Title','Link'])
for i in p_element:
    a_element = i.find_element_by_tag_name("a")
    title = a_element.get_attribute("title")
    link = a_element.get_attribute("href")
    # img_urls.append(link)
    # img_titles.append(title)
    print("Link: "+link+"\n"+"Title: "+title+"\n")
    f.writerows([title,link])

driver.quit()
