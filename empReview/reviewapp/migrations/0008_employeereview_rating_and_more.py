# Generated by Django 5.1.4 on 2025-01-06 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0007_rename_attendance_working_hours_employeereview_attendance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeereview',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employeereview',
            name='attendance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employeereview',
            name='attitude',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employeereview',
            name='bugs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employeereview',
            name='code_quality',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employeereview',
            name='communication',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employeereview',
            name='delivery_timelines',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employeereview',
            name='glacier_process',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employeereview',
            name='outstanding',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employeereview',
            name='technology',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employeereview',
            name='utilization',
            field=models.IntegerField(default=0),
        ),
    ]
