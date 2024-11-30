from django.http import Http404
from django.views import View
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.auth import login, authenticate, logout
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LabForm, RegistroUsuarioForm, DireForm, ProdForm
from django.db.models import Q
from .models import Laboratorio, Producto, DirectorGeneral
import datetime

# Index
class IndexView(View):
    def get(self, request):
        return render(request, "index.html")

# Error 404
class Error404View(View):
    def get(self, request):
        return render(request, "error404.html")

# Agregar un Laboratorio
class LabAddView(LoginRequiredMixin, View):
    login_url = '/login/'         # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redirección

    def get(self, request):
        form = LabForm()
        return render(request, "lab_add.html", {"form": form})

    def post(self, request):
        form = LabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("correct_addView")
        return render(request, "lab_add.html", {"form": form})
    
# Agregar un Producto
class ProductoAddView(LoginRequiredMixin, View):
    login_url = '/login/'         # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redirección

    def get(self, request):
        form = ProdForm()
        return render(request, "prod_add.html", {"form": form})

    def post(self, request):
        form = ProdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("correct_add_prod")
        return render(request, "prod_add.html", {"form": form})    
    
# Agregar un Director
class DireAddView(LoginRequiredMixin, View):
    login_url = '/login/'         # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redirección

    def get(self, request):
        form = DireForm()
        return render(request, "dire_add.html", {"form": form})

    def post(self, request):
        form = DireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("correct_addViewDire")
        return render(request, "dire_add.html", {"form": form})    

# Listar Laboratorios y mostrar barra de filtros
class ListarLabsView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'

    anios_choices = []

    for anio in range(2015, (datetime.datetime.now().year + 1)):
        anios_choices.append((anio, anio))
    
    def get(self, request):
        labs  = Laboratorio.objects.prefetch_related('producto_set').all()
        query = request.GET.get("query")
        
        nom_lab  = request.GET.get("nom_lab")
        pais_lab = request.GET.get("pais_lab")
        city_lab = request.GET.get("city_lab")
        anio = request.GET.get("anio")
        nom_prod = request.GET.get("nom_prod")
  
        if query:
            labs = labs.filter(
                Q(nombre__icontains=query) | # Filtrar por nombre de Laboratorio
                Q(directorgeneral__nombre__icontains=query)  # Filtrar por nombre del director
            )
        
        if nom_lab:
            labs = labs.filter(nom_lab__icontains=nom_lab)
        if pais_lab:
            labs = labs.filter(pais_lab__icontains=pais_lab)
        if city_lab:
            labs = labs.filter(city_lab__icontains=city_lab)
        if anio:
            labs = labs.filter(producto__f_fabricacion=anio)  # Filtrar por año de fabricación del producto
        if nom_prod:
            labs = labs.filter(producto__nom_prod__icontains=nom_prod)  # Por nombre de producto    
        
        producto_choices = Producto.objects.values_list('nom_prod', flat=True).distinct()    
        
        context = {'labs': labs,
                'producto_choices': producto_choices,
                'nom_lab_choices': Laboratorio.objects.values_list('nom_lab', flat=True).distinct(),
                'pais_choices': Laboratorio.objects.values_list('pais_lab', flat=True).distinct(),
                'city_choices': Laboratorio.objects.values_list('city_lab', flat=True).distinct(),
                'anio_choices': Producto.anios_choices,
            }
        return render(request, "listar.html", context)

# Listar Productos y barra de filtros
class ListarProductosView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        productos = Producto.objects.all()
        query = request.GET.get("query")
        nom_prod = request.GET.get("nom_prod")
        lab_prod = request.GET.get("lab_prod")
        f_fabricacion = request.GET.get("f_fabricacion")

        # Filtrar por cadena de texto
        if query:
            productos = productos.filter(Q(nom_prod__icontains=query))

        # Filtrar por producto
        if nom_prod:
            productos = productos.filter(nom_prod__icontains=nom_prod)

        # Filtrar por laboratorio
        if lab_prod:
            productos = productos.filter(lab_prod__id=lab_prod)

        # Filtrar por año de fabricación
        if f_fabricacion:
            productos = productos.filter(f_fabricacion=f_fabricacion)

        # Obtener valores únicos para filtros
        laboratorios = Laboratorio.objects.all()
        productos_nombres = productos.values_list('nom_prod', flat=True).distinct()
        fabricacion_anios = productos.values_list('f_fabricacion', flat=True).distinct()

        context = {
            'productos': productos,
            'laboratorios': laboratorios,
            'productos_nombres': productos_nombres,
            'fabricacion_anios': fabricacion_anios,
            'query': query,
            'nom_prod': nom_prod,
            'f_fabricacion': f_fabricacion,
        }
        return render(request, "listar_prods.html", context)

# Listar Directores Generales
class ListarDiresView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        #directores_generales = DirectorGeneral.objects.all()
        directores_generales = DirectorGeneral.objects.select_related('lab_dire').all()
        query    = request.GET.get("query")
        nom_dire = request.GET.get("nom_dire")
        lab_dire = request.GET.get("lab_dire")

        if query:
            directores_generales = directores_generales.filter(
                Q(nom_dire__icontains=query)
            )
        if nom_dire:
            directores_generales = directores_generales.filter(nom_dire__icontains=nom_dire)
        if lab_dire:
            # Filtrar por laboratorio usando su ID
            try:
                lab_id = int(lab_dire)
                directores_generales = directores_generales.filter(lab_dire__id=lab_id)
            except ValueError:
                raise Http404("ID de laboratorio inválido")
            
        context = {
            'directores_generales': directores_generales,
            'laboratorios': Laboratorio.objects.all(),
            'query': query,
            'nom_dire': nom_dire,
            'lab_dire': lab_dire,
        }
        return render(request, "listar_dires.html", context)

# Add Director con exito
def correct_addViewDire(request):
    return render(request, "correct_add_dire.html")

# Add Laboratorio con exito
def correct_addView(request):
    return render(request, "correct_add.html")

# Add Producto con exito
def correct_addViewProd(request):
    return render(request, "correct_add_prod.html")

# Actualizar Laboratorio
class LabUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        lab = get_object_or_404(Laboratorio, pk=pk)
        form = LabForm(instance=lab)
        return render(request, "lab_edit.html", {"form": form, "laboratorio": lab})

    def post(self, request, pk):
        lab = get_object_or_404(Laboratorio, pk=pk)
        form = LabForm(request.POST, instance=lab)
        if form.is_valid():
            form.save()
            messages.success(request, "Laboratorio actualizado con éxito.")
            return redirect("listar") 
        return render(request, "lab_edit.html", {"form": form, "laboratorio": lab})

# Actualizar Director
class DireUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        dire = get_object_or_404(DirectorGeneral, pk=pk)
        form = DireForm(instance=dire)
        return render(request, "dire_edit.html", {"form": form, "directorgeneral": dire})

    def post(self, request, pk):
        dire = get_object_or_404(DirectorGeneral, pk=pk)
        form = DireForm(request.POST, instance=dire)
        if form.is_valid():
            form.save()
            messages.success(request, "Datos del Director actualizados con éxito.")
            return redirect("listar_dires")  # 
        return render(request, "dire_edit.html", {"form": form, "directorgeneral": dire})

# Actualizar Producto
class ProdUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        prod = get_object_or_404(Producto, pk=pk)
        form = ProdForm(instance=prod)
        return render(request, "prod_edit.html", {"form": form, "producto": prod})

    def post(self, request, pk):
        prod = get_object_or_404(Producto, pk=pk)
        form = ProdForm(request.POST, instance=prod)
        if form.is_valid():
            form.save()
            messages.success(request, "El Producto ha sido actualizado con éxito.")
            return redirect("listar_prods")  # 
        return render(request, "prod_edit.html", {"form": form, "producto": prod})

# Eliminar Laboratorio    
class LabDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        lab = get_object_or_404(Laboratorio, pk=pk)
        return render(request, 'delete_lab.html', {'laboratorio': lab})

    def post(self, request, pk):
        lab = get_object_or_404(Laboratorio, pk=pk)
        lab.delete()
        messages.success(request, "El Laboratorio ha sido eliminado.")
        return redirect("listar")    
    
# Eliminar Director
class DireDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        dire = get_object_or_404(DirectorGeneral, pk=pk)
        return render(request, 'delete_dire.html', {'directorgeneral': dire})
    
    def post(self, request, pk):
        dire = get_object_or_404(DirectorGeneral, pk=pk)
        dire.delete()
        messages.success(request, "El Director ha sido eliminado.")
        return redirect("listar_dires")    

# Eliminar Producto
class ProdDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        prod = get_object_or_404(Producto, pk=pk)
        return render(request, 'delete_prod.html', {'producto': prod})
    def post(self, request, pk):
        prod = get_object_or_404(Producto, pk=pk)
        prod.delete()
        messages.success(request, "El Producto ha sido eliminado.")
        return redirect("listar_prods")    

# Registrar un nuevo usuario
class RegistroView(View):
    def get(self, request):
        form = RegistroUsuarioForm()
        context = {"register_form": form}
        return render(request, "registro.html", context)

    def post(self, request):
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso.")
            return redirect("/")
        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
            context = {"register_form": form}
            return render(request, "registro.html", context)

# Login
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {"login_form": form}
        return render(request, "login.html", context)

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesion como: {username}.")
                return redirect("/")
            else:
                messages.error(request, "Ha ocurrido un error, vuelva a ingresar sus datos o regístrese")
        else:
            messages.error(request, "Ha ocurrido un error, vuelva a ingresar sus datos o regístrese")

        context = {"login_form": form}
        return render(request, "login.html", context)

# Logout
class LogoutView(LoginRequiredMixin, View):
    login_url = '/login/'  # URL de inicio de sesión
    redirect_field_name = 'next'  # Nombre del campo de redirección

    def get(self, request):
        logout(request)
        messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
        return redirect("/")
