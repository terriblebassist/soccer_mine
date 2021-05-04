import scrapy
from soccer_mine.items import Player
from soccer_mine import xpaths, factory


class QuotesSpider(scrapy.Spider):
    name = "fifa"
    players_url = 'https://www.fifaindex.com/players/'
    player_url = "https://www.fifaindex.com/players/?page="

    def start_requests(self):
        yield scrapy.Request(url=self.players_url, callback=self.init_call)

    def init_call(self, response):
        # pagelimit = response.xpath(
        #     '//*[@id="bigpagination"]/nav[1]/ul/li[12]/a/@href').extract_first().split('=')[1]
        pagelimit = 2
        urls = [f"{self.player_url}{pageno}" for pageno in list(
            map(str, range(1, int(pagelimit)+1)))]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_pages)

    def parse_pages(self, response):
        tablelist = response.xpath(xpaths.xplayer_table)
        for row in tablelist:
            if row.xpath(xpaths.xplayer).extract_first() is not None:
                player_page = response.urljoin(
                    row.xpath(xpaths.xplayer).extract_first())
                yield scrapy.Request(url=player_page, callback=self.parse_players)

    def parse_players(self, response):
        yield Player(
            name=factory.get_player_name(response),
            rating=factory.get_player_rating(response),
            profile=factory.get_player_profile(response),
            teams=factory.get_player_teams(response),
            skills=factory.get_player_skills(response),
            link=response.url
        )
