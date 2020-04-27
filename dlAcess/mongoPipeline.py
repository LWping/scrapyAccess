#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wping
# create_time:
from pymongo import MongoClient


class DlacessMongoPipeline(object):

    def __init__(self, settings):
        self.settings = settings

    def process_item(self, item, spider):
        if spider.name == "allow":
            detail_item = dict(item)
            self.db['allow_publicity'].insert(detail_item)
        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        # 连接数据库
        dbserver = self.settings.get['MONGODB_SERVER']
        dbport = self.settings.get['MONGODB_PORT']
        dbname = self.settings.get['MONGODB_DB']
        client = MongoClient(dbserver, dbport)
        self.db = client[dbname]

    def close_spider(self, spider):
        pass
