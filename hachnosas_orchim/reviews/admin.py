from django.contrib import admin
from .models import Reviews


# Register your models here.
# admin.site.register(Reviews)

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'created_by', 'comment', 'created_at', 'updated_at')
    list_display_links = ('review_id', 'created_by')
    list_filter = ('created_at',)
    search_fields = ('created_by', 'comment')
    list_per_page = 25


admin.site.register(Reviews, ReviewsAdmin)
