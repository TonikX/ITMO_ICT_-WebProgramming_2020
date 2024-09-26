from django.contrib import admin
from kursovik.models import Worktable,Client,Room,Journal,Worker
# Register your models here.

admin.site.register(Worktable)
admin.site.register(Journal)
admin.site.register(Worker)
admin.site.register(Room)
admin.site.register(Client)