# Generated by Django 4.2.3 on 2023-08-20 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0008_alter_sale_amount_recieved_alter_sale_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='issued_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='recieved_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]