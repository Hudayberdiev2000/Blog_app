# Generated by Django 4.2.7 on 2024-01-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_email_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
