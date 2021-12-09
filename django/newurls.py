"""定义应用程序apps下的url模式"""
from django.urls import path      # 导入函数path,因为需要使用它将url映射到视图

from . import views               # 句号，从当前urls.py所在的文件夹导入views.py

app_name = 'apps'
urlpatterns = [
    # 主页
    path('',views.index,name = 'index'),
    # 显示所有的主题
    path('topics/',views.topics,name = 'topics'),
]
# '':与基础url匹配
# views.index：指定了要调用views.py中的哪个函数
# name = 'index'：将这个URL模式的名称指定为index