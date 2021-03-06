# Generated by Django 3.1.6 on 2021-02-08 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_issue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialissue',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='socialissue',
            name='submit_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date/Time Submited'),
        ),
        migrations.AlterField(
            model_name='socialissuecomment',
            name='social_issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='social_issue.socialissue'),
        ),
        migrations.AlterField(
            model_name='socialissuelike',
            name='social_issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='social_issue.socialissue'),
        ),
    ]
