list1 = [1,24,5,56,3,'hdl','wdl',2323]

print(list1[0:3])
print(list1[1:3])
print(list1[-1])
print(list1[-1:])
print(list1[:-1])
print(list1[-2:0])


list = list(range(100))
print(list[:10:2])
print(list[::5])


t=(0,2,4,5,2,2)
print(t[:4])

n =" "
print('bool' , bool(n))
print('bool' , bool( ))

def trim(s):
    c = s[::1]
    s1 = ''
    i=0
    for n in c :
        if n==' ':
            i=i+1
        else :
            break
    s = s[i::1] ;
    c = len(s)
    while(c>0):
        c = c- 1
        if s[-1] == ' ':
            s=s[:len(s)-2]
    return s

if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败23!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')