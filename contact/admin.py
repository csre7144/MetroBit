from django.contrib import admin
from .models import ContactList
# Register your models here.

class ContactListView(admin.ModelAdmin):
      list_display = ['name', 'email', 'phone']
      search_fields = ['name']
      list_filter = ['phone']



admin.site.register(ContactList, ContactListView)