# Generated by Django 4.2 on 2023-04-26 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='nameOfCat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='item.category'),
        ),
    ]
