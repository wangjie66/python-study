def lazy_sum(*num):
    def sum():
        m =0 ;
        for n in num :
            m = m+ n
        return  m
    return sum

f = lazy_sum(2,43,5,6)
print(f)
print(f())


'''
闭包
'''
