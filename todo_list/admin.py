from django.contrib import admin
from .models import List

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'completed')
    list_editable = ('completed',)
    search_fields = ('item',)
