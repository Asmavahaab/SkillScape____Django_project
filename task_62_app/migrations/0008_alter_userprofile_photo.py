# Generated by Django 5.0.6 on 2024-06-28 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_62_app', '0007_alter_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]