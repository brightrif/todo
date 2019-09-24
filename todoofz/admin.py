from django.contrib import admin

# Register your models here.
from . import models
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title",  "created_date", "due_date")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.Category, CategoryAdmin)
