# Generated by Django 5.0.6 on 2024-05-28 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_enrollmentdetail_fees_scholarship_subjecttaken_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='class_schedule',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_class_schedule', to='home.course'),
        ),
    ]