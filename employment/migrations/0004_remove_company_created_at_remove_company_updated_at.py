# Generated by Django 4.0.5 on 2022-06-15 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0003_alter_jobposting_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='company',
            name='updated_at',
        ),
    ]
