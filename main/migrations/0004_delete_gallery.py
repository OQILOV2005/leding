# Generated by Django 4.2.3 on 2023-09-26 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_gallery_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]