from django.contrib import admin
from .models import Category, Article, Trending, Editor, Tech, Hotnews, Suggested, Catlist, Feedback, Sets

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Trending)
admin.site.register(Editor)
admin.site.register(Hotnews)
admin.site.register(Tech)
admin.site.register(Suggested)
admin.site.register(Catlist)
admin.site.register(Feedback)
admin.site.register(Sets)
