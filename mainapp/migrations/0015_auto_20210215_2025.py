# Generated by Django 3.1.5 on 2021-02-15 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_order_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Опис'),
        ),
    ]
