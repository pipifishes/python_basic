from django.contrib import admin
# from django.urls import path
from django.urls import path,include

'''
项目learning_log下的urls.py
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.urls'))      # 添加应用程序
]