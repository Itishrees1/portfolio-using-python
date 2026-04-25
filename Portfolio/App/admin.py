from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number')       # show in admin list
    list_filter = ('name', 'email', 'number')        # add filters in the sidebar
    search_fields = ('name', 'email', 'number', 'message')  # searchable fields
