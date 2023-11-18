from django.contrib import admin
from .models import Record
# Register your models here.
class RecordAdmin(admin.ModelAdmin):
    list_display=['created_at','first_name','last_name','email','phone','city','state']
admin.site.register(Record,RecordAdmin)