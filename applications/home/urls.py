from django.urls import path

from . import views


app_name = 'home_app'

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),

    #path('registro-suscripcion', views.Suscribir.as_view(), name='suscribir'),
    #path('registro-contacto', views.ContactCreateView.as_view(), name='crear_contacto'),

]
