import scrapy
class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    title = scrapy.Field()
