# Generated by Django 3.0.3 on 2020-06-26 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_remove_userprofile_userindex'),
        ('article', '0002_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.UserProfile'),
        ),
    ]
