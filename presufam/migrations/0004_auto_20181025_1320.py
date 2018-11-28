# Generated by Django 2.1.2 on 2018-10-25 18:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presufam', '0003_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.001)]),
        ),
    ]