from django.shortcuts import render
'''
render函数，根据视图提供的数据渲染响应

django将再文件views.py中查找函数index(),在将对象request传递给这个视图函数
'''
def index(request):
    """学习笔记的主页"""
    return render(request,'apps/index.html')

from .models import Topic     # 导入与所需数据相关联的模型
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')    # 查询数据库--请求提供Topic对象，并根据属性date_added排序
    context = {'topics':topics}                      # 定义一个将发送给模板的上下文（字典）
    return render(request,'apps/topics.html',context)