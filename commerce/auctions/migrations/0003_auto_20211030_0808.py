# Generated by Django 3.2.8 on 2021-10-30 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctions_bids'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctions',
            name='item_name',
            field=models.CharField(default='empty', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bids',
            name='item_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_item', to='auctions.auctions'),
        ),
    ]