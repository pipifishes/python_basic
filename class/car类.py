# # -*- coding:UTF-8 -*-

class Car:                                               # 类的首字母需要大写，这个类定义中没有圆括号（因为要从空白创建这个类）

    def __init__(self,make,model,year):                  # 方法，这里有4个形参
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):                     #  新方法
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print(f"this car has {self.odometer_reading} miles on it")

mynewcar = Car('audi','a4',2019)                        # 根据类创建的实例
print(mynewcar.get_descriptive_name())                  # 调用方法（实例.方法）

