# Generated by Django 3.1 on 2020-09-25 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20200924_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDSLug',
            field=models.SlugField(blank=True, null=True, verbose_name='Product URL'),
        ),
    ]