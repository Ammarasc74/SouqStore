# Generated by Django 3.1 on 2020-09-24 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200924_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATDImg',
            field=models.ImageField(upload_to='category/', verbose_name='Image'),
        ),
    ]