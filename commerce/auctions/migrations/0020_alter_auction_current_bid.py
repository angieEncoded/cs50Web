# Generated by Django 3.2.8 on 2021-10-31 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_alter_auction_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='current_bid',
            field=models.FloatField(default=0),
        ),
    ]
