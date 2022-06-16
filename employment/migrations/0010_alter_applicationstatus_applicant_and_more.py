# Generated by Django 4.0.5 on 2022-06-16 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employment', '0009_rename_jobposting_applicationstatus_jobposting_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationstatus',
            name='applicant',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to=settings.AUTH_USER_MODEL, verbose_name='지원자'),
        ),
        migrations.AlterField(
            model_name='applicationstatus',
            name='jobposting_status',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='employment.jobposting', verbose_name='채용공고'),
        ),
    ]