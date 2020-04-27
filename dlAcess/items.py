# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItemList(scrapy.Item):
    administra_counterpart_name = scrapy.Field()
    unicode = scrapy.Field()
    have_detail = scrapy.Field()


# 税务
class TaxItem(scrapy.Item):
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


# 行政许可
class AllowItem(scrapy.Item):
    # define the fields for your item here like:
    administra_counterpart_name = scrapy.Field()
    administra_counterpart_type = scrapy.Field()
    unicode = scrapy.Field()
    org_code = scrapy.Field()
    register_no = scrapy.Field()
    tax_register_no = scrapy.Field()
    administra_counterpart_code5 = scrapy.Field()
    administra_counterpart_code6 = scrapy.Field()
    legal_person = scrapy.Field()
    legal_person_cert_type = scrapy.Field()
    legal_person_cert = scrapy.Field()
    allow_doc_name = scrapy.Field()
    allow_doc_no = scrapy.Field()
    allow_type = scrapy.Field()
    allow_cert_name = scrapy.Field()
    allow_cert_no = scrapy.Field()
    allow_content = scrapy.Field()
    allow_decision_date = scrapy.Field()
    validate_from = scrapy.Field()
    validate_to = scrapy.Field()
    allow_authority = scrapy.Field()
    allow_authority_unicode = scrapy.Field()
    current_status = scrapy.Field()
    data_source_unit = scrapy.Field()
    data_source_unit_unicode = scrapy.Field()
    remarks = scrapy.Field()


# 行政处罚
class PunishItem(scrapy.Item):
    # define the fields for your item here like:
    administra_counterpart_type = scrapy.Field()
    administra_counterpart_name = scrapy.Field()
    unicode = scrapy.Field()
    register_no = scrapy.Field()
    tax_register_no = scrapy.Field()
    administra_counterpart_code5 = scrapy.Field()
    administra_counterpart_code6 = scrapy.Field()
    legal_person = scrapy.Field()
    legal_person_cert_type = scrapy.Field()
    legal_person_cert = scrapy.Field()
    punish_doc_no = scrapy.Field()
    illegal_type = scrapy.Field()
    illegal_facts = scrapy.Field()
    punish_basis = scrapy.Field()
    punish_type = scrapy.Field()
    punish_content = scrapy.Field()
    punish_amount = scrapy.Field()
    confiscate_amount = scrapy.Field()
    suspended_revoked_cert_no = scrapy.Field()
    punish_decision_date = scrapy.Field()
    validate = scrapy.Field()
    publicity_to = scrapy.Field()
    punish_authority = scrapy.Field()
    punish_authority_unicode = scrapy.Field()
    data_source_unit = scrapy.Field()
    data_source_unit_unicode = scrapy.Field()
    remarks = scrapy.Field()


# 重大税收违法案件
class TaxViolationItem(scrapy.Item):
    # define the fields for your item here like:
    administra_counterpart_type = scrapy.Field()
    administra_counterpart_name = scrapy.Field()
    unicode = scrapy.Field()
    tax_register_no = scrapy.Field()
    legal_person = scrapy.Field()
    legal_person_cert_type = scrapy.Field()
    legal_person_cert = scrapy.Field()
    register_address = scrapy.Field()
    finance_name = scrapy.Field()
    finance_cert_type = scrapy.Field()
    finance_cert = scrapy.Field()
    agency_name = scrapy.Field()
    agency_type = scrapy.Field()
    agency_code = scrapy.Field()
    tax_related_professionals_name = scrapy.Field()
    tax_related_professionals_name_cert_type = scrapy.Field()
    tax_related_professionals_name_cert = scrapy.Field()
    case_nature = scrapy.Field()
    illegal_facts = scrapy.Field()
    punish_basis = scrapy.Field()
    punish_type = scrapy.Field()
    check_unit = scrapy.Field()
    publish_date = scrapy.Field()
    validate_to = scrapy.Field()


# 失信被执行人
class BreakPromiseItem(scrapy.Item):
    # define the fields for your item here like:
    administra_counterpart_type = scrapy.Field()
    administra_counterpart_name = scrapy.Field()
    unicode = scrapy.Field()
    tax_register_no = scrapy.Field()
    legal_person = scrapy.Field()
    legal_person_cert_type = scrapy.Field()
    legal_person_cert = scrapy.Field()
    cert_type = scrapy.Field()
    case_no = scrapy.Field()
    filing_time = scrapy.Field()
    exec_doc_no = scrapy.Field()
    exec_court = scrapy.Field()
    exec_basis_unit = scrapy.Field()
    validae_legal_obligations = scrapy.Field()
    publish_date = scrapy.Field()
    publish_status = scrapy.Field()
    dishonesty_expiry_date = scrapy.Field()
    shield_time = scrapy.Field()
    cancel_time = scrapy.Field()
    executed_person_situation = scrapy.Field()
    executed_person_performance_situation = scrapy.Field()
    contractor_id = scrapy.Field()
    remarks = scrapy.Field()


# 经营异常名录
class AbnormalItem(scrapy.Item):
    # define the fields for your item here like:
    administra_counterpart_type = scrapy.Field()
    administra_counterpart_name = scrapy.Field()
    unicode = scrapy.Field()
    administra_counterpart_code3 = scrapy.Field()
    administra_counterpart_code2 = scrapy.Field()
    administra_counterpart_code4 = scrapy.Field()
    institution_cert_no = scrapy.Field()
    social_organ_register_cert_no = scrapy.Field()
    legal_person = scrapy.Field()
    legal_person_cert_type = scrapy.Field()
    legal_person_cert = scrapy.Field()
    list_decision_doc_no = scrapy.Field()
    list_reason = scrapy.Field()
    list_date = scrapy.Field()
    remove_decision_doc_no = scrapy.Field()
    remove_reason = scrapy.Field()
    remove_date = scrapy.Field()
    list_authority = scrapy.Field()
    remove_authority = scrapy.Field()
    source = scrapy.Field()