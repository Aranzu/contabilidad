from django.db import models
from django.utils import timezone
from django.db.models import Sum, Count

# Create your models here.

class AnexoBoleta(models.Model):
    rut = models.CharField(max_length=100, primary_key=True)
    nombre_cl = models.CharField(max_length=100)
    num_telf = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=100)
    total = models.IntegerField(default=0)
    total_dev = models.IntegerField(default=0)
    monto_dev = models.IntegerField(default=0)