# Generated by Django 3.0 on 2020-02-19 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('off_sub', '0004_auto_20200212_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
