import scrapy
class ImageItem(scrapy.Item):
    images = scrapy.Field()
    image_urls = scrapy.Field()
