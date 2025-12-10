from django.contrib import admin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'avatar', 'phone_number', 'country', 'password')
    list_filter = ('username', )
    search_fields = ('username',)