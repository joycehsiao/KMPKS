# Generated by Django 3.0.3 on 2020-09-20 08:43

from django.db import migrations
import simditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0018_auto_20200919_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=simditor.fields.RichTextField(),
        ),
    ]