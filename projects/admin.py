from django.contrib import admin

from django.contrib import admin
from .models import *

admin.site.register(Project)
admin.site.register(Student)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    readonly_fields = ('last_submitted',)
