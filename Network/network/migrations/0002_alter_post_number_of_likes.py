# Generated by Django 3.2.8 on 2021-12-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='number_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]
