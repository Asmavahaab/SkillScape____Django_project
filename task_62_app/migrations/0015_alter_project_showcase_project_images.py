# Generated by Django 5.0.6 on 2024-06-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_62_app', '0014_project_showcase_project_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_showcase',
            name='project_images',
            field=models.ImageField(blank=True, upload_to='project_images/'),
        ),
    ]