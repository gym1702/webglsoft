from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'telefono', 'tipo', 'num_registro', )
    list_filter = ['tipo', ]
    search_fields = ['full_name', 'email', 'telefono', 'tipo',]


admin.site.register(User, UserAdmin)