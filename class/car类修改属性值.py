# # -*- coding:UTF-8 -*-
'''
修改属性值
'''
class Car:                                               # 类的首字母需要大写，这个类定义中没有圆括号（因为要从空白创建这个类）

    def __init__(self,make,model,year):                  # 方法，这里有4个形参
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0                        # 初始值设为0

    def get_descriptive_name(self):                     #  新方法
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print(f"this car has {self.odometer_reading} miles on it")

    def update_odometer(self,mileage):
        '''第二种方法新增的函数,将里程数设为指定的值'''
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        '''第三种方法新增的函数,将里程数增加指定的值'''
        self.odometer_reading += miles

mynewcar = Car('audi','a4',2019)                        # 根据类创建的实例
print(mynewcar.get_descriptive_name())                  # 调用方法（实例.方法）
mynewcar.read_odometer()                                # 调用方法（实例.方法）

# 1.直接修改属性的值
mynewcar.odometer_reading = 100
mynewcar.read_odometer()
# 2.通过方法修改属性的值
mynewcar.update_odometer(200)
mynewcar.read_odometer()
# 3.通过方法对属性的值进行递增
mynewcar.increment_odometer(300)
mynewcar.read_odometer()
