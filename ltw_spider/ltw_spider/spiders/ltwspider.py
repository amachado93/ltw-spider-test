import scrapy
from ltw_spider.items import LtwSpiderItem

class LtwspiderSpider(scrapy.Spider):
    name = "ltwspider"
    allowed_domains = ["libertythroughwealth.com"]
    start_urls = ["https://libertythroughwealth.com/category/topics/"]

    def parse(self, response):
        articles = response.css('article.item')
        for article in articles:
            art_url = response.css('h2.grid-title>a').attrib['href']
            yield scrapy.Request(art_url, callback=self.parse_article_page)
            
        
        next_page = response.css('a.next ::attr(href)').get()
        if next_page is not None:
            next_page_url = response.css('a.next ::attr(href)').get()
            yield response.follow(next_page_url, callback=self.parse)

    def parse_article_page(self, response):
        article_item = LtwSpiderItem()
        article_item['title'] = response.css('h1.post-title ::text').get()
        article_item['category'] = response.css('a.penci-cat-name ::text').get()
        article_item['author'] = response.css('a.author-url ::text').get()
        article_item['date'] = response.css('.post-box-meta-single > span:nth-child(2) ::text').get()
        article_item['content'] = response.css('.inner-post-entry ::text').getall()
        yield article_item