# Generated by Django 3.0.3 on 2020-09-16 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20200916_2048'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]