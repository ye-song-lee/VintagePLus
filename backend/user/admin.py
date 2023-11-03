from django.contrib import admin
from .models import User
from .models import Items

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'registered_dttm')

admin.site.register(User, UserAdmin)
admin.site.register(Items)