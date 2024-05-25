# Generated by Django 4.2.13 on 2024-05-25 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollmentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_type', models.CharField(choices=[('Old Continuing', 'Old Continuing'), ('New', 'New'), ('OS', 'OS')], default='New', max_length=20)),
                ('student_year', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=10)),
                ('enrollment_status', models.CharField(choices=[('Enrolled', 'Enrolled'), ('Pre-Enrolled', 'Pre-Enrolled'), ('Dropped', 'Dropped'), ('Pending', 'Pending')], default='Pending', max_length=20)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='enrollment_detail_course', to='home.course')),
            ],
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_name', models.CharField(max_length=100, unique=True)),
                ('fee_amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_multiplier', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scholarship_name', models.CharField(max_length=250)),
                ('scholarship_description', models.CharField(max_length=250)),
                ('scholarship_type', models.CharField(choices=[('Full', 'Full'), ('Half', 'Half'), ('None', 'None')], default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectTaken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_pre_enroll', models.BooleanField(default=False)),
                ('is_registered', models.BooleanField(default=False)),
                ('is_dropped', models.BooleanField(default=False)),
                ('midterm_grade', models.CharField(max_length=20)),
                ('final_grade', models.CharField(max_length=20)),
                ('final_re_grade', models.CharField(max_length=20)),
                ('enrollment_detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_detail', to='home.enrollmentdetail')),
                ('schedule_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subject_taken_schedule', to='home.class_schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('or_no', models.CharField(max_length=20)),
                ('or_date', models.DateTimeField()),
                ('or_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('enrollment_detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_detail_payment', to='home.enrollmentdetail')),
            ],
        ),
        migrations.AddField(
            model_name='enrollmentdetail',
            name='scholarship_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='enrollment_detail_scholarship', to='home.scholarship'),
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_paid', models.BooleanField(default=False)),
                ('enrollment_detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_detail_assessment', to='home.enrollmentdetail')),
                ('fee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fees', to='home.fees')),
            ],
        ),
    ]
