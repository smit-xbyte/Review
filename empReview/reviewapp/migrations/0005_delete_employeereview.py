# Generated by Django 5.1.4 on 2025-01-06 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0004_alter_employeereview_review_month'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmployeeReview',
        ),
    ]
