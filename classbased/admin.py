from django.contrib import admin
from classbased.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['sno','sname','sage','scity']

admin.site.register(Student,StudentAdmin)
