# Generated by Django 5.1.3 on 2025-01-30 05:34

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placementapps', '0009_tutornotification_delete_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentnotification',
            old_name='seen',
            new_name='is_read',
        ),
        migrations.AlterField(
            model_name='studentnotification',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='studentnotification',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placementapps.job'),
        ),
        migrations.AlterField(
            model_name='studentnotification',
            name='message',
            field=models.TextField(),
        ),
    ]
