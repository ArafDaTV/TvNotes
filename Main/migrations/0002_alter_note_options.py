# Generated by Django 4.0.1 on 2022-07-07 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['last_updated']},
        ),
    ]
