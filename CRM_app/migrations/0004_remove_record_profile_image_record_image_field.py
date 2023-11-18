# Generated by Django 4.2.7 on 2023-11-18 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM_app', '0003_record_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='record',
            name='image_field',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
