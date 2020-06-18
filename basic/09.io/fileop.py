f =open("C:\\Users\\sz\\Desktop\\log.log",'r')
# print(f.read())
# 每次调用都要关闭
f.close()

# 换一个简洁的写法
with open("C:\\Users\\sz\\Desktop\\log.log",'r') as f2:
    # print(f2.read())
    # 文本太多，容易导致内存不足
    print(f2.read(10))

with open("C:\\Users\\sz\\Desktop\\log.log",'r') as f2:
    for lines in f2.readlines():
        print(lines)

# 二进制用rb
f =open("C:\\Users\\sz\\Desktop\\log.log",'rb')
# f =open("C:\\Users\\sz\\Desktop\\开源三方件清单.png",'rb')
print(f.read())

# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

# 写文件  用w 或者wb
# >>> f = open('/Users/michael/test.txt', 'w')
# >>> f.write('Hello, world!')
# >>> f.close()