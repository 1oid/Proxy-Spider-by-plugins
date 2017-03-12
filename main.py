# coding:utf-8
from functions import *
import threading
import Queue

class proxySpiderThreading(threading.Thread):
    def __init__(self,queue,plugin="66ip",timeout=10,filename=None):
        threading.Thread.__init__(self)
        self.queue = queue
        self.plugin = plugin
        self.filename = filename
        self.timeout = timeout

    def run(self):
        if not self.queue.empty():
            print 'Start Spidering...'
            SPIDER_PROXY(page=self.queue.get_nowait(),timeout=self.timeout,plugin=self.plugin,filename=self.filename)
        else:
            exit(0)

queue = Queue.Queue(0)
# 页数加入队列
map(lambda x:queue.put_nowait(x),range(1,35))
sys.path.append("./plugin/")
threads = []
for i in range(34):
    threads.append(proxySpiderThreading(queue,plugin="66ip"))

for ths in threads:
    ths.start()