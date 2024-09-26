from django.contrib import admin

# Register your models here.

from .models import Homework
from .models import Comment

admin.site.register(Homework)
admin.site.register(Comment)
