# Generated by Django 3.2.13 on 2022-06-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220623_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_book',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
