# Generated by Django 4.2.1 on 2023-06-15 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_savedcarts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='regularpizza',
            name='category_description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sicilianpizza',
            name='category_description',
            field=models.CharField(max_length=200),
        ),
    ]
