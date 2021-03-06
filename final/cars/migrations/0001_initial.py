# Generated by Django 3.2.12 on 2022-02-08 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('mudel', models.IntegerField()),
                ('transmission', models.CharField(max_length=100)),
                ('engin_size', models.CharField(max_length=100)),
                ('powerBHP', models.CharField(max_length=100)),
                ('distance_meter', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('price', models.FloatField()),
                ('is_salled', models.BooleanField(verbose_name='is salled')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='cars.brands', verbose_name='brands')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('total', models.DecimalField(blank=True, decimal_places=0, max_digits=1000, null=True, verbose_name='total')),
                ('note', models.CharField(blank=True, max_length=100, null=True, verbose_name='note')),
                ('ordered', models.BooleanField(verbose_name='ordered')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car', verbose_name='car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='car/', verbose_name='image')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='cars.car', verbose_name='car')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
