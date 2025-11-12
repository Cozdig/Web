from django.contrib import admin
from .models import Record

# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'main_info', 'publication_attribute')
    list_filter = ('heading', )
    search_fields = ('heading', 'main_info',)