import threading
global_dict = {}

def std_thread():
    std = '1212'
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread()] = std
    print(len(global_dict),std,threading.current_thread())
    do_task_1()
    do_task_2()

def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]
    print(len(global_dict),std,threading.current_thread())

def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]
    print(len(global_dict),std,threading.current_thread())

# std_thread()

local_school  = threading.local()

def process_thread(name):
    local_school.student= name
    # 记住这里不能用process_thread的名称，会导致thread无法识别参数个数
    process_thread1()

def process_thread1():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

from multiprocessing import Pool
if __name__ == '__main__' :
    pool = Pool(4)
    for i in range(100):
        pool.apply_async(process_thread,args=('Alice',))
        pool.apply_async(process_thread,args=('Bob',))
    pool.close()
    pool.join()


# t1.start()
# t2.start()
# t1.join()
# t2.join()