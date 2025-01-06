from django.db import models
import datetime

class EmployeeReview(models.Model):
    email = models.EmailField()
    emp_id = models.CharField(max_length=50)
    developer_name = models.CharField(max_length=100)
    team_leader = models.CharField(max_length=100, blank=True, null=True)
    project_manager = models.CharField(max_length=100, blank=True, null=True)
    review_month = models.DateField()
    delivery_timelines = models.IntegerField(default=0)
    utilization = models.IntegerField(default=0)
    technology = models.IntegerField(default=0)
    attitude = models.IntegerField(default=0)
    code_quality = models.IntegerField(default=0)
    communication = models.IntegerField(default=0)
    glacier_process = models.IntegerField(default=0)
    bugs = models.IntegerField(default=0)
    attendance = models.IntegerField(default=0)
    outstanding = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employee_review'

    def __str__(self):
        return f"{self.developer_name} - {self.review_month}"
