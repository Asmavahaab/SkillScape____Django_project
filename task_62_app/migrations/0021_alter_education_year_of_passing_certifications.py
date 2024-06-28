# Generated by Django 5.0.6 on 2024-06-28 13:17

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_62_app', '0020_education'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='year_of_passing',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2034)]),
        ),
        migrations.CreateModel(
            name='certifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('issuing_organisation', models.CharField(max_length=200)),
                ('date_of_issue', models.DateField(blank=True)),
                ('certificate_link', models.URLField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
