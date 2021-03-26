from django.contrib import admin

from news.models import News, Menu, Content, Images

class ContentImageInline(admin.TabularInline):
    model = Images
    extra = 5


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
#   list_filter = ['status']

class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'detail','news', 'image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['news']
    inlines = [ContentImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(News, NewsAdmin)
admin.site.register(Menu)
admin.site.register(Content,ContentAdmin)
admin.site.register(Images, ImagesAdmin)
