from django.contrib import admin
from .models import Asgard


class CustomAsgard(admin.ModelAdmin):
    list_display = ['id', 'geography', 'history', 'culture', 'language']
admin.site.register(Asgard, CustomAsgard)