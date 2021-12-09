# # -*- coding:UTF-8 -*-

class Dog:                              # 类的首字母需要大写，这个类定义中没有圆括号（因为要从空白创建这个类）

    def __init__(self,name,age):        # 方法，这里有3个形参
        '''初始化属性name和age'''
        self.name = name                # 属性
        self.age = age
    def sit(self):                      # 新方法
        '''模拟小狗收到命令时蹲下'''
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        '''模拟小狗收到命令时打滚'''
        print(f"{self.name} rolled over.")

mydog = Dog('white','6')                # 根据类创建的实例
print("小狗的名字是：",mydog.name)         # 访问属性（实例.属性）
mydog.sit()                             # 调用方法（实例.方法）

yourdog = Dog('wangwang','3')           # 创建另一个实例
