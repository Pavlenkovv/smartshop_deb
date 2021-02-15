# Generated by Django 3.1.5 on 2021-02-07 18:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20210207_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=255, verbose_name='Прізвище')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адреса')),
                ('status', models.CharField(choices=[('new', 'Нове замщвлення'), ('in_progress', 'Замовлення в обробці'), ('is_ready', 'Замовлення готове'), ('completed', 'Замовлення виконане')], default='new', max_length=100, verbose_name='Статус замовлення')),
                ('buying_type', models.CharField(choices=[('self', 'Самовивіз'), ('delivery', 'Доставка')], default='self', max_length=100, verbose_name='Тип доставки')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Коментар до замовлення')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата створення замовлення')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата отримання замовлення')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='mainapp.customer', verbose_name='Покупець')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_customer', to='mainapp.Order', verbose_name='Замовлення покупця'),
        ),
    ]