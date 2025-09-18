from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_first_name', 'get_last_name', 'gender', 'national_code', 'birthday_date')
    search_fields = ('username', 'full_name')
    ordering = ('ceremony_datetime',)

    def get_first_name(self, obj):
        return obj.get_first_and_last_name()['first_name']
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.get_first_and_last_name()['last_name']
    get_last_name.short_description = 'Last Name'


admin.site.register(CustomUser, CustomUserAdmin)
