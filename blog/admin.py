from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(postModel)
@admin.register(postModel)
class Posts_adm(admin.ModelAdmin):
    list_display=("id", 'title', 'date')
    

admin.site.register(profileModel)

admin.site.register(Comment)

@admin.register(CategoryModel)
class categoryModelAdmin(admin.ModelAdmin):
    list_display=("name",)
