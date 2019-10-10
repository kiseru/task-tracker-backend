from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'priority',
        'status',
        'user',
    )
    list_filter = (
        'priority',
        'status',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'created_at',
    )
