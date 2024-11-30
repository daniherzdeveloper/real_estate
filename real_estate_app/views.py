from django.shortcuts import render, redirect
from .models import Propiedad
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    propiedades = Propiedad.objects.filter(
        propietario__profile__activo_para_publicar=True,  # Filtra por propietarios activos
        destacada=True  # Filtra solo propiedades destacadas
    )
    return render(request, 'real_estate_app/home.html', {'propiedades': propiedades})


def listar_propiedades(request):
    propiedades = Propiedad.objects.filter(propietario__profile__activo_para_publicar=True)
    return render(request, 'real_estate_app/listar_propiedades.html', {'propiedades': propiedades})


def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro completado. ¡Bienvenido!')
            return redirect('login')  # Cambia 'login' si tienes otra ruta para el inicio de sesión
    else:
        form = CustomUserCreationForm()
    return render(request, 'real_estate_app/registro.html', {'form': form})

@login_required
def mi_cuenta(request):
    return render(request, 'real_estate_app/mi_cuenta.html')

@login_required
def mis_propiedades(request):
    # Verificar si el usuario tiene activo_para_publicar en True
    if not request.user.profile.activo_para_publicar:  # Accede al perfil relacionado
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('/')  # Redirige a la página de inicio o cualquier otra página
    
    # Si el usuario tiene permiso, renderiza el template
    tipo_choices = Propiedad.TIPO_PROPIEDAD_CHOICES 
    propiedades = Propiedad.objects.filter(propietario=request.user)
    
    return render(request, 'real_estate_app/mis_propiedades.html', {
        'propiedades': propiedades,
        'tipo_choices': tipo_choices
    })


@login_required
def crear_propiedad(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        lugar = request.POST.get('lugar')
        tipo = request.POST.get('tipo')
        banios = request.POST.get('banios')
        cuartos = request.POST.get('cuartos')
        imagen = request.FILES.get('imagen')  # Manejo de archivos
        
        Propiedad.objects.create(
            propietario=request.user,
            titulo=titulo,
            descripcion=descripcion,
            precio=precio,
            lugar=lugar,
            tipo=tipo,
            banios=banios,
            cuartos=cuartos,
            imagen=imagen,
        )
        return redirect('mis_propiedades')  # Redirige a la vista de propiedades
    return render(request, 'real_estate_app/mis_propiedades.html')

@login_required
def suscripcion(request):
    return render(request, 'real_estate_app/suscripcion.html')



