# Generated by Django 3.0 on 2020-02-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('off_sub', '0008_auto_20200226_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(max_length=1000),
        ),
    ]
