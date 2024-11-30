from django.contrib import admin
from .models import UserProfile, Propiedad

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'activo_para_publicar')
    list_editable = ('activo_para_publicar',)

@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'propietario', 'precio', 'tipo', 'lugar', 'fecha_publicacion', 'destacada')
    list_filter = ('tipo', 'lugar', 'fecha_publicacion')
    list_editable = ('destacada',)
    search_fields = ('titulo', 'descripcion', 'lugar')
    ordering = ('-fecha_publicacion',)
