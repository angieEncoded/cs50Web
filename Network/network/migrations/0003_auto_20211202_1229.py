# Generated by Django 3.2.8 on 2021-12-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_post_number_of_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='number_of_followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='number_of_following',
            field=models.IntegerField(default=0),
        ),
    ]
