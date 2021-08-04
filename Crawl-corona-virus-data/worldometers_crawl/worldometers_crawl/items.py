# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html



# File items.py được sử dụng để khai báo những dữ liệu mà mình muốn thu thập.
# Trong file này có class CrawlItem là class được kế thừa từ class Item của Scrapy. 
# Trong class này đã định nghĩa trước một số đối tượng mà Scrapy cần dùng để thu thập dữ liệu.


import scrapy


class WorldometersCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    total_cases = scrapy.Field()
    daily_new_cases = scrapy.Field()
    daily_new_deaths = scrapy.Field()
    daily_new_recoverd = scrapy.Fiedl()