# Generated by Django 4.2.13 on 2024-05-25 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_subject_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospectus',
            name='prospectus_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]