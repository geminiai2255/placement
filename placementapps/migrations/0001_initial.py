# Generated by Django 5.1.3 on 2025-01-13 08:05

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('trainer_name', models.CharField(max_length=255)),
                ('venue', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('training_dates', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='company_logos/')),
                ('job_type', models.CharField(choices=[('full-time', 'Full-Time'), ('part-time', 'Part-Time')], default='full-time', max_length=10)),
                ('description', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('responsibilities', models.TextField(max_length=500)),
                ('qualifications', models.TextField(max_length=500)),
                ('vacancy', models.PositiveIntegerField(default=1)),
                ('passoutyear', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='placementapps.tbl_department')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='placementapps.tbl_department')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=50)),
                ('reg_no', models.CharField(max_length=50)),
                ('student_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=50)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_phone', models.CharField(max_length=10)),
                ('parent_phone', models.CharField(max_length=10)),
                ('address', models.TextField(max_length=128)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('password', models.CharField(max_length=128)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('supply', models.PositiveIntegerField(blank=True, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('pancard_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('batch', models.CharField(blank=True, max_length=100, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='placementapps.course')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='placementapps.tbl_department')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('job_application', 'Job Application'), ('other', 'Other')], default='other', max_length=20)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placementapps.course')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placementapps.job')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placementapps.tbl_student')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_on', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placementapps.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placementapps.tbl_student')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('mobile_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='tutor_images/')),
                ('batch', models.CharField(max_length=9)),
                ('status', models.CharField(default='pending', max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutors', to='placementapps.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutors', to='placementapps.tbl_department')),
            ],
        ),
        migrations.CreateModel(
            name='T_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placementapps.job')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placementapps.tbl_student')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placementapps.tbl_tutor')),
            ],
        ),
        migrations.CreateModel(
            name='SessionApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_on', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placementapps.tbl_student')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placementapps.trainingsession')),
            ],
        ),
    ]
