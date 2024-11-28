import datetime
from django.db import models

class Laboratorio(models.Model):
    id = models.AutoField(primary_key=True)
    nom_lab = models.CharField(max_length=255, verbose_name='nombre')
    city_lab = models.CharField(max_length=255, verbose_name='ciudad', default=None)
    pais_lab = models.CharField(max_length=255, verbose_name='pais', default=None)
    creado_lab = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    actualizado_lab = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        db_table = 'Laboratorio'
        verbose_name = 'Laboratorio'
        verbose_name_plural = 'Laboratorios'

    def __str__(self):
        return self.nom_lab


class DirectorGeneral(models.Model):
    
    id = models.AutoField(primary_key=True)
    nom_dire = models.CharField(max_length=255, verbose_name='nombre')
    #lab_dire = models.OneToOneField('Laboratorio', on_delete=models.CASCADE)
    lab_dire = models.OneToOneField(Laboratorio, on_delete=models.CASCADE, related_name='director')
    especialidad = models.CharField(max_length=255, verbose_name='especialidad', default=None)
    creado_dire = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    actualizado_dire = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        db_table = 'Director General'
        verbose_name = 'Director General'
        verbose_name_plural = 'Directores Generales'

    def __str__(self):
        return self.nom_dire

#anios_choices = []

#for anio in range(2015, (datetime.datetime.now().year+1)):
#    anios_choices.append((anio, anio))

def anio_actual():
        return int(datetime.date.today().year)

class Producto(models.Model):
    anios_choices = [
        (anio, str(anio)) for anio in range(2015, 2051)
    ]
    id = models.AutoField(primary_key=True)
    nom_prod = models.CharField(max_length=255, verbose_name='Producto')
    lab_prod = models.ForeignKey('Laboratorio', on_delete=models.SET_NULL, blank=True, null=True)
    f_fabricacion = models.IntegerField(choices=anios_choices, default=anio_actual, verbose_name='F Fabricación')
    p_costo = models.DecimalField(null=False, max_digits=12, decimal_places=2, verbose_name='P Costo')
    p_venta = models.DecimalField(null=False, max_digits=12, decimal_places=2, verbose_name='P Venta')
    creado_prod = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    actualizado_prod = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        db_table = 'Producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nom_prod