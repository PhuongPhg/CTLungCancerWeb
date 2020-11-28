import scrapy
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
import urllib
class YandexSpider(scrapy.spiders.Spider):
    name = 'crawlImages'
    start_urls = ['https://yandex.com/images/search?text=lung%20cancer%20ct%20scan']
    def parse(self, response):
        titles = response.css('img::attr(alt)').extract()
        links = response.css('img::attr(src)').extract()
        for item in zip(titles, links):
            all_items = {
                'Title' : BeautifulSoup(item[0]).text,
                'Link' :  "https:" + item[1]
            }
            print(item[1])
            yield all_items
