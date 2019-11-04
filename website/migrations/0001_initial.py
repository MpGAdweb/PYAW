# Generated by Django 2.2.6 on 2019-10-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('client', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('client_url', models.CharField(blank=True, max_length=200, null=True)),
                ('soluctions', models.CharField(blank=True, max_length=200, null=True)),
                ('project_date', models.DateField()),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
