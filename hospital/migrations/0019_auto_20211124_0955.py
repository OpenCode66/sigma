# Generated by Django 3.0.5 on 2021-11-24 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='address',
            new_name='hospital',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='symptoms',
        ),
    ]
