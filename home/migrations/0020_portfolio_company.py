# Generated by Django 4.1 on 2022-09-07 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_portfolio_link_alter_about_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
