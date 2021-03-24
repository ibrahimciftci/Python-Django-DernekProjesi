from django.contrib import admin

from news.models import News, Menu, Content


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']


#    list_filter = ['status']

class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'detail','news']
    list_filter = ['news']

admin.site.register(News, NewsAdmin)
admin.site.register(Menu)
admin.site.register(Content,ContentAdmin)
