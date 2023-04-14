from django.db import models
import uuid

class Rostovka(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    size = models.BigIntegerField(max_length=3, blank=True, default='')
    expended_material = models.FloatField(default='', blank=True)
    id_product = models.CharField(max_length=40, blank=True, default='')

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=40, blank=True, default='')
    cost = models.FloatField(blank=True, default='')
    id_material = models.CharField(max_length=40, blank=True, default='')

class Material(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=40, blank=True, default='')
    stock_balance = models.FloatField(blank=True, default='')
    cost_per_square_meter = models.FloatField(blank=True, default='')
# Create your models here.
