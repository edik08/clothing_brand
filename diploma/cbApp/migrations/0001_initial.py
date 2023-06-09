# Generated by Django 4.1.7 on 2023-04-02 21:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='', max_length=40)),
                ('stock_balance', models.FloatField(blank=True, default='')),
                ('cost_per_square_meter', models.FloatField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='', max_length=40)),
                ('cost', models.FloatField(blank=True, default='')),
                ('id_material', models.CharField(blank=True, default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Rostovka',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('size', models.BigIntegerField(blank=True, default='', max_length=3)),
                ('expended_material', models.FloatField(blank=True, default='')),
                ('id_product', models.CharField(blank=True, default='', max_length=40)),
            ],
        ),
    ]
