# coding:utf-8
import requests,re

class SpiderPlugin:
    '''
    66ip 代理爬行插件

    插件格式
    class SpiderPlugin:

        def spiderIP(self,page):
            ...code....

            return [(ip,port),(ip,port),(ip,port),.......]
    '''

    def spiderIP(self,page=1):
        url = "http://www.66ip.cn/areaindex_%s/1.html"%page
        req = requests.get(url)
        return re.findall(r'<td>(\d{2,3}\.\S+)</td><td>(\d{2,5})</td>',req.content)