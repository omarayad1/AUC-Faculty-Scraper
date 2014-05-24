from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.http import FormRequest
from scraper.items import faculty_contact
from scraper.validation_keys import view_state, event_validation
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst
from scraper.departments import departments
import httplib
import urllib
import HTMLParser

class faculty_spider(Spider):
    name = "faculty"
    allowed_domains = ["dir.aucegypt.edu"]
    start_urls = ["http://dir.aucegypt.edu/index.aspx"]
    deals_list_xpath = '//td'
    item_fields = {'name': './/b/span[contains(@id, "NameLabel")]/text()',
                   'department': './/span[contains(@id, "DeptLabel")]/text()',
                   'title': './/span[contains(@id, "TitleLabel")]/text()',
                   'email': './/a[contains(@id, "mailA")]/@href',
                   'phone': './/span[contains(@id, "PhoneLabel")]/text()',
                   'building': './/span[contains(@id, "BLDGLabel")]/text()',
                   'room': './/span[contains(@id, "RMLabel")]/text()',
                   'campus': './/span[contains(@id, "CampusLabel")]/text()'}

    def parse(self, response):
        for department in departments:
            department_value_escaped = HTMLParser.HTMLParser().unescape(department)
            yield FormRequest(
                url=self.start_urls[0],
                method='POST',
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
                          department_value_escaped,
                          'ctl00$ContentPlaceHolder1$Button1':
                          'Search'}, callback=self.parse2, dont_filter=True
            )

    def parse2(self, response):
        hxs = Selector(response)
        items = hxs.xpath(self.deals_list_xpath)
        for item in items:
            loader = ItemLoader(faculty_contact(), selector=item)
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()
            for field, xpath in self.item_fields.iteritems():
                if field == 'email':
                    link = item.xpath(self.item_fields['email'])
                    r = httplib.HTTPConnection('dir.aucegypt.edu')
                    try:
                        r.request('GET', '/'+link.extract()[0])
                        res = r.getresponse()
                        data = res.read()
                        email_selection = Selector(text=data)
                        email = email_selection.xpath('//@href')
                        loader.add_value('email', unicode(urllib.unquote(email.extract()[0]).replace('mailto:', '')))
                    except IndexError:
                        loader.add_value('email', u'')
                else:
                    loader.add_xpath(field, xpath)
            yield loader.load_item()
