# Generated by Django 3.1 on 2020-09-25 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_product_prddiscountprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDISBestSeller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDISNew',
            field=models.BooleanField(default=True),
        ),
    ]
