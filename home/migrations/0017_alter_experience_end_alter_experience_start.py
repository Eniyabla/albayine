# Generated by Django 4.1 on 2022-09-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start',
            field=models.DateField(),
        ),
    ]