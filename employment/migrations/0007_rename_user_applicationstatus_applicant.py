# Generated by Django 4.0.5 on 2022-06-16 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0006_remove_jobposting_user_jobposting_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationstatus',
            old_name='user',
            new_name='applicant',
        ),
    ]