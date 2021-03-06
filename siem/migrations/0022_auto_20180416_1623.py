# Generated by Django 2.0.4 on 2018-04-16 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siem', '0021_auto_20180409_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='limitrule',
            old_name='match_friendlist',
            new_name='match_allowlist',
        ),
        migrations.AlterField(
            model_name='logevent',
            name='ext0',
            field=models.CharField(default='', max_length=192),
        ),
        migrations.AlterField(
            model_name='logevent',
            name='ext1',
            field=models.CharField(default='', max_length=192),
        ),
        migrations.AlterField(
            model_name='logevent',
            name='path',
            field=models.CharField(default='', max_length=256),
        ),
    ]
