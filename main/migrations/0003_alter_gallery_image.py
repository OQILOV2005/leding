# Generated by Django 4.2.3 on 2023-09-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='Gallery/'),
        ),
    ]