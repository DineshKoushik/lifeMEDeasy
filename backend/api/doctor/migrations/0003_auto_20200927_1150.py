# Generated by Django 3.1.1 on 2020-09-27 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20200925_1959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='phone',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='address',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='gender',
        ),
    ]
