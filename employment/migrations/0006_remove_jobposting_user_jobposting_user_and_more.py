# Generated by Django 4.0.5 on 2022-06-16 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employment', '0005_jobposting_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobposting',
            name='user',
        ),
        migrations.AddField(
            model_name='jobposting',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='지원자'),
        ),
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobposting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employment.jobposting', verbose_name='채용공고')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='지원자')),
            ],
        ),
    ]
