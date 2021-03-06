# Generated by Django 4.0.5 on 2022-06-16 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employment', '0007_rename_user_applicationstatus_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationstatus',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to=settings.AUTH_USER_MODEL, verbose_name='지원자'),
        ),
    ]
