# Generated by Django 2.2.7 on 2019-11-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191111_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='null'),
            preserve_default=False,
        ),
    ]