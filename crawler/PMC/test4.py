from selenium import webdriver
import csv
import json

driver = webdriver.Edge(executable_path='D:\Study\ICT Year 3\Web Application Development\msedgedriver.exe')
driver.get('https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2176079/')
p_element = driver.find_elements_by_class_name('figure')
f = csv.writer(open('erj_crawl3.csv','w',newline='',encoding='utf-8'))
f.writerow(['Link'])
for i in p_element:
    a_element = i.find_element_by_tag_name("img")
    link = a_element.get_attribute("src")
    
    # print("Link: "+link+"\n")
    f.writerow([link])

driver.quit()
