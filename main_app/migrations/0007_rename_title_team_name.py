# Generated by Django 4.0.5 on 2022-06-09 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='title',
            new_name='name',
        ),
    ]