from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    activo_para_publicar = models.BooleanField(default=False)  # Controla si el usuario puede publicar

    def __str__(self):
        return self.user.username


class Propiedad(models.Model):
    TIPO_PROPIEDAD_CHOICES = [
        ('venta', 'En Venta'),
        ('alquiler', 'En Alquiler'),
        ('construcción', 'En Construcción'),
    ]

    propietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='propiedades')
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    lugar = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, choices=TIPO_PROPIEDAD_CHOICES)
    banios = models.PositiveIntegerField()
    cuartos = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='propiedades/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    destacada = models.BooleanField(default=False)  # Campo para controlar si es destacada

    def __str__(self):
        return f"{self.titulo} - {self.propietario.username}"

    def get_detalle_url(self):
        return f"/propiedad/{self.id}/"

    def get_contactar_url(self):
        return f"/contactar/{self.id}/"

