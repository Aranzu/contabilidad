from .models import AnexoBoleta
from rest_framework import serializers
from django.utils import timezone

class AnexoBoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnexoBoleta
        fields = "__all__"