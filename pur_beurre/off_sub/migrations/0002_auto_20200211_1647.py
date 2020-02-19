# Generated by Django 3.0 on 2020-02-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('off_sub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='products', to='off_sub.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='stores',
            field=models.ManyToManyField(blank=True, related_name='products', to='off_sub.Store'),
        ),
    ]
