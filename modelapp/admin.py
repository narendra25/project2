from django.contrib import admin
from modelapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','sno','sname','scourse','smarks']

admin.site.register(Student,StudentAdmin)
