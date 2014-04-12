from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.http import FormRequest
from scraper.items import faculty_contact
from scraper.validation_keys import view_state, event_validation
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst


class faculty_spider(Spider):
    name = "faculty"
    allowed_domains = ["dir.aucegypt.edu"]
    start_urls = ["http://dir.aucegypt.edu/index.aspx"]
    deals_list_xpath = '//td'
    item_fields = {'name': './/b/span[contains(@id, "NameLabel")]/text()',
                   'department': './/span[contains(@id, "DeptLabel")]/text()',
                   'title': './/span[contains(@id, "TitleLabel")]/text()',
                   'email': './/a[contains(@id, "mailA")]/img/@src',
                   'phone': './/span[contains(@id, "PhoneLabel")]/text()',
                   'building': './/span[contains(@id, "BLDGLabel")]/text()',
                   'room': './/span[contains(@id, "RMLabel")]/text()',
                   'campus': './/span[contains(@id, "CampusLabel")]/text()'}

    def parse(self, response):
        return FormRequest.from_response(
            response, formname='aspnetForm',
            formdata={'__LASTFOCUS': '', '__VIEWSTATE': view_state,
                      '__EVENTTARGET': '', 'EVENTARGUMENT': '',
                      '__EVENTVALIDATION': event_validation,
                      'ctl00$ContentPlaceHolder1$firstname': '',
                      'ctl00$ContentPlaceHolder1$firstnametype':
                      'firstcontains',
                      'ctl00$ContentPlaceHolder1$lastname': '',
                      'ctl00$ContentPlaceHolder1$lastnametype':
                      'lastcontains',
                      'ctl00$ContentPlaceHolder1$title': '',
                      'ctl00$ContentPlaceHolder1$email': '',
                      'ctl00$ContentPlaceHolder1$department':
                      'Printshop',
                      'ctl00$ContentPlaceHolder1$Button1':
                      'Search'}, callback=self.parse2
        )

    def parse2(self, response):
        selector = Selector(response)
        for deal in selector.xpath(self.deals_list_xpath):

            for field, xpath in self.item_fields.iteritems():
                loader = ItemLoader(
                    faculty_contact(),
                    response=response
                )
                loader.add_xpath(field, xpath)
            yield loader.load_item()
