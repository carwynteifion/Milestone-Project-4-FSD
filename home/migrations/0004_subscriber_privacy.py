# Generated by Django 3.2.13 on 2022-07-02 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_subscriber_privacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='privacy',
            field=models.BooleanField(default=False),
        ),
    ]
