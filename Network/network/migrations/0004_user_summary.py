# Generated by Django 3.2.8 on 2021-12-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_auto_20211202_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]