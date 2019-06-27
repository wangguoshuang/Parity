#-*- coding: UTF-8 -*-   
import requests
from lxml import html


def spider(sn, book_list=[]):
    """ 爬取京东的图书数据 """
    url = 'https://search.jd.com/Search?keyword={0}'.format(sn)
    # 获取HTML文档

    resp = requests.get(url)
    print(resp.encoding)
    resp.encoding = 'utf-8'

    html_doc = resp.text

    # 获取xpath对象
    selector = html.fromstring(html_doc)

    # 找到列表的集合
    ul_list = selector.xpath('//div[@id="J_goodsList"]/ul/li')
    print(len(ul_list))

    # 解析对应的内容，标题，价格，链接
    for li in ul_list:
        # 标题
        title = li.xpath('div/div[@class="p-name"]/a/@title')
        print(title[0])
        # 购买链接
        link = li.xpath('div/div[@class="p-name"]/a/@href')
        print(link[0])

        # 价格
        price = li.xpath('div/div[@class="p-price"]/strong/i/text()')
        print(price[0])

        # 店铺
        store = li.xpath('div//a[@class="curr-shop"]/@title')
        print(store[0])

        book_list.append({
            'title': title[0],
            'price': price[0],
            'link': link[0],
            'store': store[0]
        })


if __name__ == '__main__':
    spider('9787115428028')