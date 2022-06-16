# Generated by Django 4.0.5 on 2022-06-15 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(max_length=50, verbose_name='국가'),
        ),
        migrations.AlterField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, verbose_name='회사명'),
        ),
        migrations.AlterField(
            model_name='company',
            name='region',
            field=models.CharField(max_length=50, verbose_name='지역'),
        ),
        migrations.AlterField(
            model_name='company',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_jobposting', to='employment.company', verbose_name='회사_id'),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='compensation',
            field=models.PositiveIntegerField(default=1000000, verbose_name='채용보상금'),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='content',
            field=models.TextField(verbose_name='채용내용'),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='position',
            field=models.CharField(max_length=100, verbose_name='채용포지션'),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='stack',
            field=models.TextField(verbose_name='사용기술'),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
    ]
