# Generated by Django 2.2.6 on 2019-10-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='soluctions',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
