from django.contrib import admin
from .models import Company, JobPosting, ApplicationStatus

# Company 모델 어드민 페이지에 등록
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country', 'region']


# JobPosting 모델 어드민 페이지에 등록
@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'position', 'compensation', 'content', 'stack', 'created_at', 'updated_at']


# ApplicationStatus 모델 어드민 페이지에 등록
@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'applicant_id', 'jobposting_status_id']