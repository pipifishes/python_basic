from django.db import models

'''
我们创建了一个名为Topic的类，他继承Model;我们添个两个属性
'''
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)       # CharField--由字符组成的数据，用来存储主题名，并需要告知django需要在数据库中预留多少空间：200字符
    date_added = models.DateTimeField(auto_now_add=True)  # DateTimeField,记录日期和时间的数据，每当用户创建新主题的时候，自动设置为最新时间

    def __str__(self):              # 告诉django，默认使用哪个属性来显示有关主题的信息
        """返回模型字符串表示"""
        return self.text


class Entry(models.Model):                    # Entry也继承Model的类
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)    # 数据库的外键；级联删除
    text = models.TextField()                                      # 这种字段的长度不受限制
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:                                                    # 嵌套了Meta类，存储用于管理模型的额外信息
        verbose_name_plural = 'entries'                            # 特殊属性，让django在需要使用entries来表示多个条目

    def __str__(self):
        return f"{self.text[:50]}..."                              # 只显示text的前50个字符

