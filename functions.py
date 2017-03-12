# coding:utf-8
import requests,re,time,sys

# ============== 函数区 =======================
    # 加载插件
def load_plugin(plugin):
    plugin = __import__(plugin)
    plugin = getattr(plugin, 'SpiderPlugin')()
    return plugin

# 检测是否可用
def checkProxy(proxy,timeout=5):
    try:
        proxies = {"http": ""}
        proxies["http"] = proxy
        req = requests.get("http://1212.ip138.com/ic.asp", proxies=proxies, timeout=timeout).content
        result = re.findall(r'\[(\S+)\]', req)
        if len(result) != 0 and proxy.split(":")[0] in result:
            return True
    except:
        return False

# 主要执行爬虫
def SPIDER_PROXY(page,timeout,plugin,filename):
    proxies = load_plugin(plugin).spiderIP(page)
    ip = map(lambda x:"%s:%s"%x,proxies)

    if len(ip) == 0:
        print "Lost page!"
        exit(0)

    print 'Check the proxies:%s'%str(ip)
    for i in set(ip):
        if checkProxy(i,timeout=timeout):
            if filename:
                with open(filename,'a') as f:
                    f.write(i+'\n')
            else:
                print "[*] Proxy %s"%i


# 检测文件内的 代理ip是否可用
def CHECK_FILE_PROXY(filename,timeout=5,write=False,newfile=''):
    with open(filename,'r') as f:
        lines = f.readlines()

    for i in lines:
        proxy = i.replace('\n','')
        start = time.time()
        if checkProxy(proxy,timeout=timeout):
            end = time.time()
            print '[*] Proxy: %s   %.2fms'%(proxy,end-start)
            if write:
                with open(newfile,'a') as f:
                    f.write(proxy+'\n')