# Generated by Django 3.1 on 2020-09-24 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200924_0318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_alternative',
            name='PALNProduct',
        ),
        migrations.AddField(
            model_name='product_alternative',
            name='PALNproduct',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='product.product', verbose_name='Product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product_alternative',
            name='PALNAlternatives',
            field=models.ManyToManyField(related_name='alternative_product', to='product.Product', verbose_name='Alternatives'),
        ),
        migrations.CreateModel(
            name='Product_Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PACCAlternatives', models.ManyToManyField(related_name='accessories_products', to='product.Product', verbose_name='Accessories')),
                ('PACCProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainAccessory_product', to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Accessory',
                'verbose_name_plural': 'Accessorios',
            },
        ),
    ]
