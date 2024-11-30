# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User  # Importamos el modelo User
from .models import UserProfile  # Importamos el modelo UserProfile

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    """Crea un perfil de usuario automáticamente cuando se crea un usuario"""
    if created:
        UserProfile.objects.create(user=instance)  # Creamos el perfil relacionado

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    """Guarda el perfil del usuario cuando se guarda el usuario"""
    instance.profile.save()  # Guarda el perfil del usuario cada vez que se guarda el usuario
