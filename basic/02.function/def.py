def my_abs(a):
    if not isinstance(a,(int,float)):
        raise  TypeError('basd')
    if a>0 :
        return a
    else :
        return -a

print(my_abs(-4))
# print(my_abs('sdf'))

def none():
    pass

def move(x,y):
    nx = x+y
    ny = x-y
    return nx,ny

x,y = move(3,5)
print (x,y)
r = move(3,5)
print(r)