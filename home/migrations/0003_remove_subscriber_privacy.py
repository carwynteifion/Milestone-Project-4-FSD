# Generated by Django 3.2.13 on 2022-07-02 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_subscribers_subscriber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='privacy',
        ),
    ]