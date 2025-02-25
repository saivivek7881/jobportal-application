from django.contrib import admin
from .models import Job, JobApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'company_name', 'location')

from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job', 'applied_at')  # Use valid fields
    list_filter = ('applied_at',)  # Filter by date of application
    search_fields = ('name', 'email', 'job__title')  # Search by name, email, and job title
