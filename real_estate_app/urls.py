"""
URL configuration for real_estate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página de inicio
    path('propiedades/', views.listar_propiedades, name='listar_propiedades'),
    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(template_name='real_estate_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('mi-cuenta/', views.mi_cuenta, name='mi_cuenta'),
    path('mis-propiedades/', views.mis_propiedades, name='mis_propiedades'),
    path('crear_propiedad/', views.crear_propiedad, name='crear_propiedad'),
    path('suscripcion/', views.suscripcion, name='suscripcion'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
