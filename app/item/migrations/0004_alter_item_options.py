# Generated by Django 4.2 on 2023-04-25 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['name']},
        ),
    ]
