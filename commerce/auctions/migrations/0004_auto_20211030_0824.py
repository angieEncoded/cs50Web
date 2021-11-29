# Generated by Django 3.2.8 on 2021-10-30 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20211030_0808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bids',
            old_name='item_name',
            new_name='item_id',
        ),
        migrations.AlterField(
            model_name='auctions',
            name='listed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_auctions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_comments', to='auctions.auctions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]