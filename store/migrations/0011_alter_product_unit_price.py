# Generated by Django 5.0.6 on 2024-07-07 22:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_product_description_alter_product_inventory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.DecimalField(decimal_places=3, max_digits=10, max_length=100, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]