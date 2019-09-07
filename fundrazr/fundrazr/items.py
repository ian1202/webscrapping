# -*- coding: utf-8 -*-

# Define the models for your scraped items


import scrapy

class FundrazrItem(scrapy.Item):
	campaignTitle = scrapy.Field()
	amountRaised = scrapy.Field()
	goal = scrapy.Field()
	currencyType = scrapy.Field()
	endDate = scrapy.Field()
	numberContributors = scrapy.Field()
	story = scrapy.Field()
	url = scrapy.Field()
	