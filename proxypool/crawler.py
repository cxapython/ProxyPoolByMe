from .utils import get_page
import ast


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_ip3366(self):
        """
        购买的试用云代理
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://ged.ip3366.net/api/?key=20190902165158891&getnum=30&anonymoustype=3&area=1&order=2&formats=2'
        source = get_page(start_url)
        if source:
            proxy_list = ast.literal_eval(source)
            print(proxy_list)
            for item in proxy_list:
                try:
                    yield ':'.join([item.get("Ip"), str(item.get("Port"))])
                except:
                    pass
