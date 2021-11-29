# Generated by Django 3.2.8 on 2021-11-25 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0026_alter_auction_high_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auction_winner', to=settings.AUTH_USER_MODEL),
        ),
    ]