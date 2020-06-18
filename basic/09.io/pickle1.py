import pickle

d = dict(name='Bob', age=20, score=88)
# b = pickle.dumps(d)

# 保存到文件
f = open('D:\\1.txt','wb')
pickle.dump(d,f)
f.close()

# 反序列化
f = open('D:\\1.txt','rb')
d = pickle.load(f)
f.close()
print(d)


'''
JSON类型	Python类型
{}	dict
[]	list
"string"	str
1234.56	int或float
true/false	True/False
null	None
'''

import  json
d = dict(name='Bob', age=20, score=88)
print('s:',json.dumps(d))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(Student('wj',18,150),default=student2dict))
# print(json.dumps(s, default=lambda obj: obj.__dict__))
print(json.dumps(Student('wj',18,150),default=lambda student2dict: student2dict.__dict__))

# 反序列化

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

# ensure_ascii 不进行ascii编码
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)  #{"name": "小明", "age": 20}
s = json.dumps(obj, ensure_ascii=True)  #{"name": "\u5c0f\u660e", "age": 20}

