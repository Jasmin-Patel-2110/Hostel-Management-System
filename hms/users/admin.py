from django.contrib import admin

from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('enrollment_number', 'name', 'branch', 'semester', 'status', 'date_joined')
    search_fields = ('enrollment_number', 'name', 'branch', 'email')
    list_filter = ('branch', 'semester', 'status', 'gender')
    ordering = ('-date_joined',)