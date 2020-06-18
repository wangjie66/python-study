import os
print(os.name)
print(os.environ)
print(os.environ.get('path'))

# 看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('D:\\','111'))
print(os.path.split('D:\\12\\34\\34'))
print(os.path.splitext('D:\\12\\34\\34.p.df'))

# os.mkdir('D:\\111')
# os.rmdir('D:\\111')

'''
文件操作
'''
# os.rename('text.txt','test.pdf')
# os.remove('text.txt')

x = [x for x in os.listdir('.') if os.path.isdir(x)]
print(x)
x = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(x)