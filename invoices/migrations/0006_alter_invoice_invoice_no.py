# Generated by Django 3.2.8 on 2021-10-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0005_auto_20211007_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_no',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]