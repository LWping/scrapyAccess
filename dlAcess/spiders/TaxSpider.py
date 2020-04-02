# author: wping
# create_time: 2020-04-01

import scrapy


class TaxSpider(scrapy.Spider):
    name = 'tax'

    start_urls = ["http://dalian.chinatax.gov.cn/module/search/index.jsp?field=field_9745:12:1,field_9746:12:1,"
                  "field_9748:12:1&i_columnid=3038&field_9745=%E8%AF%B7%E9%80%89%E6%8B%A9&field_9746="
                  "%E8%AF%B7%E9%80%89%E6%8B%A9&field_9748=%E8%AF%B7%E9%80%89%E6%8B%A9&currpage=1"]

    start_url = "http://dalian.chinatax.gov.cn/module/search/index.jsp?field=field_9745:12:1,field_9746:12:1," \
                "field_9748:12:1&i_columnid=3038&field_9745=%E8%AF%B7%E9%80%89%E6%8B%A9&field_9746=" \
                "%E8%AF%B7%E9%80%89%E6%8B%A9&field_9748=%E8%AF%B7%E9%80%89%E6%8B%A9&currpage="
    page_num = 1;

    def parse(self, response):
        # follow links to detail pages
        links = response.css('tr td a::attr(href)').getall()
        for href in links:
            yield response.follow(href, self.parse_detail)
        # follow pagination links
        self.page_num = self.page_num + 1
        next_page = self.start_url + str(self.page_num)
        if len(links) < 15:
            self.log('end scrapy, total page num is: %s' % str(self.page_num - 1), level=20)  # 20代表输出INFO级别的日志
            return
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    @staticmethod
    def parse_detail(response):

        item_list = ['所属地区','所属年度', '所属季度', '纳税人名称', '纳税人识别号', '组织机构代码', '注册地址',
                     '法定代表人性别、性别及身份证号码', '案件性质', '主要违法事实', '相关法律依据及税务处理处罚情况', '公布机关']
        last_item = False
        event_detail = []

        for event in response.css('div.content tr td::text').getall():
            if event not in item_list:
                event_detail.append(event)
                last_item = False
            else:
                if last_item:
                    event_detail.append('')
                last_item = True

        yield {
            'area': event_detail[0],
            'year': event_detail[1],
            'quarter': event_detail[2],
            'company_name': event_detail[3],
            'unicode': event_detail[4],
            'org_code': event_detail[5],
            'register_address': event_detail[6],
            'corporation': event_detail[7],
            'case_nature': event_detail[8],
            'break_situation': event_detail[9],
            'punish_situation': event_detail[10],
            'issue_organ': event_detail[11]
        }
