# Generated by Django 5.1.6 on 2025-03-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0005_alter_order_id_alter_product_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[("Habitacion", "Habitacion")], max_length=50, null=True
            ),
        ),
    ]
