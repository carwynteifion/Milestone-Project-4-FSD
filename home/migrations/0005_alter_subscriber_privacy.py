# Generated by Django 3.2.13 on 2022-07-02 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_subscriber_privacy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='privacy',
            field=models.BooleanField(),
        ),
    ]
