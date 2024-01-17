# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join, MapCompose
from w3lib.html import remove_tags


class LtwSpiderItem(scrapy.Item):
    title = scrapy.Field()
    category = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    
