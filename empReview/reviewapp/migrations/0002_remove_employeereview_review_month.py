# Generated by Django 5.1.4 on 2025-01-06 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeereview',
            name='review_month',
        ),
    ]
