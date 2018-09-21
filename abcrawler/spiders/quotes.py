# -*- coding: utf-8 -*-
import scrapy
from abcrawler import models
from abcrawler.items import QuoteItem
import datetime



class QuotesSpider(scrapy.Spider):
    name = "quotes"
    url = input("please enter a valid url : ")
    # url = 'http://quotes.toscrape.com/page/1/'
    start_urls = [
            url,
    ]


    def parse(self, response):
        quotes = response.css('div.quote')

        for quote in quotes:
            text = quote.css('span.text::text').extract_first()
            author = quote.css('small.author::text').extract_first()
            tags = quote.css('div.tags a.tag::text').extract()
            # “ ”
            
            mod_text =  text[1:-1]
            quote_data = QuoteItem()
            quote_data['quote'] = ''.join(mod_text)
            quote_data['author'] =''.join(author)
            quote_data['tag'] =''.join(tags)
            quote_data['created_date'] = datetime.datetime.now()
            yield quote_data

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
