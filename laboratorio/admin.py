from django.contrib import admin
from .models import DirectorGeneral, Laboratorio, Producto
from django.urls import reverse
from django.template.loader import render_to_string

"""
Class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('nom_dire', 'lab_dire_link')
    search_fields = ('nom_dire', 'lab_dire__nom_lab')
    ordering = ('nom_dire',)

    def lab_dire_link(self, obj):
        change_url = reverse('admin:laboratorio_laboratorio_change', args=[obj.lab_dire.id])
        return format_html('<a href="{}">{}</a>', change_url, obj.lab_dire.nom_lab)
    lab_dire_link.admin_order_field = 'lab_dire'
    lab_dire_link.short_description = 'Laboratorio'

admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
"""
class LaboratorioAdmin(admin.ModelAdmin):
    list_display  = ('nom_lab', 'city_lab', 'pais_lab')
    list_filter   = ('nom_lab', 'pais_lab')
    search_fields = ('nom_lab',)

    # Si deseas ordenar por un campo en particular:
    ordering = ('-nom_lab',)

admin.site.register(Laboratorio, LaboratorioAdmin)


class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('nom_dire', 'lab_dire')  # Access laboratory name through related field
    search_fields = ('nom_dire', 'lab_dire__nom_lab')  # Search by director name and lab name

    # Order by director name
    ordering = ('nom_dire',)

    # Filter by laboratory name (optional)
    # list_filter = ('lab_dire__nom_lab',)  # Uncomment to add a filter by lab name

    def lab_dire(self, obj):
        
        #Custom method to return the name of the associated laboratory.
        
        return obj.lab_dire.nom_lab  # Access the related laboratory and its name

admin.site.register(DirectorGeneral, DirectorGeneralAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display  = ('nom_prod', 'lab_prod', 'f_fabricacion', 'p_costo', 'p_venta')
    list_filter   = ('lab_prod', 'nom_prod')
    search_fields = ('nom_prod',)

    # Si deseas ordenar por un campo en particular:
    ordering = ('-f_fabricacion',)

admin.site.register(Producto, ProductoAdmin)