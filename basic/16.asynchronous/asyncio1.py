import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

'''
错误的写法
'''
# hello = hello()
# hello.send(None)
# for i in range(5):
#     hello.send()

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
for i in range(1):
    loop.run_until_complete(hello())
    for j in range(4):
        print(j)
# loop.close()


'''
PS:Python 3.5开始引入了新的语法async和await，
1.把@asyncio.coroutine替换为async；
2.把yield from替换为await。
'''


async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
for i in range(1):
    loop.run_until_complete(hello())
    for j in range(4):
        print(j)

import threading
import asyncio

@asyncio.coroutine
def hello1():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop1 = asyncio.get_event_loop()
tasks = [hello1(), hello1()]
loop1.run_until_complete(asyncio.wait(tasks))
# loop1.close()


'''
3个连接由一个线程通过coroutine并发完成
asyncio提供了完善的异步IO支持；
异步操作需要在coroutine中通过yield from完成；
多个coroutine可以封装成一组Task然后并发执行。
'''
import asyncio
@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()