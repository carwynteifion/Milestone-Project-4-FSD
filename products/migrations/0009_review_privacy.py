# Generated by Django 3.2.13 on 2022-07-02 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_review_privacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='privacy',
            field=models.BooleanField(default=False),
        ),
    ]
