from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from recepcion_boleta.views import (
	anexo_boleta_view
	)
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("AnexoBoleta",views.AnexoBoletaApi, basename="AnexoBoleta")

urlpatterns = [
    path('',include(router.urls)),
    path('anexo/<int:pk>/', anexo_boleta_view, name= "anexo"),
]