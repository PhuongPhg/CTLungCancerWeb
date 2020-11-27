import scrapy
class ImageItem(scrapy.Item):
    images = scrapy.Field()
    image_urls = scrapy.Field()
    title = scrapy.Field()
    caption = scrapy.Field()
    files = scrapy.Field()
