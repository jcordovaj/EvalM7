"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from laboratorio.views import  IndexView, DireAddView, DireDeleteView, DireUpdateView, correct_addViewDire, ListarDiresView, ProductoAddView, ProdDeleteView, ProdUpdateView, correct_addViewProd, ListarProductosView, LabAddView, LabDeleteView, LabUpdateView, ListarLabsView, LoginView, RegistroView, LogoutView, correct_addView
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('error404/', TemplateView.as_view(template_name='error404.html'), name='error404'),

    # LABORATORIOS        
    path('lab/add/', LabAddView.as_view(), name='lab_add'),
    path('lab/listar/', ListarLabsView.as_view(), name='listar'),
    path("lab/", correct_addView, name="correct_addView"),
    path('lab/<int:pk>/eliminar/', LabDeleteView.as_view(), name='eliminar_lab'),
    path('lab/<int:pk>/editar/', LabUpdateView.as_view(), name='editar_lab'),
        
    # PRODUCTOS
    path('prod/add/', ProductoAddView.as_view(), name='prod_add'),
    path('prod/listar/', ListarProductosView.as_view(), name='listar_prods'),
    path("prod/", correct_addViewProd, name="correct_add_prod"),
    path('prod/<int:pk>/eliminar/', ProdDeleteView.as_view(), name='eliminar_prod'),
    path('prod/<int:pk>/editar/', ProdUpdateView.as_view(), name='editar_prod'),
    
    # DIRECTORES
    path('dire/add/', DireAddView.as_view(), name='dire_add'),
    path('dire/listar/', ListarDiresView.as_view(), name='listar_dires'),
    path("dire/", correct_addViewDire, name="correct_add_dire"),
    path('dire/<int:pk>/eliminar/', DireDeleteView.as_view(), name='eliminar_dire'),
    path('dire/<int:pk>/editar/', DireUpdateView.as_view(), name='editar_dire'),
    
    # AUTENTICACIÓN Y REGISTRO        
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]
