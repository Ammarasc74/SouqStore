# Generated by Django 3.1 on 2020-09-23 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDIImage', models.ImageField(upload_to='prodcut/', verbose_name='Image')),
            ],
        ),
        migrations.DeleteModel(
            name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCost',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cost'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCreated',
            field=models.DateTimeField(auto_now=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDDescriptions',
            field=models.TextField(max_length=1000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDName',
            field=models.CharField(max_length=50, verbose_name='Product Name '),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDPrice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='PRDIProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product'),
        ),
    ]