from django.contrib import admin
from .models import Media, Media_Type


# Register your models here.
# admin.site.register(Media_Type)
# admin.site.register(Media)

class MediaAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'file_type', 'created_at')
    list_filter = ('file_type',)
    search_fields = ('file_type', 'mime_type')
    ordering = ('-created_at',)


admin.site.register(Media, MediaAdmin)
admin.site.register(Media_Type)
