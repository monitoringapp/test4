from extruct.w3cmicrodata import MicrodataExtractor
from .base_spider import BaseSpider


class EbaySpider(BaseSpider):
    name = "ebay"
    allowed_domains = ["ebay.com"]

    def parse(self, response):
        extractor = MicrodataExtractor()
        properties = extractor.extract(response.text).get('items')[0].get('properties', {})
        item = {}
        item['title'] = properties.get('name')
        item['price'] = properties.get('offers', {}).get('properties', {}).get('price')
        if 'aggregateRating' in properties:
            item['rating'] = properties.get('aggregateRating', {}).get('properties', {}).get('ratingValue')
        yield item