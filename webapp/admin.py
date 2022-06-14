from django.contrib import admin

# Register your models here.
# 别忘了导入ArticlerPost
from .models import ArticlePost
# 注册ArticlePost到admin中
admin.site.register(ArticlePost)

from .models import ArticleColumn
# 注册文章栏目
admin.site.register(ArticleColumn)