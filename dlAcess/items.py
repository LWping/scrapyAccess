# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DlacessItem(scrapy.Item):
    # define the fields for your item here like:
    area = scrapy.Field()
    year = scrapy.Field()
    quarter = scrapy.Field()
    company_name = scrapy.Field()
    unicode = scrapy.Field()
    org_code = scrapy.Field()
    register_address = scrapy.Field()
    corporation = scrapy.Field()
    case_nature = scrapy.Field()
    break_situation = scrapy.Field()
    punish_situation = scrapy.Field()
    issue_organ = scrapy.Field()
