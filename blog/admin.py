from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(postModel)
@admin.register(postModel)
class Posts_adm(admin.ModelAdmin):
    list_display=("id", 'title', 'date')