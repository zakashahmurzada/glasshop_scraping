import scrapy


class GlassShopPySpider(scrapy.Spider):
    name = "glass_shop.py"
    allowed_domains = ["www.myglassesshop.com"]
    start_urls = ["http://www.myglassesshop.com/"]

    def parse(self, response):
        for product in response.xpath('//div[@class="col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item"]'):
            product_url = product.xpath('.//div/div/div/div[@class="product-title p-tab p-tab-13145"]').get()
            # product_image_link = ''
            # product_name = ''
            # product_price = product.xpath('div[@class = "product-title p-tab p-tab-11882"]/span/text()').get()
            
