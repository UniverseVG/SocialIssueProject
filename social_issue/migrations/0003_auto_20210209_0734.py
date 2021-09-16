# Generated by Django 3.1.6 on 2021-02-09 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_issue', '0002_auto_20210208_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialissuecomment',
            name='submit_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date/Time Commented'),
        ),
        migrations.AlterField(
            model_name='socialissuelike',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date/Time Liked'),
        ),
    ]
