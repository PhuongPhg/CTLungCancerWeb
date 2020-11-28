import scrapy
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
import urllib
import re
class wikimediaSpider(scrapy.spiders.Spider):
    name = 'wikimediaSpider'
    start_urls = ['https://commons.wikimedia.org/w/index.php?search=lung%20cancer%20%22lung%20cancer%22%2C%20%22ct%22%20-house%20filetype%3Abitmap&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%22fields%22%3A%7B%22phrase%22%3A%22%5C%22lung%20cancer%5C%22%2C%20%5C%22ct%5C%22%22%2C%22filetype%22%3A%22bitmap%22%2C%22not%22%3A[%22house%22]%7D%7D&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1&fbclid=IwAR21dTtkml_wxfXCtJgCI1iy3buTgzGhlrleq76IhN8uWN2MIBXbScyZOSw']
    def parse(self, response):
        titles = response.css('.searchResultImage a::attr(title)').extract()
        links = response.css('img::attr(src)').extract()
        for item in zip(titles, links):
            extractedlink = item[1]
            linktransform = re.sub("\\/thumb", "", extractedlink)
            # discard /thumbnail
            originallinks = re.sub("\\/\\d+px.+$", "", linktransform)
            # discard everything after the first .png
            all_items = {
                'Title' : BeautifulSoup(item[0]).text,
                'Link' :  originallinks
            }
            yield all_items
