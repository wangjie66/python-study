from io  import  StringIO

# 写内存
f = StringIO()
f.write("hello")
print(f.getvalue())


from io import BytesIO
f=BytesIO()
f.write("中国".encode('utf-8'))
f.write("中国".encode('gbk'))
print(f.getvalue())

f=BytesIO()
f.write(b'\xe4\xb8\xad\xe5\x9b\xbd')
print(f.getvalue().decode('utf-8'))