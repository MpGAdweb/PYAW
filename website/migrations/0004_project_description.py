# Generated by Django 2.2.6 on 2019-10-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20191028_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
