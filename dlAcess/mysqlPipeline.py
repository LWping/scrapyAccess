#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wping
# create_time:
import pymysql

from dlAcess.items import AllowItem, ItemList, TaxViolationItem, AbnormalItem, PunishItem, BreakPromiseItem


class DlacessMysqlPipeline(object):

    # 通用模版列表Insert语句
    listInsert = "insert into {} (administra_counterpart_name, unicode, have_detail) values ('{}', '{}', '{}')"

    # 行政许可
    allowInsert = '''
    insert into allow_publicity(administra_counterpart_name, administra_counterpart_type, unicode, org_code,
    register_no, tax_register_no, administra_counterpart_code5, administra_counterpart_code6, legal_person, 
    legal_person_cert_type, legal_person_cert, allow_doc_name, allow_doc_no, allow_type, allow_cert_name,
    allow_cert_no, allow_content, allow_decision_date, validate_from, validate_to, allow_authority, 
    allow_authority_unicode, current_status, data_source_unit, data_source_unit_unicode, remarks)
    values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
     '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
    '''

    # 行政处罚
    punishInsert = '''
    insert into punish_publicity(administra_counterpart_type, administra_counterpart_name, unicode, org_code,
    register_no, tax_register_no, administra_counterpart_code5, administra_counterpart_code6, legal_person, 
    legal_person_cert_type, legal_person_cert, punish_doc_no, allow_doc_no, illegal_type, illegal_facts,
    punish_basis, punish_type, punish_content, punish_amount, confiscate_amount, suspended_revoked_cert_no, 
    punish_decision_date, validate, publicity_to, punish_authority, punish_authority_unicode, data_source_unit,
    data_source_unit_unicode, remarks)
    values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
     '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
    '''

    # 重大税收违法案件
    taxViolationInsert = '''
    insert into tax_violation(administra_counterpart_type, administra_counterpart_name, unicode, tax_register_no,
    legal_person, legal_person_cert_type, legal_person_cert, register_address, finance_name, finance_cert_type,
    finance_cert, agency_name, agency_type, agency_code, tax_related_professionals_name, 
    tax_related_professionals_name_cert_type, tax_related_professionals_name_cert, case_nature, illegal_facts, 
    punish_basis, punish_type, check_unit, publish_date, validate_to)
    values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
     '{}', '{}', '{}', '{}', '{}', '{}')
    '''

    # 失信被执行人
    breakPromiseInsert = '''
    insert into break_promise(administra_counterpart_type, administra_counterpart_name, unicode, tax_register_no,
    exec_doc_no, exec_court, exec_basis_unit, validae_legal_obligations, publish_date, publish_status,
    dishonesty_expiry_date, shield_time, cancel_time, executed_person_situation, executed_person_performance_situation, 
    contractor_id, remarks)
    values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
     '{}', '{}', '{}', '{}', '{}')
    '''

    # 经营异常名录
    abnormalInsert = '''
    insert into abnormal(administra_counterpart_type, administra_counterpart_name, unicode, 
    administra_counterpart_code3, administra_counterpart_code2, administra_counterpart_code4, institution_cert_no,
    social_organ_register_cert_no, legal_person, legal_person_cert_type, legal_person_cert, list_decision_doc_no,
    list_reason, list_date, remove_decision_doc_no, remove_reason, remove_date, list_authority, remove_authority,source)
    values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
     '{}', '{}')
    '''

    def __init__(self, settings):
        self.settings = settings

    def process_item(self, item, spider):
        # 行政许可
        if spider.name == "allow":
            if isinstance(item, ItemList):
                sqltext = self.listInsert.format(
                    "allow_publicity_list",
                    pymysql.escape_string(item['administra_counterpart_name']),
                    pymysql.escape_string(item['unicode']),
                    pymysql.escape_string(item['have_detail'])
                )
                self.cursor.execute(sqltext)
            elif isinstance(item, AllowItem):
                sqltext = self.allowInsert.format(
                    pymysql.escape_string(item['administra_counterpart_name']),
                    pymysql.escape_string(item['administra_counterpart_type']),
                    pymysql.escape_string(item['unicode']),
                    pymysql.escape_string(item['org_code']),
                    pymysql.escape_string(item['register_no']),
                    pymysql.escape_string(item['tax_register_no']),
                    pymysql.escape_string(item['administra_counterpart_code5']),
                    pymysql.escape_string(item['administra_counterpart_code6']),
                    pymysql.escape_string(item['legal_person']),
                    pymysql.escape_string(item['legal_person_cert_type']),
                    pymysql.escape_string(item['legal_person_cert']),
                    pymysql.escape_string(item['allow_doc_name']),
                    pymysql.escape_string(item['allow_doc_no']),
                    pymysql.escape_string(item['allow_type']),
                    pymysql.escape_string(item['allow_cert_name']),
                    pymysql.escape_string(item['allow_cert_no']),
                    pymysql.escape_string(item['allow_content']),
                    pymysql.escape_string(item['allow_decision_date']),
                    pymysql.escape_string(item['validate_from']),
                    pymysql.escape_string(item['validate_to']),
                    pymysql.escape_string(item['allow_authority']),
                    pymysql.escape_string(item['allow_authority_unicode']),
                    pymysql.escape_string(item['current_status']),
                    pymysql.escape_string(item['data_source_unit']),
                    pymysql.escape_string(item['data_source_unit_unicode']),
                    pymysql.escape_string(item['remarks'])
                )
                self.cursor.execute(sqltext)
            else:
                print("mysqlPipeline item类型错误：{}".format(type(item)))
            self.cursor.execute(sqltext)
        # 行政处罚
        elif spider.name == 'punish':
            if isinstance(item, ItemList):
                sqltext = self.listInsert.format(
                    "punish_publicity_list",
                    pymysql.escape_string(item['administra_counterpart_name']),
                    pymysql.escape_string(item['unicode']),
                    pymysql.escape_string(item['have_detail'])
                )
                self.cursor.execute(sqltext)
            elif isinstance(item, PunishItem):
                sqltext = self.punishInsert.format(
                    pymysql.escape_string(item['administra_counterpart_type']),
                    pymysql.escape_string(item['administra_counterpart_name']),
                    pymysql.escape_string(item['unicode']),
                    pymysql.escape_string(item['org_code']),
                    pymysql.escape_string(item['register_no']),
                    pymysql.escape_string(item['tax_register_no']),
                    pymysql.escape_string(item['administra_counterpart_code5']),
                    pymysql.escape_string(item['administra_counterpart_code6']),
                    pymysql.escape_string(item['legal_person']),
                    pymysql.escape_string(item['legal_person_cert_type']),
                    pymysql.escape_string(item['legal_person_cert']),
                    pymysql.escape_string(item['punish_doc_no']),
                    pymysql.escape_string(item['illegal_type']),
                    pymysql.escape_string(item['illegal_facts']),
                    pymysql.escape_string(item['punish_basis']),
                    pymysql.escape_string(item['punish_type']),
                    pymysql.escape_string(item['punish_content']),
                    pymysql.escape_string(item['punish_amount']),
                    pymysql.escape_string(item['confiscate_amount']),
                    pymysql.escape_string(item['suspended_revoked_cert_no']),
                    pymysql.escape_string(item['punish_decision_date']),
                    pymysql.escape_string(item['validate']),
                    pymysql.escape_string(item['publicity_to']),
                    pymysql.escape_string(item['punish_authority']),
                    pymysql.escape_string(item['punish_authority_unicode']),
                    pymysql.escape_string(item['data_source_unit']),
                    pymysql.escape_string(item['data_source_unit_unicode']),
                    pymysql.escape_string(item['remarks'])
                )
                self.cursor.execute(sqltext)
            else:
                print("mysqlPipeline item类型错误：{}".format(type(item)))

        # 重大税收违法案件
        elif spider.name == 'tax_violation':
            if isinstance(item, ItemList):
                sqltext = self.listInsert.format(
                    "tax_violation_list",
                    pymysql.escape_string(item['administra_counterpart_name']),
                    pymysql.escape_string(item['unicode']),
                     pymysql.escape_string(item['have_detail'])
                )
                self.cursor.execute(sqltext)
            elif isinstance(item, TaxViolationItem):
                sqltext = self.taxViolationInsert.format(
                    pymysql.escape_string(item['administra_counterpart_type']),
                    pymysql.escape_string(item['administra_counterpart_name']),
                    pymysql.escape_string(item['unicode']),
                    pymysql.escape_string(item['legal_person']),
                    pymysql.escape_string(item['legal_person_cert_type']),
                    pymysql.escape_string(item['legal_person_cert']),
                    pymysql.escape_string(item['register_address']),
                    pymysql.escape_string(item['finance_name']),
                    pymysql.escape_string(item['finance_cert_type']),
                    pymysql.escape_string(item['finance_cert']),
                    pymysql.escape_string(item['agency_name']),
                    pymysql.escape_string(item['agency_type']),
                    pymysql.escape_string(item['agency_code']),
                    pymysql.escape_string(item['tax_related_professionals_name']),
                    pymysql.escape_string(item['tax_related_professionals_name_cert_type']),
                    pymysql.escape_string(item['tax_related_professionals_name_cert']),
                    pymysql.escape_string(item['allow_authority_unicode']),
                    pymysql.escape_string(item['case_nature']),
                    pymysql.escape_string(item['illegal_facts']),
                    pymysql.escape_string(item['punish_basis']),
                    pymysql.escape_string(item['punish_type']),
                    pymysql.escape_string(item['check_unit']),
                    pymysql.escape_string(item['publish_date']),
                    pymysql.escape_string(item['validate_to']),
                )
                self.cursor.execute(sqltext)
            else:
                print("mysqlPipeline item类型错误：{}".format(type(item)))

        # 失信被执行人
        elif spider.name == 'break_promise':
            if isinstance(item, ItemList):
                sqltext = self.listInsert.format(
                    "break_promise_list",
                    pymysql.escape_string(item['administra_counterpart_name']),
                    pymysql.escape_string(item['unicode']),
                    pymysql.escape_string(item['have_detail'])
                )
                self.cursor.execute(sqltext)
            elif isinstance(item, BreakPromiseItem):
                sqltext = self.breakPromiseInsert.format(
                    pymysql.escape_string(item['administra_counterpart_type']),
                    pymysql.escape_string(item['administra_counterpart_name']),
                    pymysql.escape_string(item['unicode']),
                    pymysql.escape_string(item['tax_register_no']),
                    pymysql.escape_string(item['legal_person']),
                    pymysql.escape_string(item['legal_person_cert_type']),
                    pymysql.escape_string(item['legal_person_cert']),
                    pymysql.escape_string(item['cert_type']),
                    pymysql.escape_string(item['case_no']),
                    pymysql.escape_string(item['filing_time']),
                    pymysql.escape_string(item['exec_doc_no']),
                    pymysql.escape_string(item['exec_court']),
                    pymysql.escape_string(item['exec_basis_unit']),
                    pymysql.escape_string(item['validae_legal_obligations']),
                    pymysql.escape_string(item['publish_date']),
                    pymysql.escape_string(item['publish_status']),
                    pymysql.escape_string(item['dishonesty_expiry_date']),
                    pymysql.escape_string(item['shield_time']),
                    pymysql.escape_string(item['cancel_time']),
                    pymysql.escape_string(item['executed_person_situation']),
                    pymysql.escape_string(item['executed_person_performance_situation']),
                    pymysql.escape_string(item['contractor_id']),
                    pymysql.escape_string(item['remarks'])
                )
                self.cursor.execute(sqltext)
            else:
                print("mysqlPipeline item类型错误：{}".format(type(item)))
        # 经营异常名录
        elif spider.name == 'abnormal':
            if isinstance(item, ItemList):
                sqltext = self.listInsert.format(
                    "abnormal_list",
                    pymysql.escape_string(item['administra_counterpart_name']),
                    pymysql.escape_string(item['unicode']),
                    pymysql.escape_string(item['have_detail'])
                )
                self.cursor.execute(sqltext)
            elif isinstance(item, AbnormalItem):
                print("进入abnormal pipeline: AbnormalItem")
                sqltext = self.abnormalInsert.format(
                    pymysql.escape_string(item['administra_counterpart_type']),
                    pymysql.escape_string(item['administra_counterpart_name']),
                    pymysql.escape_string(item['unicode']),
                    pymysql.escape_string(item['administra_counterpart_code3']),
                    pymysql.escape_string(item['administra_counterpart_code2']),
                    pymysql.escape_string(item['administra_counterpart_code4']),
                    pymysql.escape_string(item['institution_cert_no']),
                    pymysql.escape_string(item['social_organ_register_cert_no']),
                    pymysql.escape_string(item['legal_person']),
                    pymysql.escape_string(item['legal_person_cert_type']),
                    pymysql.escape_string(item['legal_person_cert']),
                    pymysql.escape_string(item['list_decision_doc_no']),
                    pymysql.escape_string(item['list_reason']),
                    pymysql.escape_string(item['list_date']),
                    pymysql.escape_string(item['remove_decision_doc_no']),
                    pymysql.escape_string(item['remove_reason']),
                    pymysql.escape_string(item['remove_date']),
                    pymysql.escape_string(item['list_authority']),
                    pymysql.escape_string(item['remove_authority']),
                    pymysql.escape_string(item['source'])
                )
                self.cursor.execute(sqltext)
            else:
                print("mysqlPipeline item类型错误：{}".format(type(item)))
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
