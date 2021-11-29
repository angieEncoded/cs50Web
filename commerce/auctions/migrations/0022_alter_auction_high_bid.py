# Generated by Django 3.2.8 on 2021-10-31 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_auto_20211031_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='high_bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='high_bid', to='auctions.bid'),
        ),
    ]