# Generated by Django 3.1 on 2020-10-22 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_auto_20201022_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productorder',
            name='PRDOrder',
        ),
    ]
