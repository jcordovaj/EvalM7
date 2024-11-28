from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio
from django.contrib.auth.models import User

class LaboratorioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for l in range(1, 5):
            Laboratorio.objects.create(
                nom_lab=f"Laboratorio{l}",
                city_lab=f"Ciudad{l}",
                pais_lab=f"Pais{l}"
                )

    def test_laboratorio_guardar_datos(self):
        """Comprueba que los datos del laboratorio se hayan guardado correctamente."""
        laboratorio = Laboratorio.objects.get(nom_lab="Laboratorio3")
        self.assertEqual(laboratorio.city_lab, "Ciudad3")
        self.assertEqual(laboratorio.pais_lab, "Pais3")

    def test_laboratorio_edit_url(self):
        """Comprueba que la URL de edición de un laboratorio devuelve un status 200."""
        user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        laboratorio = Laboratorio.objects.create(
            nom_lab="Laboratorio2",
            city_lab="Ciudad2",
            pais_lab="Pais2"
        )
        url = reverse('editar_lab', kwargs={'pk': laboratorio.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
     
    def test_laboratorio_RegistroView(self):
        """Comprueba que la vista REGISTRO responde correctamente."""
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registro.html') 
    
    def test_laboratorio_IndexView(self):
        """Comprueba que la vista del INDEX de laboratorios responde correctamente."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        
    def test_laboratorio_edit2_url(self):
        """Comprueba que la URL de edición de un laboratorio devuelve un status 200."""
        user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        laboratorio = Laboratorio.objects.get(nom_lab="Laboratorio4")
        url = reverse('editar_lab', kwargs={'pk': laboratorio.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    #def test_eliminar_lab_view(self):
    #    """Verifica que la página de eliminación de laboratorio funciona correctamente."""
    #    user = User.objects.create_user(username='testuser3', password='password3')
    #    self.client.login(username='testuser3', password='password3')
    #    laboratorio = Laboratorio.objects.get(nom_lab="Laboratorio1")        
    #    url = reverse('eliminar_lab', kwargs={'pk': self.laboratorio.pk})
    #    response = self.client.get(url)
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, 'delete_lab.html')
    #    expected_text = f"ELIMINAR LABORATORIO {self.laboratorio.nom_lab}"
    #    self.assertContains(response, expected_text)

