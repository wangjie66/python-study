def f(n) :
    if n==1 :
        return 1
    else :
        return n * f(n-1)

print(f(5))

# 尾递归
def f_tail(n,i) :
    if n==1 :
        return i
    else :
        return f_tail(n-1,n*i)

print(f_tail(5,1))

