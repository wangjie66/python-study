import os

print(os.getpid())

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
    print('%s , %s' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('%s , %s' % (name , end-start))

if __name__=='__main__':
    print(list(range(5)))
    pool = Pool(4)
    # pdb.set_trace()
    for i in range(5):
        pool.apply_async(long_time_task,args=(i,))
    print('waiting...')
    pool.close()
    pool.join()
    print('done...')



