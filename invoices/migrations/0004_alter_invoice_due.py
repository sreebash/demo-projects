# Generated by Django 3.2.8 on 2021-10-06 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_auto_20211006_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='due',
            field=models.PositiveBigIntegerField(max_length=200),
        ),
    ]
