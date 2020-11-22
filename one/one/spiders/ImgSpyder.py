import scrapy
from one.items import ImageItem
class ImgSpider(scrapy.spiders.Spider):
    name = "img_spider"
    start_urls = ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4419420"]

    def parse(self, response):
        image = ImageItem()
        img_urls = []
        partialLink = "https://www.ncbi.nlm.nih.gov/"
        for img in response.css(".figure img::attr(src)").extract():
            fullImgLink = partialLink + img
            img_urls.append(fullImgLink)

        image["image_urls"] = img_urls

        return image
