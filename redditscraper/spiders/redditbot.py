# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    # allowed_domains = ['www.reddit.com']
    start_urls = ['https://www.reddit.com/']

    def parse(self, response):

        for item in response.css("div.Post"):
            titles = item.css("h2::text").get()
            votes = item.css("._1rZYMD_4xY3gRcSS3p8ODO::text").get()
            times = item.css("._3jOxDPIQ0KaOWpzvSQo-1s::text").get()
            comments = item.css(".FHCV02u6Cp2zYL0fhQPsO::text").get()
            yield {
                'title':titles,
                'vote':votes,
                'time': times,
                'comment':comments,
            }
