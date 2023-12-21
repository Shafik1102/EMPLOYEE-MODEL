from django.contrib import admin
from webapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
	list_display=['no','name','city','mobile','salary','expirence','position']
admin.site.register(Employee,EmployeeAdmin)