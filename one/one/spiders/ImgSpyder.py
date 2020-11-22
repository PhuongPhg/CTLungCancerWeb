import scrapy
from one.items import ImageItem
class ImgSpider(scrapy.spiders.Spider):
    name = "img_spider"
    start_urls = ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4419420"]

    def parse(self, response):
        image = ImageItem()
        img_urls = []
        partialLink = "https://www.ncbi.nlm.nih.gov/"
        imageURL = response.css(".figure img::attr(src)").extract()
        for img in imageURL:
            fullImgLink = partialLink + img
            title = response.css(".icnblk_cntnt a::text").extract()
            caption = response.css(".caption p::text").extract()
            img_urls.append(fullImgLink)
            image["image_urls"] = img_urls
        yield ImageItem(title=title, caption=caption, image_urls=[image])
