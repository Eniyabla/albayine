# Generated by Django 4.1 on 2022-09-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_media_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]