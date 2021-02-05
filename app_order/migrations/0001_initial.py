# Generated by Django 3.1.4 on 2021-02-05 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', related_query_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create At')),
                ('description', models.CharField(max_length=150, verbose_name='Description')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', related_query_name='order', to='app_order.cart', verbose_name='Cart')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', related_query_name='payment', to='app_order.order', verbose_name='Order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', related_query_name='payment', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Count')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', related_query_name='order_item', to='app_order.order', verbose_name='Order')),
                ('shop_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', related_query_name='order_item', to='app_product.shopproduct', verbose_name='Shop Product')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', related_query_name='cart_item', to='app_order.cart', verbose_name='Cart')),
                ('shop_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', related_query_name='cart_item', to='app_product.shopproduct', verbose_name='Shop Product')),
            ],
            options={
                'verbose_name': 'Cart Item',
                'verbose_name_plural': 'Cart Items',
            },
        ),
    ]
