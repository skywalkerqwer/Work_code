import csv
import os

from fake_useragent import UserAgent
import requests
from lxml import etree
from threading import Thread, Lock


class Yx_spider(object):
    def __init__(self):
        self.rq_url = 'https://www.3839.com/top/hot.html'
        self.bs_url = 'https://www.3839.com/top/sugar.html'
        self.header = {
            'User-Agent': UserAgent().ie
        }
        # self.rq_url_list = []
        # self.bs_url_list = []
        self.t_list = []
        self.rq_lock = Lock()
        self.bs_lock = Lock()

    def get_html(self, url):
        html = requests.get(url, headers=self.header)
        return html

    def get_html_url(self, url):
        html = requests.get(url, headers=self.header).text
        parse_html = etree.HTML(html)
        list_ = parse_html.xpath("//ul[@class='ranking-game ranking-list']/li/div/em/a/@href")

        return list_

    def join_detailed(self):
        rq_list = self.get_html_url(self.rq_url)
        bs_list = self.get_html_url(self.bs_url)
        for rq in rq_list:
            t = Thread(target=self.get_data, args=(rq, "人气",))
            t.start()
            self.t_list.append(t)
        for bs in bs_list:
            t = Thread(target=self.get_data, args=(bs, "飙升",))
            t.start()
            self.t_list.append(t)

    def get_data(self, url, lx):
        url = "https:" + url
        html = self.get_html(url)
        parse = html.content.decode('utf-8', 'ignore')
        parse_html = etree.HTML(parse)
        # id
        game_id = html.url.split("/")[-1].split('.')[0]
        # 游戏名称
        game_name = parse_html.xpath("//h1[@class='name']/text()")[0]
        # 游戏评分
        game_score = parse_html.xpath("//div[@class='card']/p/text()")[0]
        # 游戏简介
        game_brief = parse_html.xpath("//div[@id='zinfoc4']/text()")
        # 游戏图标链接
        game_icon = parse_html.xpath("//div[@class='gameDesc']/img/@src")  # 记着加https：
        # 游戏评论数
        game_comment = parse_html.xpath("//div[@class='tabArea']/a[2]/span/text()")
        # 玩游戏人数
        game_people = parse_html.xpath("//div[@class='btn']/p/span/text()")
        # 游戏大小
        game_size = parse_html.xpath("//div[@class='gameTable']/table/tbody/tr[1]/td[2]/text()")
        # 游戏版本
        game_version = parse_html.xpath("//div[@class='gameTable']//tr[1]/td[2]/text()")
        # 系统要求
        game_sys = parse_html.xpath("//div[@class='gameTable']//tr[1]/td[3]/text()")
        # 游戏更新时间
        game_time = parse_html.xpath("//div[@class='gameTable']//tr[2]/td[1]/text()")
        # 语言
        game_Language = parse_html.xpath("//div[@class='gameTable']//tr[2]/td[2]/text()")
        game_green = parse_html.xpath("//div[@class='txt']/p/a/text()")
        if lx == "飙升":
            if not os.path.exists("./info"):
                os.mkdir('info')
            self.bs_lock.acquire()
            with open('./info/飙升.csv', "a+", encoding='utf-8') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(["游戏id：" + game_id])
                csv_writer.writerow(["游戏名称：" + game_name])
                csv_writer.writerow(["游戏评分：" + game_score])
                csv_writer.writerow(["游戏简介：" + "".join(game_brief)])
                csv_writer.writerow(["游戏图标链接：" + "https:" + "".join(game_icon)])
                csv_writer.writerow(["游戏评论数：" + "".join(game_comment)])
                csv_writer.writerow(["游戏人数：" + "".join(game_people)])
                csv_writer.writerow(["".join(game_size)])
                csv_writer.writerow(["".join(game_version)])
                csv_writer.writerow(["".join(game_sys)])
                csv_writer.writerow(["".join(game_time)])
                csv_writer.writerow(["".join(game_Language)])
                csv_writer.writerow(["厂商：" + "".join(game_green)])
            self.bs_lock.release()

        else:
            if not os.path.exists("./info"):
                os.mkdir('info')
            self.rq_lock.acquire()
            with open('./info/人气.csv', "a+", encoding='utf-8') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(["游戏id：" + game_id])
                csv_writer.writerow(["游戏名称：" + game_name])
                csv_writer.writerow(["游戏评分：" + game_score])
                csv_writer.writerow(["游戏简介：" + "".join(game_brief)])
                csv_writer.writerow(["游戏图标链接：" + "https:" + "".join(game_icon)])
                csv_writer.writerow(["游戏评论数：" + "".join(game_comment)])
                csv_writer.writerow(["游戏人数：" + "".join(game_people)])
                csv_writer.writerow(["".join(game_size)])
                csv_writer.writerow(["".join(game_version)])
                csv_writer.writerow(["".join(game_sys)])
                csv_writer.writerow(["".join(game_time)])
                csv_writer.writerow(["".join(game_Language)])
                csv_writer.writerow(["厂商：" + "".join(game_green)])
                csv_writer.writerow(["\n"])
                csv_writer.writerow(["\n"])
            self.rq_lock.release()

    def run(self):
        self.join_detailed()
        for i in self.t_list:
            i.join()


if __name__ == '__main__':
    game_spider = Yx_spider()
    game_spider.run()
