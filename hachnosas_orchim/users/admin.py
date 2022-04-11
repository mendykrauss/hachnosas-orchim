from django.contrib import admin
from .models import Users


# Register your models here.
# admin.site.register(Users)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': 'username'}
         ),
    )
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(Users, UsersAdmin)
