# Generated by Django 4.2 on 2023-04-27 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_item_nameofcat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
