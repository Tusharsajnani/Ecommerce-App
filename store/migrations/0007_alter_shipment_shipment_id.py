# Generated by Django 5.2.3 on 2025-06-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='shipment_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
