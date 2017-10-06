from django.contrib import admin

from footage.models import FootageDetail, Footage


@admin.register(Footage)
class FootageAdmin(admin.ModelAdmin):
    list_display = ['link', 'author', 'description']

@admin.register(FootageDetail)
class FootageDetailAdmin(admin.ModelAdmin):
    list_display = ['person', 'about_me', 'pricing', 'video_type', 'city', 'phone']
    list_filter = ['pricing', 'city']
    search_fields = ['pricing', 'city']
