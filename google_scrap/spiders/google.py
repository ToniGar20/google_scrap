import scrapy
import urllib.parse


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['google.com']
    query = input("Introduce consulta a hacer: ")

    # parsing query to check
    queryParsed = urllib.parse.quote_plus(query)

    # mounting url to parse
    start_urls = ['https://www.google.com/search?q=' + queryParsed + '&hl=es']

    # cookie for consent mode
    consent_cookie = {'CONSENT': 'YES+'}

    def start_requests(self):
        yield scrapy.Request(
            url=self.start_urls[0],
            cookies=self.consent_cookie,
            callback=self.parse
        )

    def parse(self, response):
        organicSerp = response.xpath('//div[@id="search"]/div/div/div').get()
        organicRegularSlots = response.xpath('//div[@data-sokoban-container]').get()
        keyword = response.xpath('//input[@name="q"]/@value').get()
        position = 1
        print(organicSerp)
        print(organicRegularSlots)
        print(keyword)

        # for slot in organicRegularSlots:
        #     url = slot.xpath('./div[@data-header-feature]/div/a/@href').get()
        #     title = slot.xpath('./div[@data-header-feature]/div/a/h3/text()').get()
        #     metadescription = slot.xpath('.//div[@data-content-feature]/div//text()').get()
        #     yield {
        #         'keyword': keyword,
        #         'position': position,
        #         'url': url,
        #         'title': title,
        #         'metadescription': metadescription
        #     }
        #     position += 1

        print('Crawl ended!')
