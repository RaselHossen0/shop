# Generated by Django 4.2 on 2023-04-26 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
