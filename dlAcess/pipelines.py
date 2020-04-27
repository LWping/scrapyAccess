# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class DlacessPipeline(object):

    taxInsert = "insert into tax_serve_break_law_case(area, year_, quarter_, company_name, " \
                "unicode, org_code, register_address, corporation, case_nature, break_situation, " \
                "punish_situation, issue_organ) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', " \
                " '{}', '{}', '{}', '{}')"

    def __init__(self, settings):
        self.settings = settings

    def process_item(self, item, spider):

        if spider.name == "tax":
            sqltext = self.taxInsert.format(
                pymysql.escape_string(item['area']),
                pymysql.escape_string(item['year']),
                pymysql.escape_string(item['quarter']),
                pymysql.escape_string(item['company_name']),
                pymysql.escape_string(item['unicode']),
                pymysql.escape_string(item['org_code']),
                pymysql.escape_string(item['register_address']),
                pymysql.escape_string(item['corporation']),
                pymysql.escape_string(item['case_nature']),
                pymysql.escape_string(item['break_situation']),
                pymysql.escape_string(item['punish_situation']),
                pymysql.escape_string(item['issue_organ'])
            )
            self.cursor.execute(sqltext)
        else:
            spider.log('Undifined name: %s' % spider.name)

        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        # 连接数据库
        self.connect = pymysql.connect(
            host=self.settings.get('MYSQL_HOST'),
            port=self.settings.get('MYSQL_PORT'),
            db=self.settings.get('MYSQL_DBNAME'),
            user=self.settings.get('MYSQL_USER'),
            passwd=self.settings.get('MYSQL_PASSWD'),
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();
        self.connect.autocommit(True)

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
