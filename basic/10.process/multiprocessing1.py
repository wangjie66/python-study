import os

print('no : ', os.getpid())

# only in Unix/Linux/Mac
# pid = os.fork()
# print(pid)



from multiprocessing import Process
def run_proc(name):
    print(os.getpid())

# if __name__=='__main__':
#     p = Process(target=run_proc,args=('test',))
#     p.start()
#     p.join()
#     print('end')


from multiprocessing import Pool
import time,random,pdb

def long_time_task(name):
    print('name:',name)
    print('%s , %s' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('%s , %s' % (name , end-start))


# if __name__=='__main__':
#     print(os.getpid())
#     print(list(range(5)))
#     pool = Pool(2)
#     # pdb.set_trace()
#     for i in range(5):
#         pool.apply_async(long_time_task,args=(i,))
#     print('waiting...')
#     pool.close()
#     # join方法会引起main意外的方法 按线程数打印？
#     pool.join()
#     print('done...')



import subprocess

# r = subprocess.call(['nslookup','www.python.org'])
# print(r)

'''
进程间的通信
'''
from multiprocessing import Process,Queue
import os,time,random

def write(q):
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
