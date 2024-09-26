from django.contrib import admin
from project_first_app.models import *
# Register your models here.
admin.site.register(Hotel)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active','datein','dateout','rating')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')