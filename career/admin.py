from django.contrib import admin
from .models import career
# Register your models here.

class careerView(admin.ModelAdmin):
      list_display = ['firstname', 'lastname', 'email', 'phone', 'document']


admin.site.register(career, careerView)