# Generated by Django 2.2.6 on 2019-10-25 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='cover',
            new_name='cover1',
        ),
        migrations.AddField(
            model_name='project',
            name='cover2',
            field=models.ImageField(default='no image', upload_to='images/'),
            preserve_default=False,
        ),
    ]
