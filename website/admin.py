from django.contrib import admin
from .models import Project

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("client",)}


admin.site.register(Project, ArticleAdmin)
