# Generated by Django 3.0.3 on 2020-08-12 01:25

from django.db import migrations, models
import simditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_remove_userprofile_userindex'),
        ('article', '0009_category_creater'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', simditor.fields.RichTextField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('name', 'creater')},
        ),
    ]