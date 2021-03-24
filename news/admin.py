from django.contrib import admin

from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
#    list_filter = ['status']



admin.site.register(News,NewsAdmin)
