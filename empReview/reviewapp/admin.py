from django.contrib import admin
from .models import EmployeeReview

@admin.register(EmployeeReview)
class EmployeeReviewAdmin(admin.ModelAdmin):
    # Columns displayed in the list view
    list_display = (
        'developer_name', 'emp_id', 'review_month', 
        'team_leader', 'project_manager', 'utilization', 
        'technology', 'attitude', 'remarks'
    )

    # Add filters to the sidebar
    list_filter = ('review_month', 'team_leader', 'project_manager', 'utilization')

    # Fields to be searchable
    search_fields = ('developer_name', 'emp_id', 'remarks')

    # Default ordering of records
    ordering = ('-review_month',)

    # Add pagination to improve performance
    list_per_page = 20  # Show 20 items per page

    # Fieldsets to organize the fields on the add/edit view
    fieldsets = (
        (None, {
            'fields': ('developer_name', 'emp_id', 'email')
        }),
        ('Review Information', {
            'fields': (
                'review_month', 'team_leader', 'project_manager', 
                'delivery_timelines', 'utilization', 
                'technology', 'attitude'
            ),
        }),
        ('Performance', {
            'fields': (
                'code_quality', 'communication', 'glacier_process', 
                'bugs', 'attendance_working_hours', 'outstanding_performance'
            ),
        }),
        ('Remarks', {
            'fields': ('remarks',)
        }),
    )
    
    # Optionally, set readonly fields for certain fields
    readonly_fields = ('email',)
