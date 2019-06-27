#-*- coding: UTF-8 -*-   
import requests


def spider(sn, book_list=[]):
    """ 爬取淘宝网的图数数据 """
    url = 'https://s.taobao.com/api?ajax=true&m=customized&sourceId=tb.index&q={0}'.format(sn)
    rest = requests.get(url).json()
    print(rest)
    bk_list = rest["API.CustomizedApi"]["itemlist"]["auctions"]
    print(len(bk_list))

    for bk in bk_list:
        # 标题
        title = bk['raw_title']
        price = bk['view_price']
        link = bk['detail_url']
        store = bk['nick']
        print('{title}: {price}: {link}: {store}'.format(
            title=title,
            price=price,
            link=link,
            store=store
        ))
        book_list.append({
            'title': title,
            'price': price,
            'link': link,
            'store': store
        })

if __name__ == '__main__':
    spider('9787115428028')