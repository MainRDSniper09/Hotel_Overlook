from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Product, Order

class DashboardTests(TestCase):

    def setUp(self):
        """Configuración inicial de pruebas"""
        self.client = Client()
        self.admin_user = User.objects.create_superuser(username='admin', password='admin123')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.product = Product.objects.create(name="Producto Prueba")
        self.order = Order.objects.create(customer=self.user)

    def test_index_view(self):
        """Prueba que el index carga correctamente"""
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('dashboard-index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/index.html')

    def test_products_view(self):
        """Prueba la vista de productos"""
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('dashboard-products'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Producto Prueba")

    def test_product_detail_view(self):
        """Prueba la vista de detalles del producto"""
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('dashboard-products-detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)


    def test_product_edit_view(self):
        """Prueba la vista de edición de productos"""
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('dashboard-products-edit', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)


def test_product_delete_view(self):
    """Prueba la vista de eliminación de productos"""
    self.client.login(username='admin', password='admin123')

    # Enviar la solicitud POST para eliminar el producto
    response = self.client.post(reverse('dashboard-products-delete', args=[self.product.id]), follow=True)

    # Verificar que se eliminó y redirigió correctamente
    self.assertRedirects(response, reverse('dashboard-products'))  # Asegurar que redirige a la lista de productos
    self.assertFalse(Product.objects.filter(id=self.product.id).exists())  # Verificar que el producto fue eliminado


def test_customers_view(self):
        """Prueba la vista de clientes"""
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('dashboard-customers'))
        self.assertEqual(response.status_code, 200)

def test_customer_detail_view(self):
        """Prueba la vista de detalle de cliente"""
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('dashboard-customer-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)

def test_order_view(self):
        """Prueba la vista de órdenes"""
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('dashboard-order'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)