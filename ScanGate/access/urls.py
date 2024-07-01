from django.urls import path
from . import views

urlpatterns = [
    path('', views.access, name = 'access'),
    path('perfil/<str:codigo_barras>/', views.perfil, name = 'perfil'),
    path('login/', views.login_view, name='login')
]
