# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('order_date', models.DateField()),
                ('order_contact_name', models.CharField(max_length=75)),
                ('order_contact_phone', models.IntegerField(null=True)),
                ('order_contact_email', models.EmailField(blank=True, null=True, max_length=254)),
                ('order_is_complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('item_sku', models.IntegerField()),
                ('item_descr', models.CharField(max_length=40)),
                ('item_qty', models.IntegerField()),
                ('item_paid', models.BooleanField(default=False)),
                ('item_ordered', models.BooleanField(default=False)),
                ('item_ordered_date', models.DateField(blank=True, null=True)),
                ('item_ordered_po', models.IntegerField(blank=True, null=True)),
                ('item_arrived', models.BooleanField(default=False)),
                ('item_arrived_date', models.DateField(blank=True, null=True)),
                ('item_picked_up', models.BooleanField(default=False)),
                ('item_picked_up_date', models.DateField(blank=True, null=True)),
                ('item_order', models.ForeignKey(to='specialOrders.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_sap_id', models.IntegerField(primary_key=True, serialize=False)),
                ('vendor_name', models.CharField(max_length=50)),
                ('vendor_availability', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='order_item',
            name='item_vendor',
            field=models.ForeignKey(to='specialOrders.Vendor'),
        ),
    ]
