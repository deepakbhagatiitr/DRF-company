from django.contrib import admin
from .models import Company, Employee

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type', 'added_date', 'active')
    search_fields = ('name', 'location')
    list_filter = ('type', 'active')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'position')
    search_fields = ('name', 'email', 'position')
    list_filter = ('position', 'company')
