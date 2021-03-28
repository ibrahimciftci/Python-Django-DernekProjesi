from django.contrib import admin

from content.models import Category, Content, Images


class ContentImageInline(admin.TabularInline):
    model = Images
    extra = 5


#   list_filter = ['status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'detail', 'image_tag']
    readonly_fields = ('image_tag',)
    inlines = [ContentImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Images, ImagesAdmin)
