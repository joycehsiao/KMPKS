# Generated by Django 3.0.3 on 2020-08-10 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_auto_20200810_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlegroup',
            old_name='categoriess',
            new_name='categories',
        ),
    ]