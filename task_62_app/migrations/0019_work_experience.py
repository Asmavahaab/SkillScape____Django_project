# Generated by Django 5.0.6 on 2024-06-28 12:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_62_app', '0018_alter_project_showcase_project_images'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='work_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('job_title', models.CharField(blank=True, max_length=200)),
                ('mode', models.CharField(max_length=6)),
                ('start_date', models.DateField(blank=True)),
                ('duration', models.CharField(max_length=10)),
                ('responsibilities', models.TextField(max_length=10000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
