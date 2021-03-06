# Generated by Django 3.2.8 on 2021-11-25 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='high_bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_high_bid', to='auctions.bid'),
        ),
    ]
