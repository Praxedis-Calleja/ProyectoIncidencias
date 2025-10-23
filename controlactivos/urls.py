from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping, name='ping'),
    path('prueba-bd/', views.prueba_bd, name='prueba_bd'),  # ← esta
]
