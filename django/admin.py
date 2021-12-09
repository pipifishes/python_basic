from django.contrib import admin
'''
这些代码首先导入要注册的模型Topic；
models前的句号让django在admin.py所在的目录中查找models.py
'''
from .models import Topic
admin.site.register(Topic)

from .models import Entry
admin.site.register(Entry)