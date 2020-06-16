class stu():
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s1 = stu()
# print(s1.score)
s1.score = 37
print(s1.score)


'''
测试
'''

class Screen(object):
    _resolution = 786432
    @property
    def width(self):
       return self._width
    @property
    def height(self):
       return self._height
    @property
    def resolution(self):
       return self._resolution
    @width.setter
    def width(self,v):
       self._width = v
    @height.setter
    def height(self,v):
       self._height = v


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')