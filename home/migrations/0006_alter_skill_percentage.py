# Generated by Django 4.1 on 2022-09-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_skill_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='Percentage',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]