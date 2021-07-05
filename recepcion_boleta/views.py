from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from .serializers import AnexoBoletaSerializer
from .models import AnexoBoleta
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import render
import requests
from django.views.generic import ListView, TemplateView

class AnexoBoletaApi(viewsets.ModelViewSet):
    queryset = AnexoBoleta.objects.all()
    serializer_class = AnexoBoletaSerializer

@api_view(['POST'])
def anexo_boleta_view(request):
    serializer = AnexoBoletaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)