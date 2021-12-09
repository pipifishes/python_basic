class Circle(object):              # 定义一个类
    pi = 3.14                      # 类变量

    def __init__(self,r):          # 实例变量
        self.r = r

    def get_area(self):
        return self.r**2 * self.pi

    def get_perimeter(self):
        return self.r* 2 * self.pi

circle1 = Circle(1)
print(circle1.get_area())          # 调用方法self不需要传入参数
print(circle1.get_perimeter())

###################################################################################################

class CLanguage:
    '''这是一个学习Python定义的一个类'''
    def __init__(self,name,add):
        self.name = name
        self.add = add
        print(name,"的网址为:",add)

# 创建 a 对象，并传递参数给构造函数
a = CLanguage("C语言中文网","http://c.biancheng.net")

###################################################################################################

class CLanguage :
    # 下面定义了2个类变量
    name = "C语言中文网"
    add = "http://c.biancheng.net"
    def __init__(self,name,add):
        #下面定义 2 个实例变量
        self.name = name
        self.add = add
        print(name,"网址为：",add)
    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)
# 将该CLanguage对象赋给clanguage变量
clanguage = CLanguage("C语言中文网","http://c.biancheng.net")