# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Lưu dữ liệu vào databases 
# Typical uses of item pipelines are:

#     +cleansing HTML data
#     +validating scraped data (checking that the items contain certain fields)
#     +checking for duplicates (and dropping them)
#     +storing the scraped item in a database


class WorldometersCrawlPipeline(object):
    def process_item(self, item, spider):
        return item
