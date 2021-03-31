from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from content.models import Category, Content, Images


class ContentImageInline(admin.TabularInline):
    model = Images
    extra = 5


#   list_filter = ['status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'detail', 'category', 'image_tag']
    readonly_fields = ('image_tag',)
    inlines = [ContentImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ('image_tag',)


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_contents_count', 'related_contents_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Content,
            'category',
            'contents_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Content,
                                                'category',
                                                'contents_count',
                                                cumulative=False)
        return qs

    def related_contents_count(self, instance):
        return instance.contents_count
    related_contents_count.short_description = 'Related contents (for this specific category)'

    def related_contents_cumulative_count(self, instance):
        return instance.contents_cumulative_count
    related_contents_cumulative_count.short_description = 'Related contents (in tree)'


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Content, ContentAdmin)
admin.site.register(Images, ImagesAdmin)
