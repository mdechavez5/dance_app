# Generated by Django 4.0.5 on 2022-06-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_profile_bio_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='NYC', max_length=100),
            preserve_default=False,
        ),
    ]
