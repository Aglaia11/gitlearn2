#!/user/bin/env python
# -*- coding:utf-8-*-
import Queue
import threading
import time
import sys,os
queue = Queue.Queue()
out_queue = Queue.Queue()


class ThreadNum(threading.Thread):
    """bkeep"""

    def __init__(self, queue, out_queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        while True:
        # 从队列中取消息
            num = self.queue.get()
            bkeep = num
            for i in range(10000):
                bkeep=bkeep+i

           # print bkeep
        # 将bkeep放入队列中

            self.out_queue.put(bkeep)

        # signals to queue job is done
            self.queue.task_done()


def readqueue(out_queue):
        valuelist=[]
        while out_queue.qsize()>0:
     #       print out_queue.qsize()
            valuelist.append(out_queue.get())
    #    print valuelist
        return valuelist


start = time.time()


def main():
    # populate queue with data
    for num in range(100):
        queue.put(num)

    # spawn a pool of threads, and pass them queue instance
    end1=time.time()
    N=int(sys.argv[1])
    for i in range(N):
        t = ThreadNum(queue, out_queue)
        t.setDaemon(True)
        t.start()
    queue.join()
    end2=time.time()
    print "Thread Time:%s"% (end2-end1)
    valuelist=readqueue(out_queue)
  #  print valuelist
    print "readqueue Time:%s" %(time.time()-end2)
    #for i in range(5):
     #   pl = PrintLove(out_queue)
      #  pl.setDaemon(True)
       # pl.start()

    # wait on the queue until everything has been processed



main()
print"Elapsed Time: %s" % (time.time() - start)

