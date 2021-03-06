# Generated by Django 3.2.8 on 2021-12-02 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_rename_followers_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='following',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='followed_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
