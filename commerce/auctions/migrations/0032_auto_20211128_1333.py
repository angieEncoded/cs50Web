# Generated by Django 3.2.8 on 2021-11-28 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0031_auto_20211128_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='high_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_high_bid', to='auctions.bid'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='item_id',
            field=models.IntegerField(),
        ),
    ]