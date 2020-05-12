#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wping
# create_time: 2020-04-20
import json

import scrapy
from scrapy.http import HtmlResponse

from dlAcess.items import ItemList, TaxViolationItem


class TaxVolationSpider(scrapy.Spider):
    name = 'tax_violation'

    start_urls = ["https://credit.dl.cn/credit-portal/dl/publicity/record/tax_violation"]

    list_url = "https://credit.dl.cn/credit-portal/dl/api/publicity/record/ZDSSWFAJDSR/0"

    information_url = "https://credit.dl.cn/credit-portal/dl/api/integrated/main/information"

    nav_detail_url = "https://credit.dl.cn/credit-portal/dl/api/integrated/internetList/catalog/objectCode"

    totalNum = 0
    linesPerPage = 1000

    condition = {'keyWord': ''}

    page_num = 0

    zzbh = ""

    def parse(self, response):
        item_list = ItemList()
        # follow pagination links
        self.page_num = self.page_num + 1
        print("开始抽取第{}页".format(self.page_num))
        payload = {
            'listSql': '',
            'linesPerPage': self.linesPerPage,
            'currentPage': self.page_num,
            'condition': self.condition
        }

        if self.page_num == 1:
            yield response.follow(self.list_url, callback=self.parse,
                                  method='POST',
                                  headers={'Content-Type': 'application/json'},
                                  body=json.dumps(payload))

        else:

            json_response = json.loads(response.body_as_unicode())
            # print(json_response)
            # follow links to detail pages

            try:
                resources = json_response['data']['list']

                for resource in resources:
                    item_list['administra_counterpart_name'] = resource['zzmc']
                    item_list['unicode'] = resource['tyshxydm']
                    self.zzbh = str(resource['zzbh'])

                    if self.zzbh is not None:
                        item_list['have_detail'] = '是'
                        yield item_list
                        form_data = {'zzbh': self.zzbh}

                        # 查询详情信息的入口请求
                        yield scrapy.FormRequest(self.information_url, callback=self.parse_detail,
                                                 method='POST',
                                                 headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                                 formdata=form_data)

                    else:
                        item_list['have_detail'] = '否'
                        yield item_list
                        # print("相对执行人：{}统一社会信用代码：{}, zzbh: {}, 无法获取详情信息"
                        #       .format(resource['zzmc'], resource['tyshxydm'], resource['zzbh']))
                # time.sleep(1)
                self.totalNum = json_response['data']['page']['totalNum']
                self.linesPerPage = json_response['data']['page']['linesPerPage']
            except TypeError:
                print("无法解析，接口：{}, 响应：{}".format(response.url, json_response))

            if self.page_num <= (self.totalNum / self.linesPerPage) + 1:
                yield response.follow(self.list_url, callback=self.parse,
                                      method='POST',
                                      headers={'Content-Type': 'application/json'},
                                      body=json.dumps(payload))

    def parse_detail(self, response):
        json_response = json.loads(response.body_as_unicode())
        # print(json_response)
        if json_response['data'] is None or json_response['data']['navigationBar'] is None:
            print("接口服务调用异常,url:{}".format(response.url))
            return

        html_response = HtmlResponse(url="detail HTML string",
                                     body=json_response['data']['navigationBar'],
                                     encoding='utf-8')

        categoryfacetsecond = html_response.css('div.sub-title-nav ul li:last-child a::attr(categoryfacetsecond)').get()

        catalogids = html_response.css('div.sub-title-nav ul li:last-child a::attr(catalogids)').get().split(',')

        classificationid = html_response.css('div.sub-title-nav ul li:last-child a::attr(classificationid)').get()

        detail_payload = {
            'categoryFacetSecond': categoryfacetsecond,
            'catalogIds': catalogids,
            'classificationId': classificationid,
            'zzbh': self.zzbh
        }

        print(detail_payload)

        yield response.follow(self.nav_detail_url, callback=self.parse_nav_detail,
                              method='POST',
                              headers={'Content-Type': 'application/json'},
                              body=json.dumps(detail_payload))

    # 解析子导航栏
    def parse_nav_detail(self, response):
        item = TaxViolationItem()
        json_response = json.loads(response.body_as_unicode())
        # print("parse_detail:{}".format(json_response))
        event_detail = []
        if json_response['data'] is None:
            print("接口服务调用异常,url:{}".format(response.url))
            return
        try:
            html_response = HtmlResponse(url="detail HTML string",
                                         body=json_response['data'][0],
                                         encoding='utf-8')
        except IndexError:
            print("page_num:{}, zzbh:{} 无详情数据".format(self.page_num, self.zzbh))
            return

        events = html_response.css('span.wc-value::text').getall()
        # print("events的长度:{}".format(len(events)))
        for event in events:
            event_detail.append(event)
            if len(event_detail) % 24 == 0:
                item['administra_counterpart_type'] = event_detail[0]
                item['administra_counterpart_name'] = event_detail[1]
                item['unicode'] = event_detail[2]
                item['tax_register_no'] = event_detail[3]
                item['legal_person'] = event_detail[4]
                item['legal_person_cert_type'] = event_detail[5]
                item['legal_person_cert'] = event_detail[6]
                item['register_address'] = event_detail[7]
                item['finance_name'] = event_detail[8]
                item['finance_cert_type'] = event_detail[9]
                item['finance_cert'] = event_detail[10]
                item['agency_name'] = event_detail[11]
                item['agency_type'] = event_detail[12]
                item['agency_code'] = event_detail[13]
                item['tax_related_professionals_name'] = event_detail[14]
                item['tax_related_professionals_name_cert_type'] = event_detail[15]
                item['tax_related_professionals_name_cert'] = event_detail[16]
                item['case_nature'] = event_detail[17]
                item['illegal_facts'] = event_detail[18]
                item['punish_basis'] = event_detail[19]
                item['punish_type'] = event_detail[20]
                item['check_unit'] = event_detail[21]
                item['publish_date'] = event_detail[22]
                item['validate_to'] = event_detail[23]

                yield item
                event_detail.clear()


